from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import Required, Length, Email

class LoginForm(Form):
	email = StringField('Email', validators=[Required(), Length(1,64), Email()])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('Keep me logged in')
	submit = SubmitField('Log In')

class PostForm(Form):
	title = StringField('Title', validators=[Required(), Length(1,128)])
	body = TextAreaField()
	submit = SubmitField('Submit')