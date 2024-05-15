# Introdução

Este repositório mantém o projeto final da disciplina de **Plataformas de Backend - Python** do curso de **Desenvolvimento Web FullStack** da pós-graduação da **PUC Minas**. Trata-se de um CRUD de alunos em Django utilizando templates e uma API REST para explorar os conceitos aprendidos nas aulas.

## Setup inicial

1 - Faça o clone do repositório:

```
git clone git@github.com:RicardoGPP/dwfs-pbpol-student-crud.git
```

2 - Acesse o diretório da aplicação:

```
cd dwfs-pbpol-student-crud
```

3 - Crie e execute as migrations:

```
python manage.py makemigrations
python manage.py migrate
```

4 - Crie um usuário (preencha de acordo com o necessário):

```
python manage.py createsuperuser
```

5 - Suba o servidor:

```
python manage.py runserver 8000
```

## API REST

A aplicação de CRUD de alunos disponibiliza uma API REST para interação com o modelo. Esta API usa autenticação BASIC para os métodos POST, PUT, PATCH e DELETE, então é necessário enviar o usuário e senha criados anteriormente para a devida autenticação. Os endpoints disponíveis são:

```
GET: /api/alunos
GET: /api/alunos/<id>/
POST: /api/alunos/
PUT: /api/alunos/<id>/
PATCH: /api/alunos/<id>/
DELETE: /api/alunos/<id>/
```

Para os métodos POST, PUT e PATCH, o modelo de aluno esperado é o que se segue abaixo:

```
matricula = Integer
data_nascimento = Date
email = String
telefone = String
data_ingresso = Date
```

Exemplo:

```json
{
  "matricula": 123456789,
  "data_nascimento": "1998-02-01",
  "email": "123456789@uni.academico.br",
  "telefone": "(19)99999-9999",
  "data_ingresso": "2023-03-05"
}
```

O mesmo modelo é utilizado no retorno dos alunos para as requisições GET, porém com o acréscimo do atributo `id`.

## Templates

Os templates da aplicação foram criados com base nos já disponibilizados durante os exemplos apresentados em aula, porém com algumas modificações. Estas páginas também não solicitam autenticação para que seja possível interagir com registros de alunos. Seguem as URLs mapeadas:

```
/
/criar
/editar/<id>
/excluir/<id>
```

## Docker

Caso seja necessária a disponibilização de uma imagem e container Docker, siga os passos mencionados no **Setup inicial** (o item 5 não é necessário) e execute a criação da imagem:

```
docker build -t <nome-da-imagem>:latest .
```

Em seguida, suba o container mapeando devidamente a porta:

```
docker run --name <nome-do-container> -p 8000:8000 -d <nome-da-imagem>:latest
```
