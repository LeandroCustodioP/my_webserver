from flask import current_app as app, render_template_string


@app.route('/')
def home():
    return render_template_string("home.html")


@app.route('/test')
def test():
    return "this is a test"
