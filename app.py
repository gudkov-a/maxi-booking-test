from flask import Flask, render_template
from currency_modules.factories import JsonFactory, XMLFactory

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_currency')
def get_currency():
    for f in [JsonFactory, XMLFactory]:
        factory = f()
        url, receiver, parser = factory.get_source(), factory.get_receiver(), factory.get_parser()
        raw_data = receiver.get()
        result = parser.parse(raw_data)
        if result:
            return result


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run('0.0.0.0')
