# SHIROBAKO
“白箱”大学生竞赛平台项目

### 前端结构说明

#### 调试运行说明

```
npm install
npm run dev
```

#### 文件结构说明

/src文件夹包含所有源代码和配置文件，其中index.html为html入口文件，main.js为js入口文件，本项目开发的是单页app，因此不需要其他的html文件，router.js为抽离出来的路由接口文件，所有路由模块均在router.js中定义，vendor.js前期开发过程中用不到，可以忽略。

App.vue为整个app的vue入口文件，可以修改，components文件夹下放置所有的Vue组件，根据不同组件的作用分别新建文件夹进行管理。

整个项目使用element的组件进行开发搭建，依赖关系已经全部解决，可以直接使用。

### 后端结构说明

