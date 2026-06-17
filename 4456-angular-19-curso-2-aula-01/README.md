![Imagem de capa do curso "Angular 19: aplicando interação entre componentes com inputs e outputs", que faz parte da formação "Angular 19". O logotipo do GitHub e o nome "/alura-cursos" estão no canto superior esquerdo, e o logotipo da Alura no canto superior direito. Na parte inferior direita, há uma indicação de que o curso faz parte da trilha de Front-end.](./thumb.png)

# AnyBank

O AnyBank é um projeto que simula uma aplicação bancária, que mostra o saldo atual, possui um formulário para realizar novas transações e um extrato que exibe as transações já realizadas.

## 🔨 Funcionalidades do projeto

No AnyBank, é possível realizar depósitos e saques através de um formulário. Essas transações refletem automaticamente o valor do saldo exibido. Além disso, cada nova transação é registrada no extrato, que mostra as transações mais recentes primeiro e a data de cada uma.

## ✔️ Técnicas e tecnologias utilizadas

O desenvolvimento do projeto utilizou as seguintes técnicas e tecnologias:

- **Angular**: Framework utilizado para construir a aplicação, na versão 19.
- **CLI do Angular**: Ferramenta de linha de comando para agilizar a criação e organização do projeto.
- **Componentização**: Estrutura modular e reutilizável que define a base da aplicação.
- **Pipes**: Recurso do Angular que permite a formatação e transformação de dados, como datas e moedas.
- **Formulários orientados a template**: Uma das abordagens de se lidar com formulários no Angular.
- **Inputs e outputs**: Forma de passar dados entre componentes pais e filhos.
- **Signals e computed**: Funções da API de signals utilizadas para aplicar reatividade nos componentes.

## 📁 Link do Figma

Você pode [acessar o figma do projeto aqui](https://www.figma.com/community/file/1461475432377357666).

## 🛠️ Abrir e rodar o projeto

Você vai precisar do Node.js, versão 18 ou maior.

Após baixar ou clonar o projeto do GitHub, você precisa instalar as dependências utilizando o comando:

```bash
npm install
```

Depois, para executar o projeto em modo de desenvolvimento:

```bash
npm start
# ou:
ng serve
```

Então, acesse `http://localhost:4200/` no seu navegador.
