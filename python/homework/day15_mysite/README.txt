
1.cnblogs
	http://www.cnblogs.com/weibiao/p/6831978.html
2.项目:day15_mysite
	完成功能:
		- 用户名:alex 密码:123
		- 完成数据库的增、删、改、查
		- *使用cookie完成登陆
		- 使用模态对话框
		- *使用装饰器
		- *使用模板语言和继承
		- *Form表表单
		- 表结构没有使用日期格式,不然得转换
		- update效率不高,全部修改
		- 鼠标焦点换色
		- urls分发(include)
		- 显示登录用户名字
		- *增加分页和总计条目

├── blog
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── day15_mysite
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── static
│   ├── bootstrap-3.3.7-dist
│   │   ├── css
│   │   │   ├── bootstrap-theme.css
│   │   │   ├── bootstrap-theme.css.map
│   │   │   ├── bootstrap-theme.min.css
│   │   │   ├── bootstrap-theme.min.css.map
│   │   │   ├── bootstrap.css
│   │   │   ├── bootstrap.css.map
│   │   │   ├── bootstrap.min.css
│   │   │   └── bootstrap.min.css.map
│   │   ├── fonts
│   │   │   ├── glyphicons-halflings-regular.eot
│   │   │   ├── glyphicons-halflings-regular.svg
│   │   │   ├── glyphicons-halflings-regular.ttf
│   │   │   ├── glyphicons-halflings-regular.woff
│   │   │   └── glyphicons-halflings-regular.woff2
│   │   └── js
│   │       ├── bootstrap.js
│   │       ├── bootstrap.min.js
│   │       └── npm.js
│   ├── css
│   │   └── common.css					# CSS全部配置
│   ├── jquery-1.12.4.js				# JS解析器
│   └── js
│       ├── cancel_login.js				# 模态对话框取消掉
│       ├── change_color.js				# 表格行获取焦点变色
│       └── edit.js						# 修改数据模态对话框
└── templates
    ├── add_books.html					# 增加图书页面
    ├── base.html						# BASE模板
    ├── index.html						# 数据页面
    ├── login.html						# 登录页面
    └── logout.html						# 登录页面

14 directories, 55 files
