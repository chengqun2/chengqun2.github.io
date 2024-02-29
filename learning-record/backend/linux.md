### 1. kill a pid through a running jar name:
  ps -ef | grep app-name | grep -v grep | awk '{print $2}' | xagrs kill -9;

### es修改elasticsearch.xml后新文件夹赋权：
chown -R elasticsearch:elasticsearch /path/to/new_data_directory
