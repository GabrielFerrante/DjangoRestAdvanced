import requests

class TestCurso:
    headers = {'Authorization': 'Token a5a0aea8bc9e7aeb4eef463b3019bfd1751ec4eb'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'


    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)
        
        assert resposta.status_code == 200
    
    def test_get_curso(self):
        resposta = requests.get(url=self.url_base_cursos + '2/', headers=self.headers)
        
        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            'titulo' : 'Curso PyTest3',
            'url' : 'http://www.cursoPyTest3.com.br'
        }
        resposta = requests.post(
            url=self.url_base_cursos,
             headers=self.headers, 
             data=novo)
        
        assert resposta.status_code == 201

        assert resposta.json()['titulo'] == novo['titulo']

    
    def test_put_curso(self):
        atualizado = {
            'titulo' : 'Novo curso de PyTest',
            'url' : 'http://www.NewTeste.com.br'
        }

        resposta = requests.put(
            url=f'{self.url_base_cursos}9/',
            headers= self.headers,
            data = atualizado)
      
        assert resposta.status_code == 200

    def test_put_titulo_curso(self):
        atualizado = {
            'titulo' : 'Novo curso de PyTest 2',
            'url' : 'http://www.NewTeste2.com.br'
        }
        resposta = requests.put(
            url=f'{self.url_base_cursos}9/',
            headers= self.headers,
            data= atualizado)
        
        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(
            url=f'{self.url_base_cursos}9/',
            headers= self.headers)
        
        assert resposta.status_code == 204 and len(resposta.txt) == 0