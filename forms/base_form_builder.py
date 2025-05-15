from wtforms import SelectField, StringField, PasswordField, Form
from wtforms.validators import DataRequired
from abc import ABC, abstractmethod


#This is the product, only a generic product, than allow add more fields.
#In this concrete context is for add a text field, and a select field
class BaseForm():

    def __init__(self):
        self.fields={}
    
    def add_text_field(self,name,**kwargs):
        self.fields[name] = StringField(name,validators=[DataRequired()],**kwargs)
        return self
    
    def add_select_field(self,name,unique_choices):
        self.fields[name] = SelectField(name,choices=unique_choices)
        return self

    def build(self):
        return type('DynamicForm',(Form,),self.fields)

#This is the interface from create the concret builders
class Builder(ABC):

    @abstractmethod
    def product():
        pass

#This is the concrete builder
class LoginBuilder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._product = BaseForm()
    
    @property
    def product(self):
        product = self._product
        self.reset()
        return product
    
    def username_build(self):
        self._product.add_text_field("username")

    def lastname_build(self):
        self._product.add_text_field("lastname")

    def country_build(self):
        self._product.add_text_field("country","country")
    
    def selection_any_build(self,unique_choices):
        self._product.add_select_field("selection",unique_choices)

class QuestionaryForm(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._product = BaseForm()
    
    @property
    def product(self):
        product = self._product
        self.reset()
        return product
    
    def Questions_one_to_ten(self):
        (self._product
         .add_select_field("QUESTION_A",unique_choices=[i +1 for i in range(10) ])
         .add_select_field("QUESTION_B",unique_choices=[i +1 for i in range(10) ])
         .add_select_field("QUESTION_C",unique_choices=[i +1 for i in range(10) ])
         .add_select_field("QUESTION_D",unique_choices=[i +1 for i in range(10) ])
         .add_select_field("QUESTION_E",unique_choices=[i +1 for i in range(10) ])
         .add_select_field("QUESTION_F",unique_choices=[i +1 for i in range(10) ])
         .add_select_field("QUESTION_G",unique_choices=[i +1 for i in range(10) ])
         .add_select_field("QUESTION_H",unique_choices=[i +1 for i in range(10) ])
         .add_select_field("QUESTION_I",unique_choices=[i +1 for i in range(10) ])
         .add_select_field("QUESTION_J",unique_choices=[i +1 for i in range(10) ])
         .add_select_field("QUESTION_K",unique_choices=[i +1 for i in range(10) ])
         .add_select_field("QUESTION_L",unique_choices=[i +1 for i in range(10) ])
         .add_select_field("QUESTION_M",unique_choices=[i +1 for i in range(10) ]))
        
    def Questions_zero_to_one(self):
        (self._product
         .add_select_field("QUESTION_O",unique_choices=[i for i in range(2)])
         .add_select_field("QUESTION_P",unique_choices=[i for i in range(2)])
         .add_select_field("QUESTION_Q",unique_choices=[i for i in range(2)])
         .add_select_field("QUESTION_R",unique_choices=[i for i in range(2)])
         .add_select_field("QUESTION_S",unique_choices=[i for i in range(2)])
         .add_select_field("QUESTION_T",unique_choices=[i for i in range(2)])
         .add_select_field("QUESTION_U",unique_choices=[i for i in range(2)]))

    def Questions_zero_to_hundred(self):
        (self._product
         .add_select_field("QUESTION_V",unique_choices=[0,25,50,100]))

    def Company_name(self):
        (self._product
         .add_text_field("TYPE"))       

class Director:

    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder
    
    @builder.setter
    def builder(self,builder_generic:Builder):
        self._builder = builder_generic
    
    def questionary_form(self):
        self._builder.Questions_one_to_ten()
        self._builder.Questions_zero_to_one()
        self._builder.Questions_zero_to_hundred()
        self._builder.Company_name()
        

    def admin_form(self):
        self._builder.username_build()
        self._builder.lastname_build()
        



