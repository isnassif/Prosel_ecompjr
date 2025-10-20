<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Descrição Técnica da API de Cadastro de Empresas</h1>

<p>Este projeto é uma <strong>API desenvolvida em Python</strong> utilizando o framework <strong>FastAPI</strong>, juntamente com <strong>SQLAlchemy</strong> para gerenciamento do banco de dados. O objetivo principal do sistema é realizar o <em>cadastro e gerenciamento de empresas</em>, oferecendo funcionalidades completas de criação, listagem, busca, atualização e exclusão de registros. O banco de dados utilizado é o <strong>PostgreSQL</strong>, garantindo persistência e integridade das informações.</p>

<p>A API foi desenvolvida para ser simples, rápida e escalável. As tecnologias principais empregadas são <strong>Python 3.10</strong> ou superior, <strong>FastAPI</strong> para as rotas e estrutura da aplicação, <strong>SQLAlchemy</strong> para o mapeamento objeto-relacional, <strong>Pydantic</strong> para validação de dados e <strong>Uvicorn</strong> como servidor de execução. A escolha dessas ferramentas visa garantir desempenho, clareza de código e facilidade de manutenção.</p>

<p>A estrutura do projeto é organizada em módulos para facilitar o entendimento e a expansão futura. O arquivo principal, <code>main.py</code>, contém todas as rotas da API. A pasta <code>model</code> possui o arquivo <code>company.py</code>, responsável pelo modelo ORM que define a tabela de empresas no banco de dados. Já a pasta <code>schemas</code> contém o arquivo <code>company.py</code> com os modelos <strong>Pydantic</strong> usados na validação e serialização dos dados. A pasta <code>config</code> abriga o arquivo <code>db.py</code>, que é responsável pela conexão com o banco de dados e pela criação da sessão de comunicação com o <strong>PostgreSQL</strong>.</p>

<p>Antes de rodar o sistema, é necessário garantir que o banco de dados PostgreSQL esteja instalado e que exista um banco criado com o nome <code>ecomp_jr_cadastros</code>. A configuração da conexão utiliza o usuário padrão “postgres”, senha “post” e porta 5432, podendo ser alterada conforme o ambiente de execução. Após configurado, basta criar um ambiente virtual, instalar as dependências e iniciar o servidor com o comando <code>uvicorn main:app --reload</code>. Ao iniciar, a documentação interativa da API estará disponível em <a href="http://127.0.0.1:8000/docs" target="_blank">http://127.0.0.1:8000/docs</a>.</p>

<p>A API possui diversos endpoints. O endpoint <code>GET /companys</code> retorna todas as empresas cadastradas. O endpoint <code>POST /companys</code> cria uma nova empresa, exigindo informações como nome, CNPJ, cidade, ramo de atuação, telefone, e-mail e data de cadastro. Caso o CNPJ ou e-mail já estejam cadastrados, o sistema retorna um erro de conflito. Há também o endpoint <code>GET /companys/{company_id}</code>, que busca uma empresa específica pelo seu ID, e o <code>GET /companys/search</code>, que permite buscar empresas pelo nome, total ou parcial. O endpoint <code>GET /companys/filter</code> permite filtrar empresas por cidade e ramo de atuação. Para atualizar informações, utiliza-se o método <code>PUT /companys/{company_id}</code>, que altera apenas os campos informados no corpo da requisição. Por fim, o endpoint <code>DELETE /companys/{company_id}</code> remove uma empresa do banco de dados.</p>

<p>O modelo de dados da empresa é definido na classe <code>Company</code>, que representa a tabela <strong>empresas</strong>. Essa tabela contém as colunas <code>id</code>, <code>name</code>, <code>cnpj</code>, <code>cidade</code>, <code>ramo_atuacao</code>, <code>telefone</code>, <code>email</code> e <code>data_de_cadastro</code>. Os modelos <strong>Pydantic</strong> criam a estrutura de entrada e saída de dados: <code>createCompany</code> é usado para criação de novos registros e <code>companyUpdate</code> é usado para atualização parcial dos dados de uma empresa existente.</p>

<p>A API conta com documentação interativa automática gerada pelo próprio <strong>FastAPI</strong>, disponível nas interfaces <strong>Swagger UI</strong> e <strong>ReDoc</strong>, que permitem testar os endpoints diretamente pelo navegador. O sistema foi projetado para ser claro, modular e extensível, possibilitando futuras melhorias como autenticação com JWT, paginação de resultados, validações mais avançadas de CNPJ e e-mail, testes automatizados e containerização com Docker.</p>

<p>Em resumo, o projeto é uma solução completa e bem estruturada para o gerenciamento de cadastros empresariais, unindo boas práticas de desenvolvimento, uso de tecnologias modernas e uma arquitetura limpa, tornando-o ideal tanto para aprendizado quanto para uso em ambientes reais.</p>
</body>
</html>
