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
        url, getter, parser = factory.get_source(), factory.get_receiver(), factory.get_parser()
        raw_data = getter(url).get()
        result = parser(raw_data).parse()
        if result:
            return result


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run('0.0.0.0')
