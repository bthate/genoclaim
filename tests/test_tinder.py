# OLIB - object library
#
#

import ol
import os
import random
import sys
import time
import unittest

param = ol.Object()
param.add = ["test@shell", "bart"]
param.dne = ["test4", ""]
param.edt = ["omod.rss.Cfg", "omod.rss.Cfg server=localhost", "omod.rss.Cfg channel=#dunkbots"]
param.rm = ["reddit", ]
param.dpl = ["reddit title,summary,link",]
param.log = ["test1", ""]
param.flt = ["0", "1", ""]
param.fnd = ["log test2", "todo test3", "rss reddit"]
param.rss = ["https://www.reddit.com/r/python/.rss", ""]
param.tdo = ["test4", ""]

events = []
ignore = ["ps", "rm"]
nrtimes = 1

k = ol.krn.get_kernel()

class Event(ol.hdl.Event):

    def reply(self, txt):
        if "v" in k.cfg.opts:
            print(txt)

class Test_Tinder(unittest.TestCase):

    def test_all(self):
        for x in range(k.cfg.index or 1):
            tests(k)

    def test_thrs(self):
        thrs = []
        for x in range(k.cfg.index or 1):
            ol.tsk.launch(tests, k)
        consume(events)
        
def consume(elems):
    fixed = []
    res = []
    for e in elems:
        r = e.wait()
        res.append(r)
        fixed.append(e)
    for f in fixed:
        try:
            elems.remove(f)
        except ValueError:
            continue
    k.stop()
    return res
    
def tests(b):
    keys = list(k.cmds)
    random.shuffle(keys)
    for cmd in keys:
        if cmd in ignore:
            continue
        events.extend(do_cmd(cmd))

def do_cmd(cmd):
    exs = ol.get(param, cmd, [""])
    e = list(exs)
    random.shuffle(e)
    events = []
    nr = 0
    for ex in e:
        nr += 1
        txt = cmd + " " + ex 
        if "-v" in sys.argv:
            print(txt)
        e = Event()
        e.txt = txt
        k.queue.put(e)
        events.append(e)
    return events
