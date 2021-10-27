from flask import Flask
from flask_restx import Resource, Api
from todo import Todo

app = Flask(__name__)
api = Api(
    app,
    version='0.1',
    title="API",
    description="API",
    terms_url="/",
    contact="kmbm0916.biz@gmail.com",
    license="MIT"
)

api.add_namespace(Todo, '/todos')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)