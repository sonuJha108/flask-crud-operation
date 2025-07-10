from flask import Flask,render_template,request,redirect
from models.model import db,StudentModels


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_request
def create_table():
    db.create_all()


@app.route('/create',methods = ['GET','POST'])
def create():
    if request.method == 'GET': 
        return render_template('create.html')


# app.run(host='localhost',port=5000)

if __name__ == "__main__":
    app.run(debug=True)