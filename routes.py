from bottle import Bottle, jinja2_template as template

app = Bottle()


@app.get("/static/<file_path:path>")
def index(file_path):
    return static_file(file_path, root="./static")


@app.route('/add')
def add():
    return template('add.html', title="テンプレートのテストだよ")

