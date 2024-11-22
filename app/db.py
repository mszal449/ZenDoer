from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.models import Subtask, Task

DATABASE_URL = "sqlite:///local_database.db"

engine = create_engine(DATABASE_URL, echo=True)

# Define a base class for models
Base = declarative_base()

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Initialize the database
def init_db():
    Base.metadata.create_all(bind=engine)
