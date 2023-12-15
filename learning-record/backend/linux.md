### 1. kill a pid through a running jar name:
  ps -ef | grep app-name | grep -v grep | awk '{print $2}' | xagrs kill -9;