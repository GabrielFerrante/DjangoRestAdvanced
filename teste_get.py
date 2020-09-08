import requests

headers = {'Authorization' : 'Token a5a0aea8bc9e7aeb4eef463b3019bfd1751ec4eb'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url = url_base_cursos, headers=headers)

print(resultado.json())

#TESTANDO SE O ENDPOINT ESTÁ CORRETO
#SE TIVER ALGO ERRADO, IRÁ APARECER NO PROMPT
assert resultado.status_code == 200


#TESTANDO A QUANTIDADE DE REGISTROS

assert resultado.json()['count'] == 5

#TESTANDO SE O TITULO DO PRIMEIRO CURSO ESTA CORRETO

assert resultado.json()['results'][0]['titulo'] == 'Criação de APIs REST com Django REST Framework'