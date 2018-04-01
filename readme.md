##sqlite3 命令行
    sqlite3工具 下载client的win版本解压，目录加到path路径配置路径
    cmd -》 sqlite3 db.sqlite3 -》 愉快的写sql
    或者直接用可视化工具，打开路径里面的db.sqlite3 文件即可
##虚拟环境搭建virtualenv： help: python -V     import django;print(django.get_version())
    安装工具
    pip install virtualenv
    新建环境
    virtualenv --no-site-package --python= c:\python27\python.exe venv(安装python2.7的名称，建议名称为绝对路径c:/venvs/py2.7
    启动
    c:\Users\zhaoyun\venv\Scripts\activate.bat
    停止虚拟环境
    deactivate
###virtualenvwrapper 使用,加强的工具，依赖于virtualenv，比上面一个更好用，智能提示，方便管理
    安装工具
    pip install virtualenvwrapper-win
    
    新建环境（2.7并没有在环境变量里面，默认的环境变量是3.6），默认创建的虚拟环境位于C:\Users\username\envs,
    所有的环境都在这个下面（django2.7，mysite3.6）可以通过环境变量 WORKON_HOME 来定制。
    通过计算机-->属性-->高级系统设置-->环境变量-->在系统变量中新建“变量名”：WORKON_HOME,变量值：“你自定义的路径”。
    mkvirtualenv django --no-site-package --python=C:\Python27\python.exe             
    注意：安装好后会自动进入虚拟环境  python -V 查看当前的版本
    
    以名字激活启动虚拟环境2.7版本  ，还有一个venvs3.6版本
    workon django                  workon venvs
    
    查看由所有的
    lsvirtualenv.bat   
    
    停止虚拟环境
    deactivate
    
    删除虚拟环境
    rmvitualenv django

##新建项目：
    django-admin startproject mysite
##启动django命令（需要目录在项目的根目录）：  attention：使用pycharm自己带的虚拟环境插件，
##和virtualenv，virtualenvwrapper不一样，不能够使用lsvirtualenv查看到pycharm自带的虚拟环境
    python manage.py runserver    [127.0.0.1:8000]  
##新建app：
    python manage.py startapp polls 
##进入django调试页面
    python manage.py  shell
    和ipython不同的是，上面的导入了当前环境（model类等）的对象
## 同步到缓存：django为了能跟踪表结构的变化，增加了migrations版本控制功能，如果没有该功能每次表结构变化，就需要重新⽣生成表结构，重新导入数据
    python manage.py makemigrations
##同步到数据库：
    python manage.py  migrate 
##项目的入口是urls配置文件,定位到view后，处理返回一个封装好的html


