from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello, World!"

    @app.route('/bye')
    def goodbye():
        return "<p>Goodbye, World!</p>"


    return app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)