from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)



    @app.route("/", methods=["GET", "POST"])
    def index():
        image_url = None
        if request.method == "POST":
            image_url = request.form.get("image_url")
        return render_template("index.html", image_url=image_url)


    return app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)