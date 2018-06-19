import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import csv
import pandas as pd

UPLOAD_FOLDER = '../uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__, template_folder='../templates')
app.secret_key = "abcd1234"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        name = request.form["name"]
        category = request.form["category"]

        main_data = pd.read_csv('../data/data.csv')
        x = [main_data.iloc[x, 0] for x in range(main_data['name'].size) if main_data.iloc[x, 1] == category]
        print('Users in the category: ',category,x)
        with open('data.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([name, category])

        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for('upload_file'))
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('upload_file'))
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], name + '.pdf'))
            return redirect(url_for('upload_file'))
    return render_template('file_upload.html')


if __name__ == '__main__':
    app.run(debug=True)
