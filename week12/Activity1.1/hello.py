from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello, World!"

    @app.route('/bye')
    def goodbye():
        return "<p>Goodbye, World!</p>"

    @app.route('/user/<username>')
    def user_profile(username):
        return f"<p>{username} is learning Flask.</p>"

    return app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)