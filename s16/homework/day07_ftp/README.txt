

1.cnblogs
    a.http://www.cnblogs.com/weibiao/p/6505789.html
    b.http://www.cnblogs.com/weibiao/p/6526717.html
2.ftp
    a.完成linux cmd,get,put,粘包,断点续传.
    b.其中只有get支持续传.
    c.ftp_server and client开始没有想好,是共享公共代码,还是分开.
    d.未完成,认证,进度条,切换目录.
    e.我每次写完程序都会感觉结构规化的不好,就想重写,我是先写程序后画流程图的原因?
    f.为什么即使我们用类,写着写着就成面向过程的了?

day07_ftp/
├── README.txt
├── __init__.py
├── bin
│   ├── __init__.py
│   ├── ftp_client.py   # FTP客户端.
│   ├── ftp_server.py   # FTP服务器.
│   ├── m.py            # 断点续传测试文件.
│   └── test_clent.py   # 测试用的,忽略.
├── conf
│   ├── __init__.py
│   └── settings.py     # 配置文件,C/S共用.
└── lib
    ├── __init__.py
    └── active.py       # 服务端的md5,put,get函数.