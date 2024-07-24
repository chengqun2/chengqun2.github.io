### My node learning record
F:\nodejs_workspace\node-connect-linux
F:\nodejs_workspace\node-express-mongoose-demo

### postman test post api
in the header: 
add key, value
Content-type   application/json

### run application as daemon
`nohup node app.js > app.log 2>&1 &`
#### use exit to quit, do not close the shell window directly
`exit`

### Unit Test
npm install --save-dev mocha 
npm install --save-dev chai

### electron 下载失败解决方案
在项目目录新建.npmrc文件，内容如下：
registry=https://registry.npmmirror.com/
electron_mirror=https://npmmirror.com/mirrors/electron/
然后 npm install electron 即可