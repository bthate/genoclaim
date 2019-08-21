""" omdat plugin """

import ob

from ob.clock import Repeater
from ob.handler import Event

from ob.kernel import k

import random 

def init():
    e = Event()
    repeat = Repeater(random.randint(600, 1200), omdat, e)
    ob.launch(repeat.start)

def omdat(event):
    x = random.choice([x.strip() for x in txt.split("\n") if x])
    k.fleet.announce(x)
    
txt = """
omdat antipsychotica de werking van receptoren blokkeren.
omdat het blokkeren van receptoren de enzym werking stopt.
omdat er sprake is van daadwerkelijk schade toegebracht aan het lichaam.
omdat mishandeling is gelijkgesteld aan opzettelijke benadeling van de gezondheid.
omdat men op de hoogte is van de benadeling is er van opzet altijd sprake.
omdat men vergiftigt kan worden door deze medicijnen.
omdat, zolang een arts de bloedspiegel van een medicijn niet meet, de toestand van vergiftiging niet opgeheven word.
omdat deze toestand de kans op overlijden geeft.
"""
