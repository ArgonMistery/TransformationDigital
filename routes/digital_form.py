from flask import Blueprint, render_template, request, redirect, g ,url_for
from orm.repository import RepositoryForms
from orm.models import Questionary as QuestionaryModel
from orm.orm import Questionary as QuestionaryTable 
from orm.orm import StartMappers,StandardMapper
from orm.connections import resumen_url
from forms import base_form_builder
    

digital_form = Blueprint("digitalform",__name__, url_prefix="/digital")

@digital_form.route("/form", methods = ["GET","POST"])
def digital_maturity_form():
    #Builder the form with the builder pattern
    builder_generic = base_form_builder.QuestionaryForm()
    director = base_form_builder.Director()
    director.builder = builder_generic
    director.questionary_form()
    dynamic_form = builder_generic.product.build()
    form=dynamic_form()
    
    if request.method == "POST":

        form_data = dynamic_form(request.form)
        if form_data.validate():
            data_dict = form_data.data
            QuestionaryData = QuestionaryModel(**data_dict)
            g.repositorio_general.add(QuestionaryData)
        
        return redirect(request.url)
        
    return(render_template('forms_production/questionary_form_proto.html',form=form))