# Projeto Final

## Orientações
1. Baixe o python e o node, pip e npm deverão vir juntos com o download de ambos
2. Vá para a pasta root do projeto, onde contém as pastas "core" "fast_api" e "react"
2. Rode ```pip install -r requirement``` as dependencias de python do projeto deverão ser instaladas
3. Vá para a página react/react-app e rode ```npm install```
4. rode npm start para rodar a aplicação de react
5. Abra outro terminal, vá para a pasta root do projeto e rode ```uvicorn fast_api.main:app --reload``` é importante que esteja na parte root do projeto, por causa de importações relativas em python, caso rode direto na pasta do fast_api não irá funcionar
6. As duas aplicações deverão estar rodando em 2 portas diferentes agora, enquanto o react roda na porta 3000, a api, utilizando o fast api deverodar na porta 8000
7. Para criar o banco de dados, apenas vá para o endereço ```http://127.0.0.1:8000/``` ou ```http://localhost:8000/```, a primeira vez irá criar o banco de dados, outras vezes não é mais necessário
8. Agora poderá ir para ```http://localhost:3000/``` fazer o cadastro, logar e a aplicação deverá estar rodando normalmente.

## Observações
1. Não tive tempo pra fazer uma interface mais trabalhada, apesar de funcional
2. Sempre que criar uma conta corrente, não é necessário fornecer a conta, mas irá ser retornado um número na tela, aconselho que salve esse número antes de testar as próximas funcionalidades, assim poderá fazer transferência entre outros.
3. Não há questões profundas de autenticação, o certo mesmo seria para cada endpoint, verificar se a pessoa ta logada, com o token dela, etc..
4. É possível fazer transferência de qualquer conta para qualquer conta também, não tive tempo pra fazer somente a limitação da pessoa fazer a transferência somente se a conta for dela
5. Planejo refatorar esse código mais pra frente, principalmente a questão do front.

## Testes
1. Por utilidade, acabei fazendo uns testes de integração do back-end, para testar o banco de dados postgres e tal, para testar, basta rodar no root "python tests.py", irá criar um banco de dados chamados test.db
2. Para visualizar o banco de dados em si, basta baixar a extensão no vscode chamado SQLITE VIEWER.
