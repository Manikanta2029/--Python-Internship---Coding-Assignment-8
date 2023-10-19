import os
from flask import Flask, request, render_template, redirect, url_for
from pydub import AudioSegment
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'wav', 'mp3'}  # Specify allowed file extensions

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if a file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Main route for file upload and processing
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)

            # Process the uploaded audio file (e.g., convert to MP3)
            output_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'output.mp3')
            audio = AudioSegment.from_file(filename)
            audio.export(output_filename, format="mp3")

            return f'Processed audio saved as {output_filename}'

    return render_template('upload.html')

if __name__ == '__main__':
    app.run()
