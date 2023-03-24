#!/usr/bin/env python3
"""Application routes"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .db import db
from .models.user import User


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
  """Route to login page"""
  return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
  """Route for actually logging in"""
  email = request.form.get('email')
  password = request.form.get('password')
  remember = False
  if request.form.get('remember'):
    remember = True

  user = User.query.filter_by(email=email).first()
  if not user or not check_password_hash(user.password, password):
    flash('Please check your login details and try again.')
    return redirect(url_for('auth.login'))

  login_user(user, remember=remember)
  return redirect(url_for('main.profile'))

@auth.route('/signup', strict_slashes=False)
def signup():
  """Route to signup page"""
  return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
  """Route to register user"""
  email = request.form.get('email')
  name = request.form.get('name')
  password = request.form.get('password')

  user = User.query.filter_by(email=email).first()
  if user:
    flash('Email address already exists')
    return redirect(url_for('auth.signup'))
  new_user = User(email=email, name=name,
                  password=generate_password_hash(password, method='sha256'))

  db.session.add(new_user)
  db.session.commit()

  return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
  """Route to log out"""
  logout_user()
  return redirect(url_for('main.index'))