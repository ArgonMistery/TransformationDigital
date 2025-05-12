
from flask import Flask,render_template,request,redirect,url_for
from config import ConfigObject
from forms import base_form_builder
    

app=Flask(__name__)


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
    builder_generic=base_form_builder.QuestionaryForm()
    director=base_form_builder.Director()
    director.builder=builder_generic
    director.questionary_form()
    dynamic_form=builder_generic.product.build()
    form=dynamic_form()
    return(render_template('questionary_form.html',form=form))

        

if __name__=='__main__':
    app.config.from_object(ConfigObject)
    app.run()