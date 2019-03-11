from socket import *

# 65535

syntax = "*" * 5

fip = open("/home/cntt-l-79/learning/python/ip.txt", "w")

with open("/home/cntt-l-79/learning/python/input.txt", "r") as fin:
    line = True
    start = int(fin.readline())
    end = int(fin.readline())
    while line:
        line = fin.readline()
        if (line == ''):
            break;
        input = line.strip().replace(r'/24', '')
        p1 = input.replace('.0','.')
        for i in range(1,255):
            remoteServer = p1 + str(i) +'\n'
            fip.write(remoteServer)
fin.close()
fip.close()
fresult = open("/home/cntt-l-79/learning/python/resultport.txt", "w")

with open("/home/cntt-l-79/learning/python/ip.txt", "r") as fscan:
    line = True
    while line:
        line = fscan.readline()
        if (line == ''):
            break;
        adress_ip = line
        ip = gethostbyname(adress_ip)

        count = 0
        fresult.write(adress_ip)
        print("---", adress_ip)
        for ports in range(start, end):
            try:
                print("Scanning port :%d" % (ports,))
                s = socket(AF_INET, SOCK_STREAM)
                s.settimeout(3)
                s.connect((ip, ports))
                s.settimeout(3)
                print("Port %d: is OPEN" % (ports,))
                count = count + 1
                fresult.write("\n\tPort %d: is OPEN\n" % (ports,))
            except:
                print("Port %d is CLOSED" % (ports,))
            s.close()
        print("Scanning finshed !")
        print("")
        print("%sFound %d open ports\n" % (syntax, count))
        fresult.write("\n\t%sFound %d open ports\n" % (syntax, count))
        fresult.write("%s\n" % ("="*25))
        print("*"*10)

fresult.close()
fscan.close()
