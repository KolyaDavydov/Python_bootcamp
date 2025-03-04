import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'music/'
ALLOWED_EXTENSIONS = {'mp3', 'ogg', 'wav'}

HTML = '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    <p>
        Cписок загруженных аудиофайлов: <br>
    </p>
    '''

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return HTML + get_audio_files(UPLOAD_FOLDER)


@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


def get_audio_files(directory):
    audio_files = []
    for file in os.listdir(directory):
        if file.endswith('.mp3') or file.endswith('.wav'):
            audio_files.append(file)
    if not audio_files:
        return 'Загруженных файлов нет'
    else:
        return '<p class="audio">' + '<br>'.join(audio_files) + '</p>'
        # return audio_files


if __name__ == '__main__':
    app.run(port=8888)
