import os
import signal
import uuid

from flask import Flask
from flask import render_template, request

from ImageNet.network import main
from torchvision import models
# import ImageNet

# APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_ROOT = os.getcwd()

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public'
    return r


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/detector', methods=['GET', 'POST'])
def detector():
    if request.method == 'POST':
        target = os.path.join(APP_ROOT, 'static/upload_img/')
        print(target)

        if 'file' not in request.files:
            print('file was not uploaded')

            return render_template('detector.html', is_post=False)

        for file in request.files.getlist('file'):
            filename = str(uuid.uuid4()) + '_' + file.filename

            destination = ''.join([target, filename])
            print('destination:', destination)

            file.save(destination)

            main(destination, model)

            path_detect_img = 'detected_img/' + filename
            path_upload_img = 'upload_img/' + filename

            return render_template('detector.html', is_post=True,
                                    path_detect_img=path_detect_img,
                                    path_upload_img=path_upload_img)
    else:
        return render_template('detector.html', is_post=False)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=5000)
