#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: set ai cindent et sw=4 ts=4 nowrap foldmethod=marker:
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineOnlyReceiver
from twisted.internet import reactor
class Chat(LineOnlyReceiver):
    def lineReceived(self, data):
        print data
        self.factory.sendAll("%s: %s" % (self.getId(), data))
    def getId(self):
        return str(self.transport.getPeer())
    def connectionMade(self):
        print "New connection from", self.getId()
        self.transport.write("Welcome to the chat server, %s\n" % self.getId())
        self.factory.addClient(self)
    def connectionLost(self, reason):
         self.factory.delClient(self)
class ChatFactory(Factory):
    protocol = Chat
    def __init__(self):
        self.clients = []
    def addClient(self, newclient):
        self.clients.append(newclient)
    def delClient(self, client):
        self.clients.remove(client)
    def sendAll(self, message):
        for proto in self.clients:
            proto.transport.write(message + "\n")
reactor.listenTCP(10000, ChatFactory())
reactor.run()
