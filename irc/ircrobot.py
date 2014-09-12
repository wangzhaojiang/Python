# coding: utf-8

import socket, urllib2, urllib, sys, re

"""
    handle some IRC operations
"""
class bot:
    def __init__(self, host, port, nick, channel):
        self.nick_ = nick
        self.channel_ = channel
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.irc.connect((host, port))
        print(self.irc.recv(4096))
        self.nick().user().join().privmsg("hello, world")

    def send_cmd(self, s):
        self.irc.send(s + "\r\n")
        return self

    def pong(self, data):
        return self.send_cmd("PONG " + data.split()[1])

    def nick(self):
        return self.send_cmd("NICK %s" % self.nick_)

    def user(self):
        return self.send_cmd("USER %s %s %s: Python IRC" % \
                (self.nick_, self.nick_, self.nick_))

    def join(self):
        return self.send_cmd("JOIN %s" % self.channel_)

    def quit(self):
        return self.privmsg("QAQ~").send_cmd("QUIT")

    def privmsg(self, s, t = ""):
        to = t + ":" if len(t) > 0 else ""
        return self.send_cmd("PRIVMSG %s :%s %s" % (self.channel_, to, s))

    def receive(self):
        while True:
            data = self.irc.recv(4096)
            print(data)
            
            # ignore system info
            if re.findall("^:(.*?).freenode.net", data):
                continue

            if "PING" in data:
                self.pong(data)
            if "KICK" in data and self.nick_ in data:
                self.join()

            info = re.findall("^:(.*?)!.* PRIVMSG (#.*?) :?(.*?)[:,] *(.*?)$", data)
            if not info:
                continue

            if self.nick_ in data and info[0][2] == self.nick_:
                return (info[0][0], info[0][3]) #speaker, content



"""
    talk with xiao.dou
"""
class transit:
    #url = "http://www.xiaojo.com/bot/chata.php"
    url = "http://xiao.douqq.com/bot/chat.php"

    def reply(self, q):
        data = urllib.urlencode([('chat', q)])
        req = urllib2.Request(self.url, data)
        r = urllib2.urlopen(req).read(4096)
        r = r.split("\r\n") # deal with weather info
        r = ''.join(r)
        print(r)
        return r


if __name__ == "__main__":
    ircbot = bot('chat.freenode.net', 6667, 'dby', '#xiyoulinux')
    transiter = transit()

    while True:
        try:
            (speaker, content) = ircbot.receive()
            print(content)
            reply = transiter.reply(content)
            ircbot.privmsg(reply, speaker)
        except:
            ircbot.quit()
            sys.exit()

