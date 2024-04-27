from flask import Flask, render_template, request
from post import Post
from send_mail import SendMail

app = Flask(__name__)

all_posts = Post().get_posts()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<blog_id>')
def post(blog_id):
    chosen_post = all_posts[int(blog_id)-1]
    chosen_image = Post().get_image(id=int(blog_id)-1)
    return render_template("post.html", requested_post=chosen_post, requested_img=chosen_image)

@app.route('/about')
def get_about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def receive_data():
    h1_text = None
    if request.method == 'POST':
        data = request.form
        name = data['name']
        email = data['email']
        phone = data['phone']
        message = data['message']
        send_email = SendMail().sendmail(name, email, phone, message)
        h1_text = f"Successfully sent your message!"
    return render_template("contact.html", h1_text=h1_text)


if __name__ == "__main__":
    app.run(debug=True)
