from kamene.all import *


def listToString(s):
    str1 = " "
    return (str1.join(s))


data = ["botnet", "documentation", "ARP", "spoof", "DNS", "Monkey", "not_spam", "legit_traffic", "secret", "private", "DDOS", "start", "wannacry", "eternal blue", "takeover", "sudo", "password", "virus", "zombie."]


liste = ["10.0.10.7", "10.0.10.12", "10.0.10.13", "10.0.10.14", "10.0.10.16", "10.0.10.22", "10.0.10.23", "10.0.10.26", "10.0.10.28"
         "10.0.10.29", "10.0.10.30", "10.0.10.33"]

while True:
    for ip in liste:
        sampling = random.choices(data, k=4)
        convert = listToString(sampling)
        string = convert.replace(" ", "") + ".rigged"
        packet = IP(src="10.0.10.0/24", dst=ip)/UDP(dport=53)/DNS(rd=1,
                                                                  qd=DNSQR(qname=string)) / Raw(load="Injection complete")
        send(packet)
