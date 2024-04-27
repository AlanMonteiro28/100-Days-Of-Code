from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5

#use a real email and pass
ADM_EMAIL = 'admin@email.com'
ADM_PASS =  '12345678'

class LoginForm(FlaskForm):
    email = StringField(label='Email', 
                        validators=[
                            DataRequired(),
                            Email(message='Not valid')]
                        )
    
    password = PasswordField(label='Password', 
                            validators=[
                                DataRequired(),
                                Length(min=8, message='Little short for password')]
                             )
    
    submit = SubmitField(label='Log In')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'atumalaca'

bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == ADM_EMAIL and login_form.password.data == ADM_PASS:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)



if __name__ == '__main__':
    app.run(debug=True)
