1. Vuex存值：
    存值：
    1)、state: {
        real_name: "",
    },
    2)、mutations: {
        SET_REAL_NAME: (state, realName) => {
            state.realName = realName;
        },
    },		
    取值：vue文件中引入：
    1).import { mapState } from "vuex";
    2).computed: {
        ...mapState({
            name: (state) => state.user.name,
            userId: (state) => state.user.userId,
        }),
    },
    3).console.log(this.name, this.userId, ".......");
2. vue添加自定义图标：
    1).src下assets增加图片 ico_alert.png
    2).vue中import ico_alert from "@/assets/icons/ico_alert.png";
    3).data中添加 ico_alert,
    4).<img :src="ico_alert" />
3. vue3配置代理(解决跨域)：
    1).nginx配置：
    location /api {
        proxy_pass http://221.231.109.86:9091/forward/ddm;
        proxy_set_header   X-Forwarded-Proto $scheme;
        proxy_set_header   Host              $http_host;
        proxy_set_header   X-Real-IP         $remote_addr;
        proxy_set_header   X-Forwarded-For   $proxy_add_x_forwarded_for;
    }
    2).vue.config.js配置：
    module.exports = defineConfig({
        publicPath: "./",
        transpileDependencies: true,
        // devServer 本地开发，不走nginx时使用的接口请求
        devServer: {
            host: "0.0.0.0",
            open: true,
            proxy: {
                '/api':{
                    target: 'http://221.231.109.86:9091/forward/ddm',//跨域请求的公共地址
                    ws:false, //也可以忽略不写，不写不会影响跨域'
                    changeOrigin:true, //是否开启跨域，值为 true 就是开启， false 不开启
                    pathRewrite:{
                        '^/api':''//注册全局路径， 但是在你请求的时候前面需要加上 /api
                    }
                },
            },
        },
    })
    3).请求示例：
    axios({
        method:"get",
        url:"/api/duty/getDutyList.do"
    }).then(res => {
        this.todayList = res.data.todayList;
        this.tomorrowList = res.data.tomorrowList;
    })    
4. Vue父子组件通过prop传值：
    父Vue：
        <hellochange :msgchange="hello"></hellochange>
    子Vue：
        props: ["msgchange"]    
5. setup(){
       const name = ref('Bob')
       const age = ref(30)
       return {
           name,
           age
       }
   }
6. ### Vue3 ref
   When you use ref in Vue 3, it returns a reactive object. This object contains a single property, value, which holds the actual value you passed to ref. Vue automatically tracks changes to this value property and updates the DOM accordingly.   

### vite.config.mts、vite.config.js 和 vite.config.ts 都是用于配置 Vite 构建工具的文件, 解决@开头的文件（图片等）引用路径
```
// vite.config.js
import { defineConfig } from 'vite';
import path from 'path';

export default defineConfig({
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
});
```