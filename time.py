from threading import Timer
import sys

def scheduled_task(arg):
       print("\ntask complete arg %s!\n"%(arg))

def run_scheduled_task(arg):
       timer = Timer(3, scheduled_task, [arg])
       timer.start()

