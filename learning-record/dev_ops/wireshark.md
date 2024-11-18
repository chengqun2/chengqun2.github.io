### Wireshark 网络封包分析软件
#### 过滤http端口为5000的请求
`http && tcp.port == 5000`

#### api contains "getUser"
`http && tcp.port == 5000 && http.request.uri contains "getUser"`

#### catch errors
`http && tcp.port == 5000 && http.request.uri contains "getUser" && http.response.code >= 400`