# Dingo.py django practice

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