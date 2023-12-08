from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = 'postgresql+psycopg2://user:JqzFXy7c3JSFebDsVAaVElVBSTlRsTDL@dpg-clp5rhp46foc73cd9es0-a/todos_v0uv'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


