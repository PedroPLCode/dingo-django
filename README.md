# Dingo.py django practice

[Live link to Replit](https://8ea9a1e5-9a55-47e6-a1f3-c9632a002dc8-00-1udg219vet2qx.spock.replit.dev/)

## /posts_api/v1/
## /books_api/v1/

## Maths:

```shell
GET /maths
GET /maths/add/a/b
GET /maths/sub/a/b
GET /maths/mul/a/b
GET /maths/div/a/b
```

## Greetings:
```shell
GET /greetings
GET /greetings/name

```

## Posts:
```shell
GET & PUT /posts/list
GET & PUT /posts/details/<id>
GET & PUT /posts/authors
GET & PUT /posts/authordetails/<id>

```

## Books:
```shell
GET /books/books
GET /books/tag/<str:tag>/
GET /books/book/<int:id>
GET /books/authors/<id>
GET /books/author/<int:id>
GET /books/books/author/<str:name>
GET /books/borrows/<str:username>
GET & POST /books/borrow/<int:id>

```