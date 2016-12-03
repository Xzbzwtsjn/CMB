import sys
import os
import time
import datetime
import zerorpc
c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")
print c.add(1, 2)
