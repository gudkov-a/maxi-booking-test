from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_currency')
def get_currency():
    return f'currency info, at {datetime.datetime.now().strftime("%H:%M")}'


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run('0.0.0.0')
