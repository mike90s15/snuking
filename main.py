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
            resultado = requests.get("https://ipapi.co/json").json()
            ip = resultado['ip']
            print("\n" + code_info + "IP.")
            print(code_details + f"Seu IP: {ip}")
            print(f'''
{C}[{G}i{C}] Formas de operação:

[{G}1{C}] Consultar meu IP.
[{G}2{C}] Consultar IP.
[{G}3{C}] Localizar.
[{G}4{C}] Voltar.
[{G}5{C}] {R}Sair.{C}
''')
            tool = input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')

'''
  if tool == "1":
     consultar(ip)
  elif tool == "2":
     ip=input(f'{C}[{G}*{C}] Informe o IP a ser consultado (COM pontos): {B}')
     consultar(ip)
  elif tool == "3":
     ip=input(f'{C}[{G}*{C}] Informe o IP a ser consultado (COM pontos): {B}')
     clear()
     localizar(ip)
  elif tool == "4":
     import consulta
     consulta.main()
  elif tool == "5":
      clear()
      print(f"\n{G}Somos uma legião.{C}\n")
      exit()
  else:
     clear()
     print(f'{C}[{R}-{C}] Seleção inválida.')
     time.sleep(0.2)
     main()


def again():
  opt = input("\n" + f'{C}[{G}+{C}] Deseja realizar uma nova consulta?[{G}s{C}/{R}n{C}]: ')
  if opt == "s":
      clear()
      main()
  elif opt == "n":
      print(f"\n{G}Somos uma legião.{C}\n")
      exit()
  else:
      clear()
      print(f'{C}[{R}-{C}] Seleção inválida.')
      time.sleep(0.2)
      exit()


def maps(ip):
  opt = input("\n" + f'{C}[{G}+{C}] Deseja localizar no {Y}Google Maps{C}?[{G}s{C}/{R}n{C}]: ')
  if opt == "s":
      localizar(ip)
  elif opt == "n":
      again()
  else:
      print(f'{C}[{R}-{C}] Seleção inválida.')
      time.sleep(0.2)
      exit()

def consultar(ip):
  clear()
  api = requests.get(f"https://ipapi.co/{ip}/json")
  resultado = api.json()
  ip = resultado['ip']
  print("\n" + f"{C}Endereço de IP: {B}{resultado['ip']}{C}")
  print(f"Cidade: {B}{resultado['city']}{C}")
  print(f"Região: {B}{resultado['region']}{C}")
  print(f"País: {B}{resultado['country_name']}{C}")
  print(f"Abreviação do país: {B}{resultado['country']}{C}")
  print(f"Capital do país: {B}{resultado['country_capital']}{C}")
  print(f"População do país: {B}{resultado['country_population']}{C}")
  print(f"Moeda: {B}{resultado['currency']}{C}")
  print(f"Nome da moeda: {B}{resultado['currency_name']}{C}")
  print(f"Código da região: {B}{resultado['region_code']}{C}")
  print(f"Código postal: {B}{resultado['postal']}{C}")
  print(f"Código do país: {B}{resultado['country_code']}{C}")
  print(f"Código do país ISO3: {B}{resultado['country_code_iso3']}{C}")
  print(f"Área do país: {B}{resultado['country_area']}{C}")
  print(f"País TLD: {B}{resultado['country_tld']}{C}")
  print(f"Código área: {B}{resultado['country_area']}{C}")
  print(f"Código do continente: {B}{resultado['continent_code']}{C}")
  print(f"União Européia: {B}{resultado['in_eu']}{C}")
  print(f"Latitude: {B}{resultado['latitude']}{C}")
  print(f"Longitude: {B}{resultado['longitude']}{C}")
  print(f"Fuso horário: {B}{resultado['timezone']}{C}")
  print(f"Código de Chamada: {B}{resultado['country_calling_code']}{C}")
  print(f"línguas: {B}{resultado['languages']}{C}")
  print(f"ASN: {B}{resultado['asn']}{C}")
  print(f"ORG: {B}{resultado['org']}{C}")
  print(f"Deslocamento UTF: {B}{resultado['utc_offset']}{C}")
  print(f"Versão: {B}{resultado['version']}{C}")
  maps(ip)


def localizar(ip):
  api = requests.get("https://ipapi.co/json")
  resultado = api.json()
  print(code_info + "Google Maps")
  print(code_info + "Gerando URL...")
  time.sleep(0.5)
  print ('\n' + code_result + f'Google Maps: {Y}' + 'https://www.google.com/maps/place/' + f"{resultado['latitude']}" + '+' + f"{resultado['longitude']}")
  again()
'''

main()
