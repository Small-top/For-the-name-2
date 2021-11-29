from tkinter import * # 图形界面
from tkinter import messagebox # 对话框
from traceback import format_exc #用于精准的获取错误异常
import threading # 多线程
from sys import exit
'''t = threading.Thread(target=new, args=(events.x, events.y))
    # 将子线程设置为守护线程，一旦父线程被结束了，子线程也马上跟着结束。
    t.setDaemon(True) 
    t.start()
'''
# json轻量级的数据交换格式
import json
"""
json.dumps(var): 对数据进行编码。
json.loads(var): 对数据进行解码。
json.dump(data, file): 对文件的数据进行编码。
json.load(file): 对文件的数据进行解码。
JSON   -->   Python
object       dict
array        list
string       str
number(int)  int
number(real) float
true         True
false        False
null         None
"""
def updata(old_verson):
    '''完成更新功能的函数'''
    # global response
    t = threading.Thread(target=show_updata, args=(old_verson, ))
    # 将子线程设置为守护线程，一旦父线程被结束了，子线程也马上跟着结束。
    # t.setDaemon(True) 
    t.start()


if __name__ == "__main__":
    updata([1, 1, 0, 2])
