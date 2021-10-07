SELECT * FROM books
JOIN favorites ON books.id = favorites.book_id
JOIN authors ON authors.id = favorites.author_id
WHERE books.id = 5;