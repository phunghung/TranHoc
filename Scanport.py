import socket
import subprocess
import sys
from datetime import datetime

def ScanPort():
    remoteServer = input("Enter a domain/ip to scan: ")
    start = int(input("Enter starting port number : "))
    end = int(input("Enter ending port number : "))
    remoteServerIP = socket.gethostbyname(remoteServer)

    print("-" * 60)
    print("Please wait, scanning", remoteServerIP)
    print("-" * 60)

    t1 = datetime.now()

    try:
        for port in range(start, end):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {}: Open".format(port))
            sock.close()

    except KeyboardInterrupt:
        print("You Interrupt Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    t2 = datetime.now()
    total = t2 - t1

    print('Scanning completed in: ', total)

ScanPort()
