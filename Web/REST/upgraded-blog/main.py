from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['CKEDITOR_PKG_TYPE'] = 'basic'
ckeditor = CKEditor(app)
Bootstrap5(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()

# Add Form
class CreatePostForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    author = StringField(label="Your Name", validators=[DataRequired()])
    img_url = StringField(label="Blog Image URL", validators=[DataRequired()])
    body = CKEditorField(label="Body Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).order_by(BlogPost.id).all()
    return render_template("index.html", all_posts=posts)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = db.session.query(BlogPost).filter_by(id=post_id).first()
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["GET", "POST"])
def add_post():
    add_form = CreatePostForm()
    if add_form.validate_on_submit():
        new_post = BlogPost(
            title=add_form.title.data,
            subtitle=add_form.subtitle.data, 
            author=add_form.author.data,
            body=add_form.body.data,
            img_url=add_form.img_url.data,
            date=date.today().strftime("%B %d, %Y")
            )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=add_form)

# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post_selected = db.session.query(BlogPost).filter_by(id=post_id).first()
    edit_form = CreatePostForm(
        title=post_selected.title,
        subtitle=post_selected.subtitle,
        author=post_selected.author,
        body=post_selected.body,
        img_url=post_selected.img_url,
    )
    if edit_form.validate_on_submit():
        post_selected.title = edit_form.title.data
        post_selected.subtitle = edit_form.subtitle.data 
        post_selected.author = edit_form.author.data
        post_selected.body = edit_form.body.data
        post_selected.img_url = edit_form.img_url.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post_selected.id))
    
    return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route("/delete/<post_id>")
def delete_post(post_id):
    post_to_delete = db.session.query(BlogPost).filter_by(id=post_id).first()
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
