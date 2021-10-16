from flask import Flask
from app.source.routes.product import product

app = Flask(__name__)

app.register_blueprint(product)

if __name__ == '__main__':
    app.run(host='localhost', port=5600)
