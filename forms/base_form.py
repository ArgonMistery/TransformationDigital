from wtforms import StringField, PasswordField, Form , BooleanField
from wtforms.validators import DataRequired
from abc import ABC, abstractmethod
from typing import Any

class FormBuilder():
    def __init__(self):
        self.form_class = type('Dinamic_Form',(Form,),{})
    
    def add_username(self):
        self.form_class.username=StringField('username',validators=[DataRequired()])

    def add_password(self):
        self.form_class.password=PasswordField('password',validators=[DataRequired()])
    

class FormAdmin(FormBuilder):
    def add_admin_toggle(self):
        self.form_class.adming_toggle=BooleanField('Is Admin?')

class ClientForm(FormBuilder):
    def add_address(self):
        self.form_class.address=StringField('Address')    


class FormDirector():
    def __init__(self):
        self._builder=None

    @property
    def builder(self):
        return self._builder
    
    @builder.setter
    def builder(self,builder:FormBuilder):
        self._builder=builder
    
    def build_admin_form(self):
        self._builder.add_password()
        self._builder.add_admin_toggle()
    
    def build_client_form(self):
        self._builder.add_password()
        self._builder.add_username()
        self._builder.add_address()

    def get_form(self):
        return self._builder.form_class()


class FactoryForm(ABC):
    @abstractmethod
    def create():
        pass

class FactoryConcreteForms(FactoryForm):
    def __init__(self,name):
        self.name = name
    
    def create(self):
        
        if self.name == "Admin":
            DirectorConcrete = FormDirector()
            BuilderConcrete = FormAdmin()
            DirectorConcrete.builder = BuilderConcrete
            DirectorConcrete.build_admin_form()
            return DirectorConcrete.get_form()
        
        if self.name == "Client":
            DirectorConcrete = FormDirector()
            BuilderConcrete = ClientForm()
            DirectorConcrete.builder = BuilderConcrete
            DirectorConcrete.build_client_form()
            return DirectorConcrete.get_form()
        
        else:
            raise ValueError(f"Unknow form type: {self.name}")
        



        