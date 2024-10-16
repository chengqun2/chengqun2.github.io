### 1. python安装依赖指定镜像源：
    pip --default-timeout=100 install tensorflow==2.0.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
    pip --default-timeout=100 install tensorflow==2.0.0 -i https://pypi.douban.com/simple
### 2. python高版本中escape的使用：
    from flask import escape  改为：
    from markupsafe import escape
### 3. 从浏览器获取cookies、headers、params
    1).f12 从访问url右击copy->copy as cUrl(bash) 得到：
    curl 'https://search.gitee.com/?skin=rec&type=repository&q=flask' \
    -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
    -H 'Accept-Language: zh-CN,zh;q=0.9' \
    -H 'Cache-Control: max-age=0' \
    -H 'Connection: keep-alive' \
    -H 'Cookie: BEC=8ede56c7e7ea181fcd95cf3b7e5ea9fe; Hm_lvt_24f17767262929947cc3631f99bfd274=1700635796; Hm_lpvt_24f17767262929947cc3631f99bfd274=1700635796' \
    -H 'Sec-Fetch-Dest: document' \
    -H 'Sec-Fetch-Mode: navigate' \
    -H 'Sec-Fetch-Site: none' \
    -H 'Sec-Fetch-User: ?1' \
    -H 'Upgrade-Insecure-Requests: 1' \
    -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0' \
    -H 'sec-ch-ua: "Chromium";v="118", "Opera";v="104", "Not=A?Brand";v="99"' \
    -H 'sec-ch-ua-mobile: ?0' \
    -H 'sec-ch-ua-platform: "Windows"' \
    --compressed
    2).https://curlconverter.com/  粘贴cUrl
    cookies = {
    'BEC': '8ede56c7e7ea181fcd95cf3b7e5ea9fe',
    'Hm_lvt_24f17767262929947cc3631f99bfd274': '1700635796',
    'Hm_lpvt_24f17767262929947cc3631f99bfd274': '1700635796',
    }
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'BEC=8ede56c7e7ea181fcd95cf3b7e5ea9fe; Hm_lvt_24f17767262929947cc3631f99bfd274=1700635796; Hm_lpvt_24f17767262929947cc3631f99bfd274=1700635796',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0',
    'sec-ch-ua': '"Chromium";v="118", "Opera";v="104", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    }
    params = {
    'skin': 'rec',
    'type': 'repository',
    'q': 'flask',
    }
    response = requests.get('https://search.gitee.com/', params=params, cookies=cookies, headers=headers)
### 4. python flask 蓝图(Blueprint) 注册路由：
    app.register_blueprint(admin,url_prefix='/admin')

### List, Set, Dictionary, Tuple
A List is an ordered, mutable, and indexed collection that allows duplicate elements.
Lists are defined by square brackets [].
`my_list = [1, 2, 3, 4, 5]`

A Set is an unordered collection of unique elements. It does not allow duplicates.
Sets are defined by curly brackets {}
`my_set = {1, 2, 3, 4, 5}`

A Dictionary is an unordered collection of key-value pairs. Keys are unique, but values can be duplicated.
Dictionaries are defined by curly brackets {}, with key-value pairs separated by colons:
`my_dict = {"name": "John", "age": 30}`        

A Tuple is an ordered, immutable collection that allows duplicates.
Tuples are defined by parentheses ().
`my_tuple = (1, 2, 3, 4, 5)`

### loop an array from index 1
`for price in prices[1:]`
