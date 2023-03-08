from flask_app.config.mysqlconnection import connectToMySQL
from .author_model import Author




class Book:
    
    db= "books_schema"

    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # CREATE
    @classmethod
    def save(cls, data):
        query = """INSERT INTO books (title, num_of_pages)
                VALUES ( %(title)s, %(num_of_pages)s )"""
        return connectToMySQL(cls.db).query_db(query,data)
    
    # READ (one)
    @classmethod
    def show_one_book(cls, id):
        query = "SELECT * FROM books WHERE id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query, {'id': id})
        return cls(results[0])

    # READ (all)
    @classmethod
    def all_books(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL(cls.db).query_db(query)
        books = []

        for book in results:
            books.append( cls(book) )
        return books
    
    @classmethod
    def book_by_id(cls, data):
        # LEFT JOIN the 2 tables with the favorites table with book_id and author_id
        query = """SELECT * from books
                LEFT JOIN favorites ON books.id = favorites.book_id 
                LEFT JOIN authors ON authors.id = favorites.author_id
                WHERE books.id = %(id)s"""
        results = connectToMySQL(cls.db).query_db(query, data)
        one_book = cls (results[0])

        for book in results:
            #check if book has no favorited author
            if book['authors.id'] == None:
                break
            data = {
                'id': book['authors.id'],
                'name': book['name'],
                'created_at': book ['authors.created_at'],
                'updated_at': book ['authors.updated_at']
            }
            book.authors_who_favorited.append(author.Author(data))
            return one_book
        
        @classmethod
        def unfavorited_books(cls,data):
            query= """SELECT * FROM books WHERE books.id NOT IN 
                    (SELECT book_id FROM favorites
                    WHERE author_id = %(id)s );"""
            results = connectToMySQL(cls.db).query_db(query, data)
            all_books = []
            for book in results:
                all_books.append(cls(book))
            print (all_books)
            return all_books


