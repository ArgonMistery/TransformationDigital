from dataclasses import dataclass
from typing import NewType

QuestionValue=NewType("QuestionValue",int)
QuestionString=NewType("QuestionString",str)

@dataclass
class Questionary():
    TYPE:str
    QUESTION_A:int
    QUESTION_B:int
    QUESTION_C:int
    QUESTION_D:int
    QUESTION_E:int
    QUESTION_F:int
    QUESTION_G:int
    QUESTION_H:int
    QUESTION_I:int
    QUESTION_J:int
    QUESTION_K:int
    QUESTION_L:int
    QUESTION_M:int
    QUESTION_O:int
    QUESTION_P:int
    QUESTION_Q:int
    QUESTION_R:int
    QUESTION_S:int
    QUESTION_T:int
    QUESTION_U:int
    QUESTION_V:int
