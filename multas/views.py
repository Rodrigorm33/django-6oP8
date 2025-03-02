from django.shortcuts import render
from django.db import models
from .models import Multa
from django.db.models import Q, F, Value, Func, FloatField
from django.db.models.functions import Cast, Greatest
from django.contrib.postgres.search import TrigramSimilarity

class WordSimilarity(Func):
    function = 'word_similarity'
    output_field = FloatField()
    template = "%(function)s(%(expressions)s)"

def home(request):
    return render(request, 'multas/home.html')

def buscar(request):
    # Inicializa variáveis
    query = request.GET.get('q', '').strip()
    gravidade = request.GET.get('gravidade', '')
    multas = []
    
    if query:
        # Busca usando word_similarity para permitir erros de digitação
        multas = Multa.objects.annotate(
            codigo_str=Cast('codigo_infracao', output_field=models.TextField()),
            similarity_codigo=WordSimilarity('codigo_str', Value(query)),
            similarity_infracao=WordSimilarity('infracao', Value(query)),
            similarity=Greatest(
                F('similarity_codigo'),
                F('similarity_infracao'),
                Value(0.0, output_field=FloatField())
            )
        ).filter(
            Q(similarity__gt=0.3) |  # Resultados com similaridade > 0.3
            Q(codigo_infracao__icontains=query) |
            Q(infracao__icontains=query)
        ).order_by('-similarity')

        # Filtro por gravidade se especificado
        if gravidade:
            multas = multas.filter(gravidade__iexact=gravidade)
        
        # Limita a 50 resultados para performance
        multas = multas[:50]
    
    # Obtém lista de gravidades únicas para o filtro
    gravidades = Multa.objects.values_list('gravidade', flat=True).distinct().order_by('gravidade')
    
    return render(request, 'multas/buscar.html', {
        'query': query,
        'multas': multas,
        'gravidade_selecionada': gravidade,
        'gravidades': gravidades
    }) 