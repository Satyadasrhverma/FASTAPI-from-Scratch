from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base

Databse_url = "sqlite:///./students.db"

engine = create_engine(Databse_url)

Session = sessionmaker(bind=engine)

Base = declarative_base() #Without Base, SQLAlchemy will not recognize the class as a table
#This Base class converts the Python class into a database table model.