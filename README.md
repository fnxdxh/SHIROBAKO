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

# SHIROBAKO
“白箱”大学生竞赛平台项目
# 函数说明

## competitor_register(request) 参赛者注册
  return JsonResponse
  若成功：Json={'msg':‘success’,'error_num':0}
  不成功 Json={'msg':‘failed’,'error_num':1}
  
## jury_register(request)   评委注册
  return JsonResponse
  若成功：Json={'msg':‘success’,'error_num':0}
  不成功 Json={'msg':‘failed’,'error_num':1}
  
## organizer_register(request)   组织方注册
  return JsonResponse
  若成功：Json={'msg':‘success’,'error_num':0}
  不成功 Json={'msg':‘failed’,'error_num':1}
  
## competitor_login(request) 参赛者登录
  return JsonResponse
  若成功：Json={'msg':‘success’,'error_num':0}
  不成功 Json={'msg':‘failed’,'error_num':1}
  
## jury_login(request)   评委登录
  return JsonResponse
  若成功：Json={'msg':‘success’,'error_num':0}
  不成功 Json={'msg':‘failed’,'error_num':1}
  
## organizer_login(request)   组织方登录
  return JsonResponse
  若成功：Json={'msg':‘success’,'error_num':0}
  不成功 Json={'msg':‘failed’,'error_num':1}
  
## admin_login(request) 管理员登录
   return JsonResponse
  若成功：Json={'msg':‘success’,'error_num':0}
  不成功 Json={'msg':‘failed’,'error_num':1}
  
## index_competition_list(request) 首页比赛列表
  return JsonResponse
  成功返回一个列表[{'title':,
                   'organizer':,
                   'type':,
                   'start_time':,
                   'end_time':
                   },{},{}]
  不成功同上
## competitor_competition_list(request) 参赛者比赛列表
   同上
## jury_competiton_list(request) 评委比赛列表
    同上
    
## organizer_competition_list(request) 组织方比赛列表
  同上
  
## competitor_sign_up(request) 参赛者报名比赛
  return JsonResponse
  若成功：Json={'msg':‘success’,'error_num':0}
  不成功 Json={'msg':‘failed’,'error_num':1}
  
## file_upload(request) 上传文件
  return JsonResponse
  若成功：Json={'msg':‘success’,'error_num':0}
  不成功 Json={'msg':‘failed’,'error_num':1}
  
## file_download(request) 下载文件
   成功  返回StreamingHttpResponse
   不成功 返回httpresponse
   
## grade_upload(request) 上传分数
     return JsonResponse
  若成功：Json={'msg':‘success’,'error_num':0}
  不成功 Json={'msg':‘failed’,'error_num':1}
  
## file_list(request) 文件列表
  return JsonResponse
  json=[{‘name’:,
         'msg':success,
         'error_num':0},{},{}]
  失败  Json={'msg':‘failed’,'error_num':1}
  
## competition_detail(request) 比赛详情
  同上
 
## create_competition(request) 创建比赛
return JsonResponse
  若成功：Json={'msg':‘success’,'error_num':0}
  不成功 Json={'msg':‘failed’,'error_num':1}
  
## invite_jury(request)邀请评委
同上

## my_logout(request) 登出
同上

## search_competition(request) 搜索
同比赛列表

## competition_detail(request) 比赛详情
return JsonResponse
json = {'title':,
        'stage':,
        'organizer':,
        'description':,
        'msg':'success'
        'error_num':}
 失败同上
