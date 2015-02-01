from flask import render_template, redirect, request, url_for, flash

from . import app, db

from forms import LoginForm, PostForm
from models import User, Post
from flask.ext.login import login_user, logout_user, login_required, current_user

@app.route('/')
def index():
	post_list = Post.query.order_by(Post.timestamp.desc()).all()
	return render_template('index.html', posts=post_list)

@app.route('/user/<username>')
def user(username):
	user = User.query.filter_by(username=username).first_or_404()
	post_list = user.posts.order_by(Post.timestamp.desc()).all()
	return render_template('user.html', user=user, posts=post_list)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is None or not user.verify_password(form.password.data):
			flash('Invalid email or password')
			return redirect(url_for('login'))
		login_user (user, form.remember_me.data)
		return redirect(request.args.get('next') or url_for('index'))
	return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out')
	return redirect(url_for('index'))

@app.route('/new', methods=['GET', 'POST'])
@login_required
def new_post():
	form = PostForm()
	if form.validate_on_submit():
		post = Post(title=form.title.data,
					body=form.body.data,
					author=current_user)
		db.session.add(post)
		db.session.commit()
		flash('The post was added sucessfully')
		return redirect(url_for('index'))
	return render_template('edit_post.html', form=form)