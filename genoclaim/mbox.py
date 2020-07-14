# GENOCLAIM - https://genoclaim.rtfd.io - OTP-CR-117/9/001 - otp.informationdesk@icc-cpi.int
#
# genoclaim email related commands.

import mailbox, os, random, time

from bot.obj import fntime
from bot.spc import Db, Dict, Object, k
from bot.tms import elapsed

bdmonths = ['Bo', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
            'Sep', 'Oct', 'Nov', 'Dec']
monthint = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
}

class Email(Dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = ""

def to_date(date):
    date = date.replace("_", ":")
    res = date.split()
    ddd = ""
    try:
        if "+" in res[3]:
            raise ValueError
        if "-" in res[3]:
            raise ValueError
        int(res[3])
        ddd = "{:4}-{:#02}-{:#02} {:6}".format(res[3], monthint[res[2]], int(res[1]), res[4])
    except (IndexError, KeyError, ValueError):
        try:
            if "+" in res[4]:
                raise ValueError
            if "-" in res[4]:
                raise ValueError
            int(res[4])
            ddd = "{:4}-{:#02}-{:02} {:6}".format(res[4], monthint[res[1]], int(res[2]), res[3])
        except (IndexError, KeyError, ValueError):
            try:
                ddd = "{:4}-{:#02}-{:02} {:6}".format(res[2], monthint[res[1]], int(res[0]), res[3])
            except (IndexError, KeyError):
                try:
                    ddd = "{:4}-{:#02}-{:02}".format(res[2], monthint[res[1]], int(res[0]))
                except (IndexError, KeyError):
                    try:
                        ddd = "{:4}-{:#02}".format(res[2], monthint[res[1]])
                    except (IndexError, KeyError):
                        try:
                            ddd = "{:4}".format(res[2])
                        except (IndexError, KeyError):
                            ddd = ""
    return ddd

def cor(event):
    if not event.args:
        event.reply("cor <email>")
        return
    s = Dict()
    s["From"]= event.args[0]
    nr = -1
    db = Db()
    args = ["From",] + event.rest.split()
    for email in db.all("genoclaim.mbox.Email", s):
        nr += 1
        if event.index and nr != event.index:
            continue
        event.reply("%s %s %s" % (nr, email.format(args, True), elapsed(time.time() - fntime(email.__stamp__))))

def email(event):
    if not event.args:
        event.reply("email <match>")
        return
    event.parse()
    match = event.args[0]
    try:
        match, *args = event.args
    except ValueError:
        match = event.args[0]
        args = []
    nr = -1
    db = Db()
    for o in db.find_value("genoclaim.mbox.Email", match):
        nr += 1
        if nr != event.index:
            continue            
        event.reply("%s %s" % (str(nr), o.format(event.args, True)))

def mbox(event):
    if not event.args:
        event.reply("mbox <path>")
        return
    fn = os.path.expanduser(event.args[0])
    event.reply("reading from %s" % fn)
    nr = 0
    if os.path.isdir(fn):
        thing = mailbox.Maildir(fn, create=False)
    elif os.path.isfile(fn):
        thing = mailbox.mbox(fn, create=False)
    else:
        event.reply("need a mbox or maildir.")
        return
    try:
        thing.lock()
    except FileNotFoundError:
        pass
    for m in thing:
        o = Email()
        o.update(m)
        try:
            sdate = os.sep.join(to_date(o.Date).split())
        except AttributeError:
            sdate = None
        o.text = ""
        for payload in m.walk():
            if payload.get_content_type() == 'text/plain':
                o.text += payload.get_payload()
        o.text = o.text.replace("\\n", "\n")
        o.save(stime=sdate)
        nr += 1
    if nr:
        event.reply("ok %s" % nr)
