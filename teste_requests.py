import requests

#GET avaliacões
'''
avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

#Acessando o código de status HTTP
print(avaliacoes.status_code)

#sempre retorna um Dict
print(avaliacoes.json())

#acessando a quantidade de registros
print(avaliacoes.json()['count'])

#Acessando a próxima página de resultados
print(avaliacoes.json()['next'])

#Acessando os resultados dessa página
print(avaliacoes.json()['results'])

#Acessando o primeiro resultado
print(avaliacoes.json()['results'][0])


#Acessando o ID do primeiro resultado
print(avaliacoes.json()['results'][0]['id'])

'''
#GET avaliação

#avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/2')

#print(avaliacao.json())

#GET CURSOS

#PASSANDO O TOKEN
'''headers = {"Authorization":'Token a5a0aea8bc9e7aeb4eef463b3019bfd1751ec4eb'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/',headers=headers)

print(cursos.json())
'''