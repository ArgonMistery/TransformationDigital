
from flask import Flask,render_template,request,redirect,url_for,g
from config import ConfigObject
from forms import base_form_builder
    
from orm.repository import RepositoryForms
from orm.models import Questionary as QuestionaryModel
from orm.orm import Questionary as QuestionaryTable 
from orm.orm import StartMappers,StandardMapper
from orm.connections import resumen_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#This is very important in the code, becouse we need to map the model with the table only one time

StartMappers(QuestionaryModel,QuestionaryTable)

app=Flask(__name__)


@app.before_request
def before_connections():
    engine=create_engine(resumen_url)
    Session_global=sessionmaker(bind=engine)
    g.session_global=Session_global()
    g.repositorio_general=RepositoryForms(g.session_global)


@app.route('/')
def home():
    """This function only redirect the main page"""
    return render_template('home.html')



@app.route('/form/<form_type>',methods=['GET','POST'])
def form_manager(form_type):
    if form_type == 'Admin':
        
        builder_generic=base_form_builder.LoginBuilder()
        director=base_form_builder.Director()
        director.builder=builder_generic
        director.admin_form()
        dynamic_form=builder_generic.product.build()
        form=dynamic_form()
        return(render_template('dynamic_admin_form.html',form=form))
    
@app.route('/digital_maturity_form',methods=['GET','POST'])
def digital_maturity_form():
    

    #Builder the form with the builder pattern
    builder_generic=base_form_builder.QuestionaryForm()
    director=base_form_builder.Director()
    director.builder=builder_generic
    director.questionary_form()
    dynamic_form=builder_generic.product.build()
    form=dynamic_form()

    if request.method == "POST":
        
        form_data=dynamic_form(request.form)
        if form_data.validate():
            data_dict=form_data.data
            QuestionaryData=QuestionaryModel(**data_dict)
            g.repositorio_general.add(QuestionaryData)
        
        return redirect(request.url)
        
    return(render_template('questionary_form.html',form=form))


@app.after_request
def shutdown_session(response):
    if hasattr(g,"session_global"):
        g.session_global.close()
    return response


if __name__=='__main__':
    app.config.from_object(ConfigObject)
    app.run()