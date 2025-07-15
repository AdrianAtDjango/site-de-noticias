<h1>📰🟡 Rio Branco Times - Um site simples de notícias</h1>

<h3>Rio Branco Times é uma empresa ficticia que busca se aventurar no ramo do jornalismo, para isso criei um site extremamente simples para a listagem e leitura de noticias da página, utilizando Django e suas tecnologias.</h3>
<br>

<h2>📦 Funcionalidades</h2>
<ul>
  <li>Listagem de notícias</li>
  <li>Leitura de notícias</li>
  <li>Criação e edição de notícias pelo django-admin</li>
  <li>Design limpo e fluido com SCSS e CSS</li>
  <li>HTML semântico</li>
</ul>

<br>
<h2>⚙️ Tecnologias Utilizadas</h2>
<ul>
  <li>Python 3.13+</li>
  <li>Django</li>
  <li>SQLite (banco de dados padrão)</li>
  <li>HTML e SCSS (com DTL)</li>
</ul>

<br>
<h2>🚀 Como executar o projeto</h2>
<ol>
  <li>Clone o repositório:</li>
  
    git clone https://github.com/seu-usuario/site-de-noticias.git
    cd site_noticias/noticias

  <li>Crie e ative um ambiente virtual:</li>

    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate

  <li>Aplique as migrações:</li>

    python manage.py migrate
    # faz as migrações das models

  <li>Execute o servidor de desenvolvimento:</li>
  
    python manage.py runserver
    # roda o servidor da aplicação

  <li>Acesse o sistema:</li>
    <ul>
      <li>Interface de uso: http://127.0.0.1:8000</li>
      <li>Admin Django: http://127.0.0.1:8000/admin</li>
    </ul>
</ol>

<br>
<h2>📌 Notas</h2>
<ul>
  <li>O projeto já inclui o banco de dados db.sqlite3. Você pode apagá-lo e recriar se quiser começar do zero.</li>
</ul>
