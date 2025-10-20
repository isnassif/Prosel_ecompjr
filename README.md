<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Descrição Técnica da API de Cadastro de Empresas</h1>

<p>Neste projeto, foi desenvolvida em linguagem Python e utilizando o framework FastAPI, juntamente com SQLAlchemy para gerenciamento do banco de dados, um software de gestão de empresas. O objetivo principal do sistema é realizar o cadastro e gerenciamento de empresas, oferecendo funcionalidades completas de criação, listagem, busca, atualização e exclusão de registros. O banco de dados utilizado é o PostgreSQL, garantindo persistência e integridade das informações.</p>

<p>A API foi desenvolvida para ser simples, rápida e escalável. As tecnologias principais empregadas são, a linguagem de programaçõ Python 3.10.12, FastAPI para as rotas e estrutura da aplicação, SQLAlchemy para o mapeamento objeto-relacional, Pydantic para validação de dados e Uvicorn como servidor de execução. A escolha dessas ferramentas visa garantir desempenho, clareza de código e facilidade de manutenção.</p>

<p>A estrutura do projeto é organizada em módulos para facilitar o entendimento e a expansão futura, como por exemplo, interface gráfica, login e testes de unidade. O arquivo principal, main.py, contém todas as rotas da API. A pasta model possui o arquivo company.py, responsável pelo modelo ORM que define a tabela de empresas no banco de dados. Já a pasta schemas contém o arquivo company.py com os modelos Pydantic usados na validação e serialização dos dados. A pasta config abriga o arquivo db.py, que é responsável pela conexão com o banco de dados e pela criação da sessão de comunicação com o PostgreSQL.</p>

<p>Antes de rodar o sistema, é necessário garantir que o banco de dados PostgreSQL esteja instalado e que exista um banco criado com o nome ecomp_jr_cadastros. A configuração da conexão utiliza o usuário padrão “postgres”, senha “post” e porta 5432, podendo ser alterada conforme o ambiente de execução. Após configurado, basta criar um ambiente virtual, instalar as dependências e iniciar o servidor</p>

<p>A API possui diversos endpoints. O endpoint GET /companys retorna todas as empresas cadastradas. O endpoint POST /companys cria uma nova empresa, exigindo informações como nome, CNPJ, cidade, ramo de atuação, telefone, e-mail e data de cadastro. Caso o CNPJ ou e-mail já estejam cadastrados, o sistema retorna um erro de conflito. Há também o endpoint GET /companys/{company_id}, que busca uma empresa específica pelo seu ID, e o GET /companys/search, que permite buscar empresas pelo nome, total ou parcial. O endpoint GET /companys/filter permite filtrar empresas por cidade e ramo de atuação. Para atualizar informações, utiliza-se o método PUT /companys/{company_id}, que altera apenas os campos informados no corpo da requisição. Por fim, o endpoint DELETE /companys/{company_id} remove uma empresa do banco de dados.</p>

<p>O modelo de dados da empresa é definido na classe Company, que representa a tabela empresas. Essa tabela contém as colunas id, name, cnpj, cidade, ramo_atuacao, telefone, email e data_de_cadastro. Os modelos Pydantic criam a estrutura de entrada e saída de dados: createCompany é usado para criação de novos registros e companyUpdate é usado para atualização parcial dos dados de uma empresa existente.</p>

<p>Em resumo, o projeto é uma solução completa e bem estruturada para o gerenciamento de cadastros empresariais, unindo boas práticas de desenvolvimento, uso de tecnologias modernas e uma arquitetura limpa, tornando-o ideal tanto para aprendizado quanto para uso em ambientes reais.</p>
</body>
</html>
