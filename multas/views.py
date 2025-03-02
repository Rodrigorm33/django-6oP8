from django.shortcuts import render
from .models import Multa
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.core.cache import cache

def home(request):
    return render(request, 'multas/home.html')

def index(request):
    return render(request, 'multas/index.html')

@cache_page(60 * 60)  # Cache por 1 hora, já que as multas raramente mudam
def buscar(request):
    query = request.GET.get('q', '').strip()
    gravidade = request.GET.get('gravidade', '')
    page = request.GET.get('page', 1)
    
    # Adiciona busca ao histórico
    if query:
        historico = request.session.get('historico_busca', [])
        if query not in historico:
            historico.insert(0, query)
            historico = historico[:5]  # Mantém apenas as 5 últimas buscas
            request.session['historico_busca'] = historico

        # Melhora a busca usando Q objects e trigram similarity
        multas = Multa.objects.filter(
            Q(codigo_infracao__iexact=query) |  # Busca exata por código
            Q(codigo_infracao__istartswith=query) |  # Começa com o código
            Q(infracao__icontains=query) |  # Contém a descrição
            Q(artigos_ctb__icontains=query)  # Busca por artigos do CTB
        )

        if gravidade:
            multas = multas.filter(gravidade__iexact=gravidade)
        
        paginator = Paginator(multas, 10)  # Reduzido para 10 itens por página para mobile
        multas = paginator.get_page(page)
    else:
        multas = []
    
    gravidades = cache.get('gravidades_lista')
    if not gravidades:
        gravidades = list(Multa.objects.values_list('gravidade', flat=True).distinct())
        cache.set('gravidades_lista', gravidades, 60 * 60 * 24)  # Cache por 24h
    
    return render(request, 'multas/buscar.html', {
        'query': query,
        'multas': multas,
        'gravidade_selecionada': gravidade,
        'gravidades': gravidades,
        'historico': request.session.get('historico_busca', [])
    })