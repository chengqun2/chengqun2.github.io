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

### 带时间展示历史命令
`HISTTIMEFORMAT='%F %T ' history | tail -10`

### 查看某文件夹大小
`sudo du -hc --max-depth=0 /yd21`

### Clear Cache
`sudo sh -c 'echo 3 > /proc/sys/vm/drop_caches'`

### Find the application folder by specific port
`lsof -i:8080` to show the PID of the port 8080
`readlink -f /proc/PID/cwd`

### Show the version of nginx 
`/usr/local/nginx/sbin/nginx -v`

### mount a new disk
1. `lsblk `
2. `sudo mkfs /dev/sdd`
3. `sudo mkdir /data01`
4. `sudo mount /dev/sdd /data01`
5. `df -h`
6. `vim /etc/fstab`   
   Add to /etc/fstab to ensure the disk mounts automatically after a reboot:
   `UUID=1111-2222-3333-4444  /data01  ext4  defaults  0  0`

### Enable the firewall and allow necessary ports
sudo firewall-cmd --state
sudo systemctl start firewalld
sudo systemctl enable firewalld
sudo firewall-cmd --zone=public --add-port=22/tcp --permanent
sudo firewall-cmd --zone=public --add-port=80/tcp --permanent
sudo firewall-cmd --zone=public --add-port=443/tcp --permanent
sudo firewall-cmd --reload
sudo firewall-cmd --list-all

### x86_64，则表示服务器是x86架构。 如果输出结果是aarch64，则表示服务器是ARM架构
`uname -m`

### Show version of the Linux 
`cat /etc/os-release`

### 
`rsync -a -H /var/lib/clickhouse/ /mnt/sdc/clickhouse`

### 设置Linux服务器时间：
`date -s "2007-08-03 14:15:00"`

### SSD（Solid State Drive，固态硬盘）和HDD（Hard Disk Drive，机械硬盘
`lsblk -d -o name,rota`
sda     0  # This is likely an SSD because rota = 0
sdb     1  # This is likely an HDD because rota = 1
