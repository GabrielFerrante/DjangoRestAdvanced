import requests

headers = {'Authorization' : 'Token a5a0aea8bc9e7aeb4eef463b3019bfd1751ec4eb'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novoCurso = {
    "titulo":"Gerência de projetos",
    "url":"http://www.projetos.com",

}

resultado = requests.post(url=url_base_cursos,headers=headers,data=novoCurso)


#TESTANDO O CÓDIGO STATUS HTTP
assert resultado.status_code == 201

#TESTANDO SE O TITULO DO CURSO É O MESMO QUE O INSERIDO
assert resultado.json()['titulo'] == novoCurso['titulo']