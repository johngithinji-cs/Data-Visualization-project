#!/usr/bin/env python3
"""
Defines auth blueprint which handles everything auth related
"""
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User
from . import db


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    """route to login page"""
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    """route for actually logging in"""
    email = request.form.get('email')
    password = request.form.get('password')
    remember = False
    if request.form.get('remember'):
        remember = True

    user = User.query.filter_by(emai=email).first()
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    """route to signup page"""
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    """route for actually signing up"""
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # check if user exists and if true, redirect to signup page again
    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email address already esists')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, name=name,
                    password=generate_password_hash(password, method='sha256'))

    # add new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))



@auth.route('/logout')
@login_required
def logout():
    """route to log out"""
    logout_user()
    return redirect(url_for('main.index'))