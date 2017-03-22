##  基于Multiprocessing模块的Python 多进程任务框架

#### 通过mulprocessing模块的Queue队列进行数据传递
#### 基于python装饰器路由,通过@mul.addFunc('sub')为work进程添加执行函数(消费者) @mul.addFunc('main')为主进程添加执行函数(生产者)

* pil.py 主进程会遍历目录图片，将文件名通过Queue传递给work进程进行操作如裁剪
* curl.py 主进程会抓取图片url（已知乎为例)，work进程会下载图片
