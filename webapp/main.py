# main.py

from flask import Blueprint, render_template, request, session, redirect, url_for, current_app

from flask_login import login_required, current_user

import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/upload',methods = ['POST', 'GET'] )
@login_required
def upload():
    
    if request.method == "POST":

        if request.files:

            file = request.files["file"]            
            print("------------------>>>>>", file.filename)
            #print("------------------>>>>>", current_app.config["FILE_UPLOAD_BASE"])
            print("------------------>>>>>", current_user.home)
            dir_path = os.path.join(current_app.config["FILE_UPLOAD_BASE"], current_user.home)
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
            filename = os.path.basename(file.filename)
            file_path = os.path.join(dir_path, filename)
            file.save(file_path)
            return redirect(request.url + "?uploadedfile=" + filename)    
    
    return render_template('upload.html', name=current_user.name)