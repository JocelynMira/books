from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author_model import Author
from flask_app.models.book_model import Book


# route to main page new author
@app.route('/')
def authors_index():
    return render_template('add_author.html', all_authors = Author.all_authors())

# CREATE
@app.route('/new_author', methods=['POST'])
def new_author():
    print(request.form)
    data = {
        'name' : request.form['name']
    }
    author_id = Author.save(data)
    return redirect ('/')

# READ 
@app.route('/all_authors')
def authors():
    authors = Author.all_authors() 
    return render_template ('add_author.html', all_authors = authors)

@app.route('/one_author/<int:id>')
def get_one_author(id):
    data = {
        'id': id
    }
    return render_template ('author_show.html', author = Author.show_one_author(data), unfavorited_books = Book.unfavorited_books(data) )

