import os

from app.app import create_app
if __name__ == '___main___':
    app = create_app()
    app.run(port=8000, debug = True)

if __name__ == '__main__':
	app.debug = True
	app.run()
