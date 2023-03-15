#!/usr/bin/env python3
"""Defines main blueprint which handles regular routes and
protected pages
"""

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db


main = Blueprint('main', __name__)

@main.route('/')
def index():
    """route to home page"""
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    """route to individual profile page"""
    return render_template('profile.html', name=current_user.name)