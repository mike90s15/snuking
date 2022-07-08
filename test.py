#!/usr/bin/env python
#Snuking / Somos uma legião. 2021 ©                        #Mike Edwards / Somos uma legião. 2022 ©

import time
import os
import platform
try:
    import requests
    import bs4
    import html5lib
    import phonenumbers
    import argparse
    import urllib3
    import colorama
except:
    os.system("python3 -m pip install --upgrade pip")
    os.system("pip install -r requirements.txt")
    clear()
    print(code_result + "Instalado com sucesso.\n")
    #main()

def clear():
    if platform.system() == "Linux": print('\033c', end='')
    else: os.system("cls")

clear()
R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'

code_info = C + '[' + Y + 'i' + C + '] '
code_details = C + '[' + G + '*' + C + '] '
code_result = C + '[' + G + '+' + C + '] '
code_error = C + '[' + R + '!' + C + '] '

print(f'''\033[1;37m
              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        ▓▓▓▓██░░░░░░░░░░░░░░░░▓▓██▓▓
     ██░░░░                    ░░░░▓▓
    ▓▓░░                            ░░▓▓
  ██░░                                ░░██
  ██    ░░░░▓▓░░░░      ░░░░░░░░░░░░    ▓▓
  ▓▓  ▓▓░░▒▒▓▓▓▓▓▓░░    ░░▓▓▓▓▓▓▒▒░░▓▓  ▓▓
  ▓▓██          ▓▓██    ████          ██▓▓
  ▓▓            ░░░░    ░░░░          ░░▓▓
  ▓▓▒▒  ▒▒▒▒▓▓▒▒░░░░    ░░░░▒▒▒▒▓▓▒▒  ▒▒▓▓
  ▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓░░    ░░▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓
  ▓▓░░  ░░░░░░░░  ▓▓    ██  ░░░░░░░░  ░░▓▓
  ▓▓  ░░░░        ▓▓    ██        ░░░░  ▓▓
  ▓▓░░░░░░░░      ▓▓    ██      ░░░░░░░░▓▓
  ▓▓░░░░░░░░            ▓▓        ░░░░  ██
  ▓▓░░▓▓        ▓▓        ▓▓        ▓▓░░▓▓
  ▓▓░░▓▓▓▓        ▓▓░░░░▓▓        ▓▓▓▓░░▓▓
  ▓▓░░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ░░▓▓
  ▓▓░░░░░░▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓
    ▒▒  ░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░▒▒░░░░▒▒
      ▓▓    ░░░░░░░░░░░░░░░░░░░░  ░░▓▓
      ▓▓░░    ░░░░░░██▓▓░░░░░░    ░░▓▓
        ▓▓░░        ▓▓▓▓        ░░▓▓
          ▓▓░░    ░░▓▓▓▓░░    ░░▓▓
            ▓▓░░  ░░▓▓▓▓░░  ░░▓▓
              ██░░  ▓▓▓▓  ░░▒▒
                ▓▓▓▓▓▓▓▓▓▓▓▓
             SNUKING / ANONYMOUS
             Mike    / ANONYMOUS                           '''); time.sleep(3)
clear()

def main():
    clear()
    v = "1.0.3"
    print(f'''{G}
\n
.----.______
|           |
|    ___________
|   /          /
|  /          /
| /          /
|/__________/ {v}
\033[1;37m
 ''')
    #print(f"{Y}Atual: {version}\033[1;37m")
    print("\n" + code_info + "Menu.")
    print(f'''
\033[1;37m[{G}i\033[1;37m] Formas de operação:

[{G}01\033[1;37m] IP.
[{G}02\033[1;37m] Nome.
[{G}03\033[1;37m] CPF.
[{G}04\033[1;37m] Vizinhos.
[{G}05\033[1;37m] CEP.
[{G}06\033[1;37m] CNPJ.
[{G}07\033[1;37m] Placa.
[{G}08\033[1;37m] Telefone.
[{G}09\033[1;37m] BIN.
[{G}10\033[1;37m] Gerador.
[{G}11\033[1;37m] YouTube.

[{G}44\033[1;37m] Atualizar.
[{G}55\033[1;37m] Novidades.
[{G}66\033[1;37m] Ajuda.
[{G}00\033[1;37m] {R}Sair.\033[1;37m
''')
    tool=input(f'\033[1;37m[{G}+\033[1;37m] Selecione a forma de operação:{B} ')
    match int(tool):
        case 1:
            clear()
            import ip
            ip.main()

main()
