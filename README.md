# django-authority
Django权限管理系统插件


### 可以移值到任何django的项目上，用来管理用户对任何模型的增删改查

1、authority/middleware/authentication.py 中定义 url白名单，未登录跳转链接url

2、actions 包括 views, edit, delete, change, add 

3、在模板 html 中判断 是否有模型的 action 如：

    {% if 'add' in request.actions %}
    <a href="#"> 增加用户 </a>
    {% endif %}
