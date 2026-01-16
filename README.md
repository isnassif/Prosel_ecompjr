<h1>Sistema de Gerenciamento de Empresas com FastAPI & PostgreSQL</h1> 

<p>Olá! Este repositório contém uma API robusta desenvolvida para o gerenciamento de cadastros de empresas. O projeto utiliza tecnologias modernas como <strong>FastAPI</strong> para o framework web, <strong>SQLAlchemy</strong> como ORM e <strong>Docker</strong> para containerização, garantindo um ambiente de desenvolvimento isolado e escalonável. Esse sistema foi desenvolvimento como desafio técnico para entrar na Ecomp Júnior, a empresa júnior de computação da Universidade Estadual de Feira de Santana. Abaixo, apresento o relatório detalhado da arquitetura e funcionalidades com alguns trechos visuais do código, é importante que você também verifique os códigos.</p>

<section class="container"> 
  
<h2>1. Arquitetura de Dados e Persistência</h2> 

<p>A base do sistema foi construída utilizando o <strong>PostgreSQL</strong> como banco de dados relacional. A integração entre o código Python e o banco é feita através do SQLAlchemy, permitindo uma manipulação de dados orientada a objetos.</p> 

<div class="metodo"> 
  <ul> 
    <li> <strong>Modelagem (SQLAlchemy):</strong> O arquivo <code>model/company.py</code> define a estrutura da tabela <code>"empresas"</code>, incluindo campos como CNPJ, e-mail e ramo de atuação. O comando <code>create_all(engine)</code> garante que a tabela seja criada automaticamente ao iniciar a aplicação. </li> 
    <li> <strong>Gerenciamento de Sessão (Dependency Injection):</strong> Utilizei o padrão <em>yield</em> na função <code>get_db</code>. Isso garante que cada requisição abra uma conexão exclusiva com o banco e, o mais importante, feche-a automaticamente após o uso, evitando vazamentos de memória (memory leaks). </li> 
    <li> <strong>Configuração Dinâmica:</strong> O arquivo <code>config/db.py</code> utiliza variáveis de ambiente (<code>os.getenv</code>) para localizar o host do banco, permitindo que o mesmo código funcione tanto localmente quanto dentro de containers Docker. </li> </ul> </div>

  <div align="center">
      <img src="https://github.com/user-attachments/assets/79ef0ffb-0bde-4969-99b8-0759cc3f6486" width="393" height="285" style="object-fit: cover;">
      <br>
      <em>Figura 1: Código da estrutura da tabela empresas. </em>
  </div>


<h2>2. Validação e Segurança com Pydantic (Schemas)</h2> 

<p>Para garantir que os dados inseridos na API sejam íntegros e sigam as regras de negócio, implementei schemas utilizando o <strong>Pydantic</strong>. Isso fornece uma camada de segurança e documentação automática, garantindo que garantir que a API nunca processe dados "sujos" ou inválidos.</p>

<div class="metodo"> 
  <ul> 
    <li> <strong> Validação de CNPJ:</strong>  Implementei um <code>@field_validator</code> customizado para garantir que o CNPJ contenha apenas números, além de restrições de tamanho fixo (14 caracteres), evitando erros de inserção. </li> 
    <li> <strong> Tipagem Estrita (EmailStr): </strong> O uso do tipo <code>EmailStr</code> valida automaticamente se o formato do e-mail é válido (ex: nome@dominio.com) antes mesmo de chegar ao banco de dados. </li> 
    <li> <strong> Update Parcial Inteligente: </strong> Diferente do cadastro, o schema de atualização utiliza campos <code>Optional</code>. Isso permite o método <strong>PATCH/PUT</strong> parcial, onde o usuário pode alterar apenas o telefone, por exemplo, sem precisar reenviar todos os outros dados. </li> 
  </ul> 
</div>

  <div align="center">
      <img src="https://github.com/user-attachments/assets/4b22ab58-804b-4ec4-b283-7abcf073b05e" width="649" height="389" style="object-fit: cover;">
      <br>
      <em>Figura 2: Código utilizado para atualizar uma empresa e paradefinir os dados de retorno para o usuário. </em>
  </div>


<h2>3. Funcionalidades da API (Endpoints)</h2> 

<p>A API segue os princípios <strong>RESTful</strong>, oferecendo um CRUD (Create, Read, Update, Delete) completo, além de funcionalidades de busca avançada.</p>

<div clss="metodo"> 
  <ul> 
    <li> <strong>Criação com Lógica de ID e Unicidade:</strong> O endpoint <code>POST</code> verifica se o CNPJ ou E-mail já existem para evitar duplicidade (Erro 409). Além disso, implementei uma lógica manual para encontrar o próximo ID disponível, garantindo organização sequencial. </li> 
    <li> <strong>Filtros Avançados (ILike):</strong> Os endpoints de busca e filtro utilizam o operador <code>.ilike()</code> do SQLAlchemy. Isso permite buscas "case-insensitive" (não diferencia maiúsculas de minúsculas) e parciais, facilitando a localização de empresas por nome ou cidade. </li> 
    <li> <strong>Tratamento de Exceções:</strong> Todos os endpoints possuem verificações <code>if not results</code> que disparam <code>HTTPException 404</code>, retornando mensagens claras para o usuário caso um recurso não seja encontrado. </li> 
  </ul> 
</div>


<h2>4. Containerização com Docker e Docker Compose</h2> 

<p>Para facilitar o deploy e a padronização do ambiente, a aplicação foi totalmente "dockerizada".</p>

<div class="metodo"> <ul> <li> <strong>Dockerfile Otimizado:</strong> Utilizei a imagem <code>python:3.10-slim</code> para manter o container leve. O processo inclui a instalação de dependências do sistema (<code>libpq-dev</code>) necessárias para a comunicação com o PostgreSQL. </li> <li> <strong>Orquestração (Docker Compose):</strong> O arquivo <code>docker-compose.yml</code> gerencia dois serviços simultâneos: a <code>api</code> (FastAPI) e o <code>db</code> (Postgres). </li> <li> <strong>Interdependência (depends_on):</strong> Configurei a API para aguardar o serviço de banco de dados, garantindo que a aplicação não quebre ao tentar se conectar a um banco que ainda está iniciando. </li> </ul> </div>

</section>

<h2>5. Interface Automática e Documentação (Swagger UI)</h2> <p>Uma das funcionalidades mais poderosas da arquitetura implementada é a geração automática de documentação interativa. Ao utilizar o FastAPI combinado com os Schemas do Pydantic, o sistema disponibiliza uma interface visual completa para testes sem a necessidade de ferramentas externas como Postman ou Insomnia.</p>

<div class="metodo"> <ul> <li> <strong>Swagger UI (/docs):</strong> Acessível diretamente pelo navegador, esta interface lista todos os endpoints criados, os métodos HTTP permitidos e os modelos de dados esperados (JSON), permitindo a execução de requisições em tempo real. </li> <li> <strong>Redoc (/redoc):</strong> Uma documentação alternativa, mais focada em leitura e organização para desenvolvedores externos, apresentando de forma limpa como consumir a API de cadastros. </li> <li> <strong>Teste de Schema em Tempo Real:</strong> A interface valida os campos obrigatórios (como CNPJ e e-mail) antes mesmo de enviar a requisição, exibindo erros de validação visualmente caso algum dado não cumpra os requisitos definidos no <code>schemas/company.py</code>. </li> </ul> </div>

<div align="center">


<em>Figura 4: Interface do Swagger UI gerada automaticamente para o gerenciamento de empresas. </em> </div>
