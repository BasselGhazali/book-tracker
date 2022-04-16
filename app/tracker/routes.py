from app.tracker import main
from app import db
from app.tracker.models import Book, Publication
from app.tracker.forms import EditBookForm, CreateBookForm, AddBookForm
from flask import render_template, flash, request, redirect, url_for
from flask_login import login_required


@main.route('/')
def display_books():
    books = Book.query.all()
    return render_template('home.html', books=books)


@main.route('/display/publisher/<publisher_id>')
def display_publisher(publisher_id):
    publisher = Publication.query.filter_by(id=publisher_id).first()
    publisher_books = Book.query.filter_by(pub_id=publisher.id).all()

    return render_template('publisher.html', publisher=publisher, publisher_books=publisher_books)


@main.route('/delete/<book_id>', methods=['GET', 'POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get(book_id)
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        flash('{} has been deleted').format(book)
        return redirect(url_for('main.display_books'))
    return render_template('delete_book.html', book=book, book_id=book.id)


@main.route('/edit/book/<book_id>', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    book = Book.query.get(book_id)
    form = EditBookForm(obj=book)

    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.price = form.price.data
        book.image = form.image.data

        db.session.add(book)
        db.session.commit()

        flash('Book changed successfully')
        return redirect(url_for('main.display_books'))

    return render_template('edit_book.html', form=form)


# @main.route('/create/book/<pub_id>', methods=['GET', 'POST'])
# @login_required
# def create_book(pub_id):
#     form = CreateBookForm()
#     pub_form = AddBookForm()
#
#     pub_form.pub_id.data = pub_id
#
#     if form.validate_on_submit():
#         book = Book(title=form.title.data,
#                     author=form.author.data,
#                     image=form.image.data,
#                     tags=form.tags.data,
#                     vendors=form.vendors.data,
#                     genre=form.genre.data)
#
#         db.session.add(book)
#         db.session.commit
#
#         flash('Book added successfully')
#         return redirect(url_for('main.display_publisher'), publisher_id=pub_id)
#
#     return render_template(url_for('create_book.html', form=form, pub_id=pub_id))
