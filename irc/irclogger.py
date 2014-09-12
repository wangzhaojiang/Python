#!/usr/bin/env python2

import socket, sys, re, time

class writer:
    """
    log msg with datetime
    
    @staticmethod
    def write(msg):
        name = time.strftime("%Y-%m-%d.log", time.localtime())
        fp = open("/var/ftp/pub/"+name, "a")
        stamp = time.strftime("%H:%M", time.localtime())
        content = stamp + ' ' + msg
        fp.write(content + '\n')
        fp.close()
	"""

class bot:
    """
    handle some IRC operations.
    """
    def __init__(self, host, port, nick, channel):
        self._nick = nick
        self._channel = channel
        self._irc = socket.socket(socket.AF_INET6, socket.SOCK_STREAM) # for ipv6
        #self._irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # for ipv4
        self._irc.connect((host, port))
        self.nick().user().join()

    def sendcmd(self, s):
        self._irc.send(s + "\r\n")
        return self

    def pong(self, data):
        return self.sendcmd("PONG " + data.split()[1])

    def nick(self):
        return self.sendcmd("NICK %s" % self._nick)

    def user(self):
        return self.sendcmd("USER %s %s %s: Logger" % (self._nick, self._nick, self._nick))

    def join(self):
        return self.sendcmd("JOIN %s" % self._channel)

    def quit(self):
        return self.sendcmd("QUIT")

    def proc_join(self, data):
        info = re.findall("^:(.*?)!.* JOIN (#.*?)$", data)
        if not info:
            return False
        user = info[0][0]
        channel = info[0][1].strip()
       # writer.write(user + " JOIN %s" % channel)
        return True

    def proc_quit(self, data):
        info = re.findall("^:(.*?)!.* QUIT (.*)$", data)
        if not info:
            return False
        user = info[0][0]
       # writer.write(user + " QUIT")
        return True

    def proc_privmsg(self, data):
        info = re.findall("^:(.*?)!.* PRIVMSG (#.*?) (:.*)$", data)
        if not info:
            return False
        user = info[0][0]
        msg = info[0][2].strip().strip(':')
        if "\x01ACTION" in msg:
            me = re.findall("\x01ACTION (.*)\x01", msg)[0]
       #     writer.write('*' + user + ' ' + me)
       # else:
       #     writer.write(user + ": " + msg)
        return True

    def log(self):
        while True:
            data = self._irc.recv(4096)
            print(data)

            # ignore system info
            if re.findall("^:(.*?).freenode.net", data):
                continue

            if "PING" in data:
                self.pong(data)
            if "KICK" in data and self._nick in data:
                self.join()

            self.proc_join(data) or self.proc_quit(data) or self.proc_privmsg(data)


if __name__ == "__main__":
    ircbot = bot('ipv6.chat.freenode.net', 6667, 'condy_hehe', '#xiyoulinux')
    try:
        ircbot.log()
    except KeyboardInterrupt:
        ircbot.quit()
        sys.exit()
