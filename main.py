from flask import Flask, render_template, request, redirect, flash, send_from_directory
app = Flask(__name__)

import os

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

try:
    from PIL import Image
    import PIL.ImageOps
except:
    print("Make sure to pip install Pillow")

import fileSearch
import fileSort
import config


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/download/', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        keywords = request.form['text']
        refinewords = request.form['checkbox']
        path = 'static'
        results = fileSearch.keyword_search(path, keywords)
        info = fileSearch.fileInfo(results)
        results = fileSearch.refineSearch(results, refinewords)
        return render_template('downloadResults.html', keywords=keywords, results=results, info=info)
    return render_template('downloadResults.html')

@app.route('/<filename>')
def get_file(filename):
    return send_from_directory('static',filename)


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        filename = secure_filename(file.filename)
        # Create a path to the image in the upload folder, save the upload
        # file to this path
        uploaded=(os.path.join('static', filename))
        file.save(uploaded)
        name = request.form['filename']
        descript = request.form['description']
        age = request.form['age-group']
        subject = request.form['subject']
        country = request.form['country']
        
        fileSort.addtoFile(uploaded, name, descript, age, subject, country)
        return render_template('upload.html')
    return render_template('upload.html')

@app.route('/fullfile/')
def fullfile():
    global results
    global info
    if request.method == 'POST':
        keywords = request.form['text']
        path = 'static'
        results = fileSearch.keyword_search(path, keywords)
        info = fileSearch.fileInfo(results)
        return render_template('downloadResults.html', keywords=keywords, results=results, info=info)
    return render_template('download.html')

@app.route('/blog/')
def blog():
    return render_template("blog.html")

@app.route('/blogpost1/')
def blogpost1():
    return render_template("blogpost1.html")

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template("index.html")
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)


