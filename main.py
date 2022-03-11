from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Заготовка')


@app.route('/training/<prof>', methods=['GET', 'POST'])
def training(prof):
    if str(prof) in ['инженер', 'строитель']:
        print('ok')
        return render_template('ingener.html', title='Заготовка')
    else:
        return render_template('science.html', title='Заготовка')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
