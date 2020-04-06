### Python-Spider作业
#### day01
- 了解爬虫的主要用途
- 了解反爬虫的基本手段
- 理解爬虫的开发思路
- 熟悉使用Chrome的开发者工具
- 使用urllib库获取《糗事百科》前3页数据
- 使用urllib库登录《速学堂》官网
- 爬取
    - https://knewone.com/
    - 58同城二手信息
    

#### day02
- 获取豆瓣电影分类排行榜 -前100条数据
- 数据opener的用法
    - opener的构建
    - 代理的使
    - cookie的使用
- 了解cookie的作用
- 使用cookie登录虾米音乐
- 使用requests 库获取数据《纵横网小说排行》前3页数据
- 使用requests 登录速学堂
- 
#### day03
- 熟练使用re，了解基本语法的使用
- 熟练使用xpath，了解基本语法的使用
- 掌握BeautifulSoup，掌握css的用法
- 爬一部小说 [盗墓笔记](http://www.jueshitangmen.info/daomubiji)，要求保存成文件
- 爬取小猪短租信息

#### day04
- 熟练使用selenium爬取方式
- 爬取拉钩职位
- 80s网站的抓取
#### day05
- 熟悉scrapy的基本使用（创建与运行，目录结构）
- 爬取当当网python图书信息
- 爬取17173游戏排行信息

#### day06
- 掌握3种调试方式
    - debug
    - scrapy shell
    - test Restful 插件
- 掌握crawlspider的使用
- 掌握动态UA与PROXY的使用

#### dya07
- 掌握3种登录的思路
- 掌握MOngo的基本使用
- 完成练习题
    ```
    创建年级，并随机添加 10 名学生；
    
           for (var i = 1; i <= 10; i++) {
               db.grade.insert({
                   "name": "zhangsan" + i,
                   "sex": Math.round(Math.random() * 10) % 2,
                   "age": Math.round(Math.random() * 6) + 3,
                   "hobby": []
               });
           }
    ```
    - 查看grade班级中的所有学生
    
    - 查看grade班级中所有年龄是 4 岁的学生
    
    - 查看grade班级中所有年龄大于 4 岁的学生
    
    - 查看grade班级中所有年龄大于 4 岁并且小于 7 岁的学生
    
    - 查看grade班级中所有年龄大于 4 岁并且性别值为0的学生
    
    - 查看grade班级中所有年龄小于 4 或者大于 7 岁的学生
    
    - 查看grade班级中所有年龄是 4 岁或 6 岁的学生
    
    - 查看grade班级中所有姓名带zhangsan1的学生
    
    - 查看grade班级中所有姓名带zhangsan1和zhangsan2的学生
    
    - 查看grade班级中所有兴趣爱好有三项的学生
    
    - 查看grade班级中所有兴趣爱好包括画画的学生
    
    - 查看grade班级中所有兴趣爱好既包括画画又包括跳舞的学生
    
    - 查看grade班级中所有兴趣爱好有三项的学生的学生数目
    
    - 查看grade班级的第二位学生
    
    - 查看grade班级的学生，按年纪升序
    
    - 查看grade班级的学生，按年纪降序

#### day08
- 熟悉搭建splash的环境
- 使用requests库结合splash爬虫当当网
- 使用scrapy结合splash爬取瓜子二手车信息

#### day09
- 熟练使用scrapy-redis插件
- 使用scrapy-redis爬取51job求职信息