from flask_app.config.mysqlconnection import connectToMySQL
# from .book_model import Book



class Author:
    
    db= "books_schema"

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []


    # CREATE
    @classmethod
    def save(cls, data):
        query = """INSERT INTO authors (name)
                VALUES ( %(name)s )"""
        return connectToMySQL(cls.db).query_db(query,data)

    # READ (one)
    @classmethod
    def show_one_author(cls, id):
        query = "SELECT * FROM authors WHERE id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query, {'id': id})
        return cls(results[0])
    
    # READ (all)
    @classmethod
    def all_authors(cls):
        query = "SELECT * FROM authors"
        results = connectToMySQL(cls.db).query_db(query)
        authors = []

        for author in results:
            authors.append( cls(author) )
        return authors

    # filters out the authors with no favorites using 'NOT IN'
    @classmethod
    def unfavorited_authors(cls,data):
        query = """SELECT * FROM authors
                WHERE author.id NOT IN
                ( SELECT author_id FROM favorites
                WHERE book_id = %(id)s );"""
        authors = []
        results = connectToMySQL(cls.db).query_db(query, data)

        for author in results:
            authors.append(cls(author))
        return authors
    
    @classmethod
    def add_favorite(cls,data):
        query = """INSERT INTO favorites (author_id, book_id) 
                VALUES (%(author_id)s, %(book_id)s);"""
        results = connectToMySQL(cls.db).query_db(query, data)
        return results



    # @classmethod
    # def get_author_favorites(cls, data):
    #     query = """SELECT * FROM authors
    #     LEFT JOIN books ON authors.book_id = dojos.id
    #     WHERE dojos.id = %(id)s"""
    #     results = connectToMySQL(cls.DB).query_db(query, data)
    #     dojo = cls (results [0])
        
    #     for row_from_db in results:

    #         ninja_info = {
    #             "id" : row_from_db['ninjas.id'],
    #             "first_name": row_from_db['first_name'],
    #             "last_name": row_from_db['last_name'],
    #             "age": row_from_db['age'],
    #             "created_at": row_from_db['ninjas.created_at'],
    #             "updated_at": row_from_db['ninjas.updated_at']
    #         }
    #         dojo.ninjas.append( Ninja(ninja_info))
    #     return dojo