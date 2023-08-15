# luggfinder
Um webapp para gerenciar ocorrências com bagagens em aeroportos.

# Proposta
Facilitar o dia-a-dia do gerenciamento das ocorrências, apresentando dois lados: o da empresa aérea e o do fornecedor, de forma interativa com uma interface simples e direta ao ponto.
Em resumo, este é o fluxo:
 1- Empresa Aérea insere o processo no sistema.
 2- Solicitado o serviço do fornecedor.
 3- Fornecedor conclui o serviço e insere o custo.
 4- Se necessário, a empresa aérea confere e aprova o valor.
 5- Fornecedor emite nota fiscal e faz o upload para o sistema.

 É possível automatizar a inserção de dados dos processos através da extensão do navegador chrome, disponível em "chrome_extension". É feito uma compilação de dados através de um scrap
 simples. Basta o usuário informar o número do processo ou um 'range' (ex.:AAABB12300 até AAABB12310).

 # Estrutura Geral
  - Banco de Dados: SQLAlchemy com SQLite;
  - BackEnd: Python utilizando Flask;
  - FrontEnd: HTML, CSS, Javascript;
  - Hospedagem: VPS pessoal, à principio será postado online em "app.lucaslannes.com.br", posteriormente em domínio próprio - "aerotools.com.br/luggfinder"
