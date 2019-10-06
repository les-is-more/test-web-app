from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker, mapper
from sqlalchemy.ext.declarative import declarative_base


login = { 'UID': 'diapox',
    'PW':'Priest.1',
    'server': 'lizzie.cvqr1dhfa9aq.ap-southeast-1.rds.amazonaws.com',
    'db':'lizzie'}
# To resolve the issue of misisng MySQLDB module in Flask ORM, make sure 
# to include PyMYSQL in the requirements and in the URI.
serverURI =  "mysql+pymysql://{}:{}@{}/{}".format(login['UID'],login['PW'], login['server'],login['db'])

engine = create_engine(serverURI, convert_unicode = True, echo=True)
metadata = MetaData(bind=engine)

dbSession = scoped_session(sessionmaker(autocommit=True, \
    autoflush=True, bind=engine))

Base = declarative_base()
Base.query = dbSession.query_property()


# def init_db():
#     # import all modules here that might define models so that
#     # they will be registered properly on the metadata.  Otherwise
#     # you will have to import them first before calling init_db()
#     # import yourapplication.models
#     Base.metadata.create_all(bind=engine)