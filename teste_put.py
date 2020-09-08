import requests

headers = {'Authorization' : 'Token c7c965eacea49afd96dc715e5c7f5923d5c3d424'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


cursoAtualizado = {
    "titulo":"Novo curso de Celular",
    "url":"http://www.celular.com.br",
}

#BUSCANDO O CURSO COM ID 6
#curso = requests.get(f'{url_base_cursos}6/', headers=headers)
#print(curso.json())
resultado = requests.put(url=f'{url_base_cursos}6/',headers=headers,data=cursoAtualizado)


assert resultado.status_code == 200

assert resultado.json()['titulo'] == cursoAtualizado['titulo']