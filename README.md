# SIG-gerencimanto_de_tarefas

*Tarefa:* Criar um sistema de gerenciamento de tarefas com autenticação de usuários.

#### Requisitos:
1. *Autenticação de Usuários:*
   - Implementar registro de novos usuários.
   - Implementar login/logout.
   - Proteger certas rotas para que apenas usuários autenticados possam acessá-las.

2. *CRUD de Tarefas:*
   - Criar, ler, atualizar e deletar tarefas.
   - Cada tarefa deve ter um título, descrição, data de criação e status (pendente ou concluída).
   - As tarefas devem ser associadas a usuários específicos (um usuário só pode ver e gerenciar suas próprias tarefas).


#### Dicas para Não Se Perder:
1. *Entenda a Estrutura do Projeto Django:*
   - Familiarize-se com a estrutura padrão de projetos Django (apps, views, models, templates, etc.).
   - Entenda como o Django trata URLs e roteamento.

2. *Divida o Problema em Partes Menores:*
   - Comece implementando a autenticação de usuários (Django tem bibliotecas integradas como django.contrib.auth que facilitam isso).
   - Em seguida, modele a entidade Tarefa e implemente as operações CRUD.
   - Por fim, configure a API e implemente os testes.

3. *Documentação e Recursos:*
   - Utilize a documentação oficial do Django, que é muito completa e bem organizada.
   - Consulte tutoriais e exemplos práticos para esclarecer dúvidas específicas.

4. *Pratique Testes:*
   - Ter um bom entendimento de como escrever e rodar testes em Django é crucial, pois muitas entrevistas valorizam candidatos que se preocupam com a qualidade e a confiabilidade do código.
   