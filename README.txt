# rentingsong
1、将文件夹apps标记为source root
2、创建app命令： python manage.py startapp appname
3、setting设置，将apps, templates添加到setting.py文件中。
4、django urls管理，访问的时候，网址应该为：127.0.0.1：8000/<global_url_namespace_name>/<app_url_name>