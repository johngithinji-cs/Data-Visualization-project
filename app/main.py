#!/usr/bin/env python3
"""Application routes"""

from flask import Blueprint, render_template
from flask_login import login_required, current_user


main = Blueprint('main', __name__)


# Other routes
@main.route('/', strict_slashes=False)
def index():
  """Route to home page"""
  return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
  """
  Route to individual profile page
  """
  # ---Should load user files for individual user from database---
  return render_template('profile.html', name=current_user.name)