import requests
import threading


def rd(url, txt, ends):
    print("Executando...")
    for line in txt:
        response = requests.get(host + line)
        if ends == "y":
            print(f"{response.status_code} | GET | {url}{line}")
        else:
            if response.status_code < 404:
                print(f"{response.status_code} | GET | {url}{line}")
            else:
                pass


banner = """
▄████  █    ████▄ ████▄ ███     ▄      ▄▄▄▄▄      ▄▄▄▄▀ ▄███▄   █▄▄▄▄
█▀   ▀ █    █   █ █   █ █  █     █    █     ▀▄ ▀▀▀ █    █▀   ▀  █  ▄▀
█▀▀    █    █   █ █   █ █ ▀ ▄ █   █ ▄  ▀▀▀▀▄       █    ██▄▄    █▀▀▌ 
█      ███▄ ▀████ ▀████ █  ▄▀ █   █  ▀▄▄▄▄▀       █     █▄   ▄▀ █  █ 
 █         ▀            ███   █▄ ▄█              ▀      ▀███▀     █  
  ▀                            ▀▀▀                               ▀                                          
"""
print(banner)

host = str(input("Qual o dominio? "))
print("""
1 - word01.txt
2 - /usr/share/dirb/wordlists 
3 - /usr/share/dirb/common.txt 
4 - /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt 
5 - <caminho>

""")

word = str(input("Qual a wordlist? "))
errors = str(input("Deseja que erros sejam exibidos?[y/n]")).lower().strip()
pn = open(f"{word}", "rt")

rd(host, pn, errors)
