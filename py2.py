from multiprocessing import Process
import sys
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime
import requests

url = "http://192.168.2.105:8090/oscarapi/basket/Paid-Vas-Bill/"
headers = {'content-type': 'application/json',
           'Token': 'd5a9f06116cd2af2a0280b36c2ca68e4db38adf6'}
body = ""


def func1():
    print('start func1', datetime.fromtimestamp(time()))
    api()
    print('end func1', datetime.fromtimestamp(time()))


def func2():
    print('start func2', datetime.fromtimestamp(time()))
    api()
    print('end func2', datetime.fromtimestamp(time()))


def api():
    response = requests.post(url, data=body, headers=headers)
    print("response:----->>>>", response.content)


if __name__ == '__main__':
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()


