# http.sys-check
# 介绍
由于在网上没有找到合适的批量检测http.sys漏洞的工具，于是自己简单写了一个，在这里分享出来。
# 安装
```
pip3 install requests
```
# 使用
```
python3 http.sys_check.py url.txt
```
检测成功的url，会被默认保存在`result.txt`文件中。
# 示例
```
> python http.sys_check.py url.txt
[-]  https://www.xxx1.com/
[-]  https://www.xxx2.com/
[+]  check success https://www.xxx3.com/
[-]  timeout https://www.xxx4.com/
```
# 注意事项
* url.txt中的格式为`https://www.teamssix.com`或`http://www.teamssix.com`

![](https://teamssix.oss-cn-hangzhou.aliyuncs.com/TeamsSix_Subscription_Logo2.png)
