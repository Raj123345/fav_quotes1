#from flask import Flask,render_template
from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:Raj@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://kqqvmagdfxhmjn:d495f97c38dc48c45434282a7bf1991c3cc5b7f3df3b14a95bb90666a400a6e1@ec2-52-19-96-181.eu-west-1.compute.amazonaws.com:5432/d75vkqt6mdak25'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class Favquotes(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    author=db.Column(db.String(30))
    quote=db.Column(db.String(2000))


@app.route('/')
def index():
    result=Favquotes.query.all()
    #return render_template('index.html')
    return render_template('index.html',result=result)


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process', methods=['POST'])
def process():
    author=request.form['author']
    quote=request.form['quote']
    quotedata=Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))
