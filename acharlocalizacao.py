import requests
import json


#Achar o localizacao atraves do CEP
meu_cep = input('Digita seu CEP: ')
cep = requests.get(f"https://cep.awesomeapi.com.br/json/{meu_cep}") #coloque o CEP
cep = cep.json()
print('SEU CEP: {}'.format(cep['cep']))
print('SUA RUA: {}'.format(cep['address']))
print('SEU ESTADO: {}'.format(cep['state']))
print('BAIRRO: {}'.format(cep['district']))
print('CIDADE: {}'.format(cep['city']))
print('DDD: {}'.format(cep['ddd']))
