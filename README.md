# AgroLife

Sistema de Gestão Agropecuária

## Pré-requisitos
- Python 3.10+
- pip

## Passo a passo para rodar o projeto

1. **Clone o repositório e acesse a pasta do projeto:**
   ```bash
   cd ProjetoAgroLife
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplique as migrações:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crie um superusuário:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Rode o servidor:**
   ```bash
   python manage.py runserver
   ```

7. **Acesse no navegador:**
   - http://127.0.0.1:8000/
   - http://127.0.0.1:8000/admin/

---

- O frontend utiliza Tailwind CSS via CDN (não precisa de Node.js ou npm).
- Para alterar a logo, substitua o arquivo em `boi/static/img/logo.png`.

---

Qualquer dúvida, entre em contato com o responsável pelo projeto. 