from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.book_model import Book
from flask_app.models.author_model import Author


# sent from add_author page route to new_book
@app.route('/books')
def books_index():
    return render_template('add_book.html', all_books = Book.all_books())

# CREATE
@app.route('/new_book', methods=['POST'])
def new_book():
    print(request.form)
    data = {
        'title' : request.form['title'],
        'num_of_pages' : request.form['num_of_pages']
    }
    book_id = Book.save(data)
    return redirect ('/books')

# READ 
@app.route('/all_books')
def books():
    books = Book.all_books() 
    return render_template ('add_book.html', all_books = books)

@app.route('/one_book/<int:id>')
def get_one_book(id):
    data = {
        'id': id
    }
    return render_template ('show_book.html', book = Book.book_by_id(data),unfavorited_authors= Author.unfavorited_authors(data) )

@app.route('/join_author', methods=['POST'])
def join_author():
    data = {
        'author_id': request.form ['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect (f"/book/{request.form['book_id']}")