import requests

headers = {'Authorization' : 'Token c7c965eacea49afd96dc715e5c7f5923d5c3d424'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}6/', headers=headers)

assert resultado.status_code == 204

#testando se o tamanho do conteudo retorno é 0

assert len(resultado.text) == 0