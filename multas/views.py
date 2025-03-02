from django.shortcuts import render
from .models import Multa
from django.db.models import Q, F, Value, Func
from django.db.models.functions import Greatest
from django.contrib.postgres.search import TrigramSimilarity

class Similarity(Func):
    function = 'SIMILARITY'
    output_field = None

def home(request):
    return render(request, 'multas/home.html')

def buscar(request):
    # Inicializa variáveis
    query = request.GET.get('q', '').strip()
    gravidade = request.GET.get('gravidade', '')
    multas = []
    
    if query:
        # Busca usando trigram similarity para permitir erros de digitação
        multas = Multa.objects.annotate(
            similarity_codigo=Similarity('codigo_infracao', Value(query)),
            similarity_infracao=Similarity('infracao', Value(query)),
            similarity=Greatest(
                F('similarity_codigo'),
                F('similarity_infracao'),
                Value(0.0)
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