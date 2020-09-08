from rest_framework import serializers
from django.db.models import Avg 
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        #Parâmetros extras
        #Email não será apresentado, somente exigido quando for escrita
        extra_kwargs = {
            'email': {'write_only':True}
        }
        model = Avaliacao
        #Dados que serão mostrados
        fields = [
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        ]

    #Validando a nível de field, para cada field que queira fazer validações,
    #  faça um método validate_"FIELD"
    def validate_avaliacao(self,valor):
        # de 1 a 6-1
        if valor in range(1,6):
            return valor
        raise serializers.ValidationError('A avaliação precisa ser entre 1 e 5')

class CursoSerializer(serializers.ModelSerializer):
    #Somente leitura, não poderá cadastrar avaliaçoes pelo curso

    #Nested Relationship
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    #HyperLinked Related Field
    #avaliacoes = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='avaliacao-detail')

    #Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    #CUSTOMIZANDO O SERIALIZER
    #Atribui a esse campo um valor gerado por uma função
    media_avaliacoes = serializers.SerializerMethodField()
    class Meta:
        model = Curso
        
        fields = [
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        ]

    #O problema de casos como esse, é que toda vez que for serializado um curso
    #A API vai ter q calcular a média, É mais fácil criar um signal no model
    #E por lá, atualizar o field
    
    #Padrão para funções de campos de SerializerMethodField
    def get_media_avaliacoes(self,obj):
        #obj.avaliacoes = Related name definido no model
        #Funções de agregações 
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media * 2) / 2