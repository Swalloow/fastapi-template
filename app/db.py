from databases import Database
from sqlalchemy import MetaData, create_engine

from app.config import settings

# sqlalchemy
DATABASE_URI = str(settings.SQLALCHEMY_DATABASE_URI)
engine = create_engine(DATABASE_URI)
metadata = MetaData()

# databases query builder
database = Database(DATABASE_URI)
