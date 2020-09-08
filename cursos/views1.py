'''
VERSÃO BÁSICA DE USO

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Curso,Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
# Create your views here.


class CursoAPIView(APIView):
    """ API de Cursos da projeto 1 REST """
    #METODO GET 
    def get(self, request):
        cursos = Curso.objects.all()
        #Many é quando todos os cursos
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self,request):
        
        serializer = CursoSerializer(data=request.data)
        #Verificando se o serializer é valido, se não, retorna uma exception
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)



class AvaliacaoAPIView(APIView):
    """ API de Avaliações da projeto 1 REST """
    def get(self,request):
        serializer = AvaliacaoSerializer(Avaliacao.objects.all(), many=True)
        return Response(serializer.data)

    
    def post(self,request):
        serializer= AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #PODEMOS SUBISTITUIR O SERIALIZER.DATA POR ALGUM DICIONARIO DE RESPOSTA
        #ESPECIFICANDO OS CAMPOS DA RESPOSTA DO PRÓPRIO OBJETO serializer.data['id']
        return Response(serializer.data,status.HTTP_201_CREATED)

    '''