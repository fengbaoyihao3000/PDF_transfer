import threading


def process_run(thread_num, function, arg):
    """
    用于开启多线程
    :param thread_num: 并发的线程数
    :param function: 并发执行的函数
    :param arg: 需要传入的参数
    :return:
    """
    thread_pool = []
    for i in range(thread_num):
        p = threading.Thread(target=function, args=arg[i])
        thread_pool.append(p)
        p.start()
    for p in thread_pool:
        p.join()
