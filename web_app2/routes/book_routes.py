from flask import Blueprint, jsonify, request, render_template, redirect #, flash

from web_app2.routes.models import Book, parse_records, db, migrate
book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books.json")
def list_books():
    books = [
       {"id": 1, "title": "Book 1"},
       {"id": 2, "title": "Book 2"},
       {"id": 3, "title": "Book 3"},]
    #book_records = Book.query.all()
    #print(book_records)
    #books = parsed_records(book_records)
    return jsonify(books)

@book_routes.route("/books")
def list_books_for_humans():
    books = [
        {"id": 1, "title": "Book 1"},
       	{"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},]	    
    book_records = Book.query.all()
    print(book_records)
    return render_template("books.html", message="Here's some books", books=book_records)

@book_routes.route("/books/new")
def new_book():
    return render_template("new_book.html")

@book_routes.route("/books/create", methods=["POST"])
def create_book():
    print("FORM DATA:", dict(request.form))
    
    new_book = Book(title=request.form["book_title"], author_id=request.form["author_name"])
    db.session.add(new_book)
    db.session.commit()
    #return jsonify({
     #   "message": "BOOK CREATED OK (TODO)",
      #  "book": dict(request.form)})
    return redirect(f"/books")

    