import requests
import jsonpath

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

#Sempre retorna uma Lista
#resultados = jsonpath.jsonpath(avaliacoes.json(),'results')
#print(resultados)

#Primeiro resultado
primeira = jsonpath.jsonpath(avaliacoes.json(),'results[0]')
print(primeira)

nome = jsonpath.jsonpath(avaliacoes.json(),'results[0].nome')
print(nome)

# Todos os nomes das pessoas que avaliaram o curso
nomes = jsonpath.jsonpath(avaliacoes.json(),'results[*].nome')

print(nomes)