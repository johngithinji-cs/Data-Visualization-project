#!/usr/bin/env python3
"""Application routes"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
import dash
from dash import html, dcc

import pandas as pd


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


@main.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    """
    Route to upload a file
    """
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # ---Should save file to database for individual user---
        flash('File uploaded successfully')
        return redirect(url_for('main.profile'))
    return render_template('upload.html')


@main.route('/visualize', methods=['GET', 'POST'])
@login_required
def visualize():
    """
    Route to visualize uploaded data using Dash
    """
    if request.method == 'POST':
        # check if the post request has the file and visualization type parts
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        if 'visualization_type' not in request.form:
            flash('No visualization type selected')
            return redirect(request.url)
        file = request.files['file']
        visualization_type = request.form['visualization_type']

        # Read file data into a pandas DataFrame
        df = pd.read_csv(file, encoding="cp1252")

        # Check if the visualization_type provided by the user is a valid column name in the df DataFrame
        if visualization_type not in df.columns:
            flash('Invalid visualization type selected')
            return redirect(request.url)

        # Perform data visualization with Dash
        app = dash.Dash(__name__)
        app.layout = html.Div(children=[
            html.H1(children='Data Visualization'),
            dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': df.index, 'y': df[visualization_type], 'type': 'line', 'name': visualization_type},
                    ],
                    'layout': {
                        'title': visualization_type
                    }
                }
            )
        ])
        return app.run_server()

    return render_template('visualize.html')
