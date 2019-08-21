""" zorg plugin """

import ob

from ob.clock import Repeater
from ob.handler import Event

from ob.kernel import k

import random 

def init():
    e = Event()
    repeat = Repeater(random.randint(600, 1200), zorg, e)
    ob.launch(repeat.start)

def zorg(event):
    x = random.choice([x.strip() for x in txt.split("\n") if x])
    k.fleet.announce(x)

txt = """
a. een interventie, bestaande uit een vorm van verzorging, bejegening, behandeling, begeleiding of bescherming;
b. toediening van medicatie, vocht en voeding, regelmatige medische controle of andere medische handelingen;
c. pedagogische of therapeutische maatregelen;
d. opname in een accommodatie;
e. beperking van de bewegingsvrijheid;
f. afzondering of separatie in een daartoe geschikte verblijfsruimte;
g. beperking van het recht op het ontvangen van bezoek of het gebruik van communicatiemiddelen;
h. toezicht op betrokkene;
i. onderzoek aan kleding of lichaam;
j. controle op de aanwezigheid van gedrag beïnvloedende middelen;
k. beperkingen in de vrijheid het eigen leven in te richten, die tot gevolg hebben dat betrokkene iets moet doen of nalaten.
"""
