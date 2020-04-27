# `notebookOnWeb`
你的网上笔记本
----------------
通过flask和SQLite3把您所输入的笔记存储在网上仓库内
网址`/`是根目录，如果访问这里，将会自动重定向到`/home`。
`/login`是登陆网址。
`/logon`是注册网址。
`/shownotes/<topic>`是显示笔记的网址。
在`/home`会显示所有的笔记主题，点击主题就会进入`/shownotes/<topic>`。

目录结构
----------------------------------------------------------------
该程序默认运行在回送地址的5000端口（不关我事，是flask定的），也就是一般的`127.0.0.1:5000`，启动文件是`runserver.py`，负责页面的文件在`notebookonweb/views.py`，静态文件在`notebookonweb/static`，HTML文件在`notebookonweb/templates`。

谢谢
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
`E.O.F`
