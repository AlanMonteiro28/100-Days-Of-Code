from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"

db.init_app(app)

class Book(db.Model):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.id))
    all_books = result.scalars()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        with app.app_context():
            new_book = Book(
                title=request.form['title'],
                author=request.form['author'],
                rating=request.form['rating']
                )
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if request.method == 'POST':
        book_to_update = Book.query.filter_by(id=id).first()
        book_to_update.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    book_selected = Book.query.filter_by(id=id).first()
    return render_template("edit.html", book=book_selected)



if __name__ == "__main__":
    app.run(debug=True)

