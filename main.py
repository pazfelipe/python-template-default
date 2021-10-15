from flask import Flask
from app.source.services.product import save, findAll

app = Flask(__name__)


@app.route('/')
def index():
    products = findAll()
    return products


if __name__ == '__main__':
    app.run(host='localhost', port=5600)
