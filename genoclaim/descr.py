# mods/descr.py
#
#

""" commit descriptions of MEDS. """

import ob

from ob.clock import Repeater
from ob.handler import Event
from ob.fleet import Fleet

from ob.kernel import k

import random

got = []

def init():
    e = Event()
    repeater = Repeater(60, descr, e)
    ob.launch(repeater.start)

def descr(event):
    x = random.choice([x for x in txt.split("\n") if x])
    if x not in got:
        got.append(x)
        k.fleet.announce(x)

txt = """
dat is geen zorg, dat is het plegen van strafbare feiten !!
Mishandeling gepleegd door toediening van voor het leven of de gezondheid schadelijke stoffen !!
de medicijnen brengen schade toe aan het lichaam en daarom is het toedienen ervan mishandeling.
de medicijnen brengen schade toe aan het lichaam en daarmee het slachtoffer in een levensbedreigende situatie. #ggz
Opzettelijke benadeling van de gezondheid, gepleegd met voorbedachten rade, de dood ten gevolge.
Volledig geinformeerd, die medicijnen zijn gif en het toedienen ervan is strafbaar - http://pythonhosted.org/meds/ #ggz
Opzettelijke benadeling van de gezondheid, gepleegd met voorbedachten rade, de dood ten gevolge.
opzettelijke benadeling van de gezondheid, gepleegd met voorbedachten rade, de dood ten gevolge
Behandeling met levensgevaarlijke medicijnen is strafbaar.
Zware mishandeling gepleegd met voorbedachten rade wordt gestraft met gevangenisstraf van ten hoogste twaalf jaren
Met mishandeling wordt gelijkgesteld opzettelijke benadeling van de gezondheid.
Indien het misdrijf wordt gepleegd door toediening van voor het leven of de gezondheid schadelijke stoffen.
indien het misdrijf wordt gepleegd door toediening van voor het leven of de gezondheid schadelijke stoffen.
mishandeling door toediening van voor het leven of de gezondheid schadelijke stoffen
Met mishandeling wordt gelijkgesteld opzettelijke benadeling van de gezondheid.
Artikel 300.4 Met mishandeling wordt gelijkgesteld opzettelijke benadeling van de gezondheid.
hoe medicijnen je gezondheid benadelen
Met MEDS kan je bijhouden hoe medicijnen je gezondheid benadelen.
daadwerkelijk foltering
Toedienen van voor het leven of de gezondheid schadelijke stoffen is strafbaar en moet voor de strafrechter #ggz
De arts meld niet dat de medicijnen gif zijn en de Tweede Kamer maakt wetten om toediening straffeloos te maken.
Antipsychotica zijn gif. Toedienen ervan is mishandeling.
Zorg dragen voor de meest kwetsbare met het leveren van zorg die bestaat uit het plegen van strafbare feiten.
Antipsychotica zijn gif. Het toedienen ervan is mishandeling.
antipsychotica zijn gif
antipsychotica zijn gif.
Antipsychotica zijn gif.
Antipsychotica zijn in hun werking benadeling van de gezondheid. Zekerheidsbewustzijn.
Antipsychotica zijn in hun werking benadeling van de gezondheid.
Mishandeling met medicijnen is strafbaar in het Wetboek van Strafrecht
Uit onderzoek blijkt dat antipsychotica schadelijk zijn voor de gezondheid, ze veroorzaken verlies van hersenweefsel.
De schade die men toebrengt is opzettelijk en daarmee is het mishandeling
Antipsychotica brengen schade toe aan de hersenen in de hoop met die schade de psychotische symptomen te verminderen. De schade die men toebrengt is opzettelijk en daarmee is het mishandeling
Er is geen daadwerkelijk rechtsmiddel voor mishandeling gepleegd door toediening van voor het leven of de gezondheid schadelijk stoffen
Omstandigheden die verplichten tot mishandeling gepleegd door toediening van voor het leven of de gezondheid schadelijke stoffen. #ggz
De BIG-geregistreerde is schuldig aan mishandeling gepleegd door toediening van voor het leven of de gezondheid schadelijke stoffen.
De huisarts is schuldig aan mishandeling gepleegd door toediening van voor het leven of de gezondheid schadelijke stoffen.
Behandeling met medicijnen die de hersenen vergiftigen is langdurige opzettelijke benadeling van de gezondheid tot de dood erop volgt
Men meet het bloed niet.
Met mishandeling wordt gelijkgesteld opzettelijke benadeling van de gezondheid.
MEDS - Artikel 300.4 Met mishandeling wordt gelijkgesteld opzettelijke benadeling van de gezondheid. #ggz
MEDS - Behandeling met medicijnen die de hersenen vergiftigen is langdurige opzettelijke benadeling van de gezondheid tot de dood erop volgt.
3.Verbod van foltering - Niemand mag worden onderworpen aan foltering of aan onmenselijke of vernederende behandeling of bestraffing.
Behandeling met medicijnen die de hersenen vergiftigen is langdurige opzettelijke benadeling van de gezondheid tot de dood erop volgt.
Medicine Effect Registration Program.
"""