#  File : ser.py
# coding=utf-8
# cam with twisted
#  Modified date: 2014-08-25 21:23
import optparse
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ServerFactory


def parse_args():
    usage = 'usage: % python file hostname:port'

    parser = optparse.OptionParser(usage)

    _, address = parser.parse_args()

    if not address:
        print parser.format_help()
        parser.exit()

    def parse_address(addr):
        if ':' not in addr:
            host = '127.0.0.1'
            port = addr
        else:
            host, port = addr.split(":", 1)

        if not port.isdigit():
            parser.error('port must be integers.')

        return host, int(port)

    return map(parse_address, address)

class CamProtocol(Protocol):
    
    def dataReceived(self, data):
        pass
    
    def connectionMade(self):
        print 'New connection from %s' % str(self.factory.transport.getPeer())
    
    def connectionLost(self):
        print 'Lose connection from %s' % str(self.factory.transport.getPeer())

class CamFactory(ServerFactory):
    protocol = CamProtocol

    def __init__(self):
        pass
    

def main():
    address = parse_args()

    factory = CamFactory()
    print 'Server-Cam on %s' %port.getHost()

if __name__ == '__main__':
    main()
