
from flask import Flask,g
from routes.digital_form import digital_form
from config import ConfigObject

from orm.orm import StartMappers,StandardMapper
from orm.connections import resumen_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm.models import Questionary as QuestionaryModel
from orm.orm import Questionary as QuestionaryTable 
from orm.repository import RepositoryForms

#This is very important in the code, becouse we need to map the model with the table only one time
StartMappers(QuestionaryModel,QuestionaryTable)


app=Flask(__name__)
@app.before_request
def before_connections():
    engine=create_engine(resumen_url)
    Session_global=sessionmaker(bind=engine)
    g.session_global=Session_global()
    g.repositorio_general=RepositoryForms(g.session_global)

@app.route("/")
def home():
    return "<h1> Hello world </h1>"

@app.after_request
def shutdown_session(response):
    if hasattr(g,"session_global"):
        g.session_global.close()
    return response

app.register_blueprint(digital_form)

if __name__=='__main__':
    app.config.from_object(ConfigObject)
    app.run()