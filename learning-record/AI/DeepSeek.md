### deepseek本地部署：
1、安装 ollama(本地下载、管理和运行各类大语言模型的工具)
2、下载deepseek_r1模型（1.5b、7b、8b、14b、32b、70b、671b 按需下载不同参数量的模型）：
ollama pull deepseek-r1:1.5b
3、运行 deepseek_r1模型
ollama run deepseek-r1:1.5b
4、编写代码调用（发送 HTTP 请求来调用模型）

### 代码中直接调用deepseek api
1、在deepseek官网申请API key
2、代码中配置申请好的api key，调用url: https://api.deepseek.com，返回结果