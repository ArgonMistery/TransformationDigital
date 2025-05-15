import sys
sys.path.append("..")
from orm.repository import RepositoryForms
from orm.models import Questionary as QuestionaryModel
from orm.orm import Questionary as QuestionaryTable 
from orm.orm import StartMappers
from orm.connections import resumen_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


ReportDataEngine=create_engine(resumen_url)
SessionReportData=sessionmaker(bind=ReportDataEngine)

with SessionReportData() as session:
    repositoryReportData=RepositoryForms(session)

    AvailableMapper=StartMappers(QuestionaryModel,QuestionaryTable)

    print(repositoryReportData.get(QuestionaryModel))
