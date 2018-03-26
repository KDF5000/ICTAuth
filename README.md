### ICTAuth
在没有图形化界面的情况下可以通过命令行方便的认证ICT有线网，比如树莓派的认证，同时应对ICT十二点后会统一强制下线所有的用户，添加了网络监控功能，可以再断网的时候自动进行认证

由于所里网管更新，master分支脚本不能使用，请切换到v2分支使用
----

#### 使用方法
首先下载代码
```
$git clone https://github.com/KDF5000/ICTAuth.git
```
修改`auth.py`里面认证需要的用户名和密码
> pass_str = hashlib.md5("******").hexdigest()
> 
> data = {"username":"******", "password":password,"drop":0, "type":1, "n":100}

然后执行下面命令进行登录和退出
```
$python auth.py login
$python auth.py logout
```
#### 添加网络监控程序
下载的代码中`mornitor_net.sh`是监控网络是否连接比在断网的情况下调用auth.py进行自动认证。为了持续监控需要将此程序加入crontab进行定时执行，可以修改devincron里面的相应路径，然后执行下面指令即可。
```
$crontab devincorn
```
该设置将会每十分钟检查一下网络连接情况，如果发现已经断网则自动认证。
