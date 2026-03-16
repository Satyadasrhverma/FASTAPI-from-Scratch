from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base


database_url = "sqlite:///./notes.db"

engine = create_engine(database_url)

sessionloacal = sessionmaker(bind=engine)

Base = declarative_base()