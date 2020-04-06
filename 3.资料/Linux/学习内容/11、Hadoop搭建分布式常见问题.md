# Hadoop分布式的搭建
## 1. 搭建前提
1. 多台计算机
2. 计算机需要安装Java
3. 网络防火墙关闭
4. 计算机之间可以连通

### 1.1 多台计算机的准备
> 如果要准备多台真的虚拟机，成本太高，我们在此使用虚拟机

> 但是安装多台虚拟机速度太慢，所以我们选择克隆

> 如何克隆?

### 1.2 克隆步骤

1. 装好一台计算机
2. 修改配置文件
    1. `/etc/sysconfig/network-scripts/ifcfg-eth0`
        1. 删除**HWADDR**
        2. 删除**UUID**
    2. 修改主机名
        `/etc/sysconfig/network`

3. 关机
4. 在虚拟里创建快照
5. 在虚拟机里克隆
6. 开启克隆出来的机器
7. 修改计算机名
8. 删除文件
    1. `rm -rf /etc/udev/rules.d/70-persistent-net.rules`
9. 重启


### 2. 伪分布式搭建

1. 下载hadoop安装包
2. 安装hadoop
    1. 在我们这是解压`tar -xf hadoop版本号`
3. 配置hadoop的安装路径
    1.PATH=$PATH:$hadoop/bin:$hadoop/sbin
4. 配置hadoop 配置Java的路径
文件路径在`/hadoop-2.5.6/etc/hadoop/` (因为远程调用时，不会读取本机profile文件)
    1. hadoop-env.sh
    2. mapred-evn.sh
    3. yarn-env.sh
5. 配置hadoop 配置关于分布式的内容
    1. core-site.xml

            <!--配置namenode在哪-->
            <property>
                <name>fs.defaultFS</name>
                <value>hdfs://node01:9000</value>
            </property>
            <!--配置hadoop存放数据的临时目录-->
            <property>
                <name>hadoop.tmp.dir</name>
                <value>/var/abc/</value>
            </property>
    2. hdfs-site.xml
        
          <!--设置副本数，不在超过节点数-->
            <property>
                <name>dfs.replication</name>
                <value>1</value>
            </property>
            <!--设置secondaryNode在哪个节点-->
            <property>
                <name>dfs.namenode.secondary.http-address</name>
                <value>node01:50090</value>
            </property>
6. 修改slaves文件，设置哪个为datenode节点
7. 格式化文件系统
    1. `hdfs namenode -format`
8. 启动hdfs系统
    1. `start-dfs.sh`
9. 查看进程
    1.`jps`
    
10. 在网页验证
    1. http://ip:50070
11. 基本操作
    1. 创建目录
        `hdfs dfs -mkdir -p /user/root`
    2. 上传文件
        `hdfs dfs -put 文件名 路径`
    

### 3 真分布式搭建
1. 创建免密钥

        ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa
        cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys
        #把node01的公钥 发送给其它节点
        scp ~/.ssh/id_dsa.pub node2:~/.ssh/node01.pub
        scp ~/.ssh/id_dsa.pub node3:~/.ssh/node01.pub
        scp ~/.ssh/id_dsa.pub node4:~/.ssh/node01.pub
        # 2，3，4节点将公钥追加到authorized_keys 在3台计算机依次执行
        cat /.ssh/node01.pub >>~/.ssh/authorized_keys

2. 修改配置文件
     1. core-site.xml
    
                <!--配置namenode在哪-->
                <property>
                    <name>fs.defaultFS</name>
                    <value>hdfs://node01:9000</value>
                </property>
                <!--配置hadoop存放数据的临时目录-->
                <property>
                    <name>hadoop.tmp.dir</name>
                    <value>/var/abc/</value>
                </property>
    2. hdfs-site.xml
            
              <!--设置副本数，不在超过节点数-->
                <property>
                    <name>dfs.replication</name>
                    <value>1</value>
                </property>
                <!--设置secondaryNode在哪个节点-->
                <property>
                    <name>dfs.namenode.secondary.http-address</name>
                    <value>node02:50090</value>
                </property>
3. 讲配置好的hadoop文件发给别的计算机
        
        scp -r hadoop node02:`pwd`
        scp -r hadoop node03:`pwd`
        scp -r hadoop node04:`pwd`
4. 格式化文件系统
    1. `hdfs namenode -format`
5. 启动hdfs系统
    1. `start-dfs.sh`
6. 查看进程
    1.`jps`
    
7. 在网页验证
    1. http://ip:50070
8. 基本操作
    1. 创建目录
        `hdfs dfs -mkdir -p /user/root`
    2. 上传文件
        `hdfs dfs -put 文件名 路径`


### 4. 分布式问题
> WARN hdfs.DFSUtil: Namenode for null remains unresolved for ID null.  Check your hdfs-site.xml file to ensure namenodes are configured properly.

**解决方案**：查看core-site.xml里面的fs.defaultFS的值是否正确

> 每次链接都提示是否确认？
Are you sure you want to continue connecting (yes/no)

**解决方案**:
修改/etc/ssh/ssh_config

将其中的# StrictHostKeyChecking ask 改成 StrictHostKeyChecking no`