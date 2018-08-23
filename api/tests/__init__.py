from flask import Flask

app = Flask(__name__)

from app import routes
if __name__ == '___main___':
    app = create_app()
    app.run(port=8000, debug = True)
