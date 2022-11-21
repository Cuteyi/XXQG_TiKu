# workers = 5  # 定义同时开启的处理请求的进程数量，根据网站流量适当调整
worker_class = "gevent"  # 采用gevent库，支持异步处理请求，提高吞吐量。基于协程实现的“伪线程”，共享内存
# worker-connections = 1000
bind = "0.0.0.0:1880"