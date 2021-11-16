from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

Base = declarative_base()

logger = logging.getLogger(__name__)

class Database:
    # http://docs.sqlalchemy.org/en/latest/core/engines.html

    # Main DB Connection Ref Obj
    db_engine = None
    session: sessionmaker = None

    def __init__(self, db_uri: str):
        self.db_engine = create_engine(db_uri, connect_args={'check_same_thread': False})
        Base.metadata.create_all(self.db_engine)
        self.connection = self.db_engine.connect()
        self.session = sessionmaker(bind=self.db_engine)
        logger.info(self.db_engine)
