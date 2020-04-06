# 5-MongoDB数据库

## 介绍
官方文档：http://www.mongoing.com/docs/

### 文档

MongoDB是一个面向文档的数据库
 举例：{“foo”:3, “greeting”:“Hello,world!”}
 区分大小写，且key唯一，不可重复，文档可嵌套

### 集合

集合就是一组文档
 文档类似于关系型数据库里的行
 集合类似于关系型数据库里的表
 集合中的文档无需固定额结构（与关系型数据库的区别）

### 集合的命名

1. 不能有空字符串（" "）
2. 不能包含\0字符（空字符）
3. 不能使用system.的前缀（系统保留）
4. 建议不包含保留字 "$"
5. 用 .  分割不懂命名空间的子集合（如：blog.users， blog.posts）

### 数据库

1. 多个文档组成集合，多个集合组成数据库
2. 一个实例可以承载多个数据库
3. 每个数据库都有独立的权限
4. 保留的数据名称（admin,local,config）

## MongoDB安装启动

下载mis包，安装在根目录下MongoDB文件夹里就OK，例如：D：\MongDB......。切记一开始安装不要选择附带安装compass图形工具，这个下载很慢可能直接卡死。

启动：
 配置数据路径
 在目录D:\MongoDB\Server\4.0的bin文件使用'Shift'+'右键'选择在此处打开cmd，然后再cmd中输入：monogod --dbpath D:\MongoDB\Server\4.0\data
 回车，来到NETWORK  [thread1] waiting for connections on port 27017
 此时，在bin里打开另一个cmd，输入mongo，回车，就OK啦
 可以使用 show databases 试一试

### 使用命令行操作数据库（CRUD）

新增数据（Create）
```bash
# 进入数据库，如果没有该数据库，会自动创建
use students； 
# 新增数据
stu = {
  name:'Jhon',
  age:21}
# 插入数据到数据库
db.students.insert(stu)
```
查询数据（Read）
```css
# 查询students中的所有数据
db.students.find()
# 查询students中的一条数据
db.students.findOne()
```
修改数据（Update）

```bash
# 需要先查询这条数据
s = db.students.findOne()
# 修改数据=替换数据，替换后的数据没有年龄
db.students.update({name: 'Jhon'}, {name: 'JhonC'})
```

删除数据（Delete）


```css
# 删除该属性的数据
db.students.remove({name: 'JhonC'})
# 删除students中的所有数据
db.students.remove(())
```
练习：
```csharp
# 新建并进入数据库
use students
# 查看当前数据库
db.log
#插入多条数据
db.students.insertMany(
    [
        { name:"bob", age:16, sex: "male", grade:95},
        { name:"ahn", age:18, sex: "female", grade:45},
        { name:"xi", age:15, sex: "male", grade:75},
        { name:"bob1", age:16, sex: "male", grade:95},
        { name:"ahn1", age:18, sex: "male", grade:45},
        { name:"xi1", age:15, sex: "female", grade:55},
        { name:"bob2", age:16, sex: "female", grade:95},
        { name:"ahn2", age:18, sex: "male", grade:60},
        { name:"xi2", age:15, sex: "male", grade:75},
        { name:"bob3", age:16, sex: "male", grade:95},
        { name:"ahn3", age:18, sex: "female", grade:45},
        { name:"xi3", age:15, sex: "male", grade:85},
        { name:"bob4", age:16, sex: "female", grade:95},
        { name:"ahn4", age:18, sex: "male", grade:45},
        { name:"xi4", age:15, sex: "male", grade:75}
    ]
)
# 查看所有数据
db.students.find()
# 查看数据数量
db.students.count()
# cls 清屏
# 查询所有男生数据
db.students.find({sex: 'male'})
# 查询所有及格学生信息
db.students.find({grade:{'$gte':60}})
# 查询所有18岁男生和16岁女生的数据
db.students.find({'$or':[{sex:'male', age:18}, {sex: 'female', age:16}]})
# 按照学生的年龄进行排序（1代表升序，-1代表降序）
db.students.find().sort({age: 1})
# 给所有学生都加一个地址=china的字段属性（修改器操作）
db.students.update({}, {'$set':{adress:'china'}}, {multi:true})
# 给所有女学生都加一岁（修改器操作）
db.students.update({sex:'female'}, {'$inc':{age:1}}, {multi: true})
```

## 使用Python连接MongoDB

手动启动MongoDB
 在MongoDB的bin目录打开cmd 输入 monogod --dbpath D:\MongoDB\Server\4.0\data

```python
# 建立客户端连接的三种方法
from pymongo import MongoClient
client = MongoClient()
# client2 = MongoClient('localhost', 27017)
# client3 = MongoClient('mongodb://localhost:27017')
# 显示数据库
dbs = client.list_database_names()
print(dbs)
# 进入某个数据库
db = client.blog
```

###  curd完整示例代码
```python
from pymongo import MongoClient
from bson.objectid import ObjectId


class TestMongo(object):

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['students']

    def add_one(self):
        '''新增数据'''
        post ={
            'name': 'ben',
            'age': 18,
            'sex': "male",
            'grade': 80,
            'adress': "china"
        }
        return self.db.students.insert_one(post)
    def add_many(self):
        '''新增多条数据'''
        infos = [
            {'name': 'ben', 'age': 18, 'sex': "male", 'grade': 80, 'adress': "china"},
            {'name': 'sum', 'age': 19, 'sex': "male", 'grade': 75, 'adress': "china"},
            {'name': 'lily', 'age': 16, 'sex': "female", 'grade': 90, 'adress': "china"},
            {'name': 'teddy', 'age': 19, 'sex': "male", 'grade': 65, 'adress': "china"},
            {'name': 'fluence', 'age': 18, 'sex': "female", 'grade': 80, 'adress': "china"}
            ]
        return self.db.students.insert_many(infos)

    def get_one(self):
        '''查询一条数据'''
        return self.db.students.find_one()

    def get_more(self):
        '''查询多条数据'''
        return self.db.students.find({'age': 18})

    def get_one_from_oid(self, oid):
        '''查询指定ID的数据'''
        obj = ObjectId(oid)
        return self.db.students.find_one({'_id': obj})

    def update_one(self):
        '''修改一条数据'''
        return self.db.students.update_one({'age': 20}, {'$inc': {'x': 10}})

    def update_many(self):
        '''修改多条数据'''
        return self.db.students.update_many({}, {'$inc': {'age': 5}})

    def dalete_one(self):
        '''删除一条数据'''
        return self.db.students.delete_one({'name': 'ben'})

    def delete_many(self):
        '''删除多条数据'''
        return self.db.students.delete_many({'age': 24})

def main():
    obj = TestMongo()
    # rest = obj.add_one()
    # print(rest)

    # rest = obj.add_many()
    # print(rest)

    # rest = obj.get_one()
    # print(rest)

    # rest = obj.get_more()
    # for i in rest:
    #     print(i['_id'])

    # rest = obj.get_one_from_oid('5c68b5cb5a49891b40b8a18e')
    # print(rest)

    # rest = obj.update_one()
    # print(rest)

    # rest = obj.update_many()
    # print(rest)

    # rest = obj.delete_one()
    # print(rest.delete_count)

    # rest = obj.delete_many()
    # print(rest.delete_count)
if __name__ == '__main__':
    main()
```