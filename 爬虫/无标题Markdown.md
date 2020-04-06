1. 装虚拟
2. 创建虚拟机-centos6.5
	1. 网络-自动获取    
	2. 使用xshell连接linux
	    1. xshell安装免费版本
	    2. xftp安装免费版本
	3. 删除网络信息，以方便克隆使用
	    1. cd /etc/dev/network-script
	    2. vi ifcfg-eth0
	    3. 删除UUID，和HDADRESS 使用DD快捷键 esc wq
	    4. 删除 硬件信息文件 /etc/udev/rules.d/70-dsfs-net.rules
	    5. rm -rf 70-dsfs-net.rules
	4. 装Python
	5. 装Twiested
	6. 克隆