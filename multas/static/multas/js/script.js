// Função para inicializar os favoritos
function initializeFavorites() {
    // Recupera favoritos do localStorage
    const favorites = JSON.parse(localStorage.getItem('favorites') || '[]');
    
    // Atualiza ícones de favoritos
    document.querySelectorAll('.btn-favorite').forEach(btn => {
        const multaId = btn.dataset.multaId;
        if (favorites.includes(multaId)) {
            btn.innerHTML = '<i class="fas fa-star"></i>';
        } else {
            btn.innerHTML = '<i class="far fa-star"></i>';
        }
    });
}

// Função para alternar favorito
function toggleFavorite(button) {
    const multaId = button.dataset.multaId;
    let favorites = JSON.parse(localStorage.getItem('favorites') || '[]');
    
    if (favorites.includes(multaId)) {
        // Remove dos favoritos
        favorites = favorites.filter(id => id !== multaId);
        button.innerHTML = '<i class="far fa-star"></i>';
        showToast('Removido dos favoritos');
    } else {
        // Adiciona aos favoritos
        favorites.push(multaId);
        button.innerHTML = '<i class="fas fa-star"></i>';
        showToast('Adicionado aos favoritos');
    }
    
    localStorage.setItem('favorites', JSON.stringify(favorites));
    
    // Anima o botão
    button.classList.add('animate__animated', 'animate__rubberBand');
    setTimeout(() => {
        button.classList.remove('animate__animated', 'animate__rubberBand');
    }, 1000);
}

// Função para mostrar toast de notificação
function showToast(message) {
    const toast = document.createElement('div');
    toast.className = 'toast-notification';
    toast.textContent = message;
    document.body.appendChild(toast);
    
    // Anima entrada
    setTimeout(() => toast.classList.add('show'), 100);
    
    // Remove após 3 segundos
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// Função para aplicar filtro de gravidade
function filterByGravidade(gravidade) {
    const cards = document.querySelectorAll('.card');
    
    cards.forEach(card => {
        if (gravidade === 'todas' || card.classList.contains(gravidade)) {
            card.style.display = 'block';
            // Adiciona animação de fade in
            card.classList.add('animate__animated', 'animate__fadeIn');
        } else {
            card.style.display = 'none';
        }
    });
}

// Função para realizar busca
function performSearch() {
    const searchInput = document.querySelector('.search-input');
    const searchTerm = searchInput.value.toLowerCase();
    const cards = document.querySelectorAll('.card');
    let found = false;
    
    cards.forEach(card => {
        const text = card.textContent.toLowerCase();
        if (text.includes(searchTerm)) {
            card.style.display = 'block';
            card.classList.add('animate__animated', 'animate__fadeIn');
            found = true;
        } else {
            card.style.display = 'none';
        }
    });
    
    // Mostra/esconde mensagem de nenhum resultado
    const noResults = document.querySelector('.no-results');
    if (noResults) {
        noResults.style.display = found ? 'none' : 'block';
    }
}

// Event Listeners
document.addEventListener('DOMContentLoaded', () => {
    // Inicializa favoritos
    initializeFavorites();
    
    // Listener para botões de favorito
    document.querySelectorAll('.btn-favorite').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            toggleFavorite(btn);
        });
    });
    
    // Listener para filtro de gravidade
    const gravidadeFilter = document.querySelector('.gravidade-filter');
    if (gravidadeFilter) {
        gravidadeFilter.addEventListener('change', (e) => {
            filterByGravidade(e.target.value);
        });
    }
    
    // Listener para campo de busca
    const searchInput = document.querySelector('.search-input');
    if (searchInput) {
        let timeout = null;
        searchInput.addEventListener('input', () => {
            // Debounce para melhor performance
            clearTimeout(timeout);
            timeout = setTimeout(performSearch, 300);
        });
    }
    
    // Listener para botão de busca
    const searchButton = document.querySelector('.btn-search');
    if (searchButton) {
        searchButton.addEventListener('click', (e) => {
            e.preventDefault();
            performSearch();
        });
    }
});