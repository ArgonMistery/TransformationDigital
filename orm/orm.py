from sqlalchemy import Column,Integer,Table,MetaData,String
from sqlalchemy.orm import registry
from orm.models import Questionary

#This is a object than need all the tables
metadata=MetaData()
StandardMapper=registry()

Questionary=Table(
    "QUESTIONARY",
    metadata,
    Column("ID_GLOBAL",Integer(),primary_key=True,autoincrement=True),
    Column("TYPE",String()),
    Column("QUESTION_A",Integer()),
    Column("QUESTION_B",Integer()),
    Column("QUESTION_C",Integer()),
    Column("QUESTION_D",Integer()),
    Column("QUESTION_E",Integer()),
    Column("QUESTION_F",Integer()),
    Column("QUESTION_G",Integer()),
    Column("QUESTION_H",Integer()),
    Column("QUESTION_I",Integer()),
    Column("QUESTION_J",Integer()),
    Column("QUESTION_K",Integer()),
    Column("QUESTION_L",Integer()),
    Column("QUESTION_M",Integer()),
    Column("QUESTION_O",Integer()),
    Column("QUESTION_P",Integer()),
    Column("QUESTION_Q",Integer()),
    Column("QUESTION_R",Integer()),
    Column("QUESTION_S",Integer()),
    Column("QUESTION_T",Integer()),
    Column("QUESTION_U",Integer()),
    Column("QUESTION_V",Integer())
)

def StartMappers(DATA_CLASS_OBJECT:object,TABLE_OBJECT:object):
    Questionary_mapper=StandardMapper.map_imperatively(DATA_CLASS_OBJECT,TABLE_OBJECT)

