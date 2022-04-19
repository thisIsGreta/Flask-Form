from flask import Flask, render_template
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm, RecaptchaField

SECRET_KEY = "secret-string"
app = Flask(__name__)
app.config.from_object(__name__)


class CommentForm(FlaskForm):
    email = TextAreaField("Email", validators=[DataRequired()])
    password = TextAreaField("Password", validators=[DataRequired()])
    recaptcha = RecaptchaField()


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login(form=None):
    if form is None:
        form = CommentForm()
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
