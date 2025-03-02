from django.shortcuts import render
from .models import Multa
from django.db.models import Q

def home(request):
    return render(request, 'multas/home.html')

def index(request):
    return render(request, 'multas/index.html')

def buscar(request):
    # Inicializa variáveis
    query = request.GET.get('q', '').strip()
    gravidade = request.GET.get('gravidade', '')
    multas = []
    
    if query:
        # Busca simples usando contains
        multas = Multa.objects.filter(
            Q(codigo_infracao__icontains=query) |
            Q(infracao__icontains=query)
        )

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