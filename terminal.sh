# Primeiro comando:
git rm --cached multas/forms.py

# Segundo comando (copie toda a linha):
git add multas/forms.py && git commit -m "fix: recria forms.py com UTF-8 encoding" && git push origin main

# Terceiro comando:
git add multas99/settings.py && git commit -m "feat: adiciona railway domain aos ALLOWED_HOSTS" && git push origin main

# Com base no log, o deploy foi bem-sucedido! Para acessar seu site no Railway, você tem algumas opções:

# 1. **Através do Dashboard do Railway**:
#    - Acesse https://railway.app/dashboard
#    - Clique no seu projeto
#    - Na aba "Settings" ou na visão geral, você encontrará a URL gerada (geralmente algo como `https://seu-projeto.up.railway.app`)

# 2. **Através do CLI do Railway**:
#    - Execute o comando abaixo no terminal:
railway status
# ou
railway domain
