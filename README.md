# keyboard-config
## 通过改变内核反馈到软件层的返回值来达到改键的目的
  使用方案：[xkeysnail](https://github.com/mooz/xkeysnail)
  设定config，让xkeysnail翻译后再执行

## 如何实现arch linux上使其开机自启动，切无需手动输入管理员密码
   xkeysnail的启动需要sudo获取临时权限。
### 解决方案
   设定一个守护进程，并且让其开机自启动。
   
   cd 到制定的目录下创建一个service。
   再执行systemctl enable * 相关的命令设定这个服务开机自启动。
   
