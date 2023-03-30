#!/usr/bin/env python3
"""Application routes"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .db import db
from .models.user import User
import os
from os.path import join, dirname, realpath
from flask import current_app
import mysql.connector

import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mpld3

import io


auth = Blueprint('auth', __name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="analyst",
    password="project",
    database="user_data"
)

uploads_dir = os.path.join(auth.root_path, 'fileUploads')
os.makedirs(uploads_dir, exist_ok=True)


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

@auth.route('/upload', strict_slashes=False)
def upload():
    """Route to upload file page."""
    return render_template('upload.html')

@auth.route('/upload', methods=['POST'])
def uploadFile():
    """Function to save uploaded file. """
    global file_path
    uploaded_file = request.files['file']
    global file_name
    file_name = uploaded_file.filename
    if file_name != '':
        file_path = os.path.join(uploads_dir,
                                 uploaded_file.filename)
        uploaded_file.save(file_path)
        return redirect(url_for('auth.visualize'))

@auth.route('/demo', strict_slashes=False)
def demo_app():
    """Route to upload file page."""
    return render_template('demo.html')

@auth.route('/dashboard', strict_slashes=False)
def visualize():
    """Route to visualization page."""
    csvData = pd.read_csv(file_path, header=0)
    columns = csvData.columns
    return render_template('visualize.html', columns=columns, fname=file_name)

@auth.route('/display')
def display():
    """Route to display the visualization."""
    csvData = pd.read_csv(file_path, header=0)
    x = request.form.get('x')
    y = request.form.get('y')
    chart = request.form.get('chart')
    return render_template('plot.html', x=x, y=y, chart=chart)

def create_figure(data, x, y, chart):
    """Function to draw the plots"""
    fig, ax = plt.subplots(figsize = (6,4))
    fig.patch.set_facecolor('#E8E5DA')

    if chart == 'Bar':
        ax.bar(data["x"], data["y"], marker="*", color = "#304C89")
    elif chart == 'Line':
        ax.plot(data["x"], data["y"], marker="*", color = "#304C89")
    elif chart == 'Scatter':
        ax.scatter(data["x"], data["y"], marker="*", color = "#304C89")
    elif chart == 'Histogram':
        ax.hist(data["x"], data["y"], marker="*", color = "#304C89")

    return fig
   # img_path = os.path.join(uploads_dir, "my_plot.png")
    #fig.savefig(img_path)

@auth.route('/logout')
@login_required
def logout():
  """Route to log out"""
  logout_user()
  return redirect(url_for('main.index'))
