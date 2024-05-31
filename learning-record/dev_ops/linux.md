### 1. kill a pid through a running jar name:
`ps -ef | grep app-name | grep -v grep | awk '{print $2}' | xagrs kill -9;`

### es修改elasticsearch.xml后新文件夹赋权：
`chown -R elasticsearch:elasticsearch /path/to/new_data_directory`

### nano(`Ctrl + O`, `Ctrl + X`) 修改Linux服务器名称 
`hostname`
`nano /etc/hostname`
`nano /etc/hosts`
`hostname new_hostname`

### change password of Linux with user root
`passwd`

### nexus install
`tar -zxvf nexus-3.37.1-01-unix.tar.gz `
`cd /usr/local/nexus-3.37.1-01/bin/`
`./nexus run &`

### linux 开启防火墙，并禁用ping
`sudo systemctl status firewalld`
`sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" protocol="icmp" icmp-type="echo-request" reject'`

### 端口占用情况
`sudo netstat -tuln`
`sudo netstat -tuln | grep 8080`
