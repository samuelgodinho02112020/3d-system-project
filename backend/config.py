import os
from webapp import app

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:@127.0.0.1/interview_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "SAMUEL"