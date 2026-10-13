from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/tables-basic')
def basic_tables():
    return render_template('tables-basic.html')



app.run(debug=True)





