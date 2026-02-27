from sqlalchemy.orm import declarative_base

Base = declarative_base()


# Users module
from app.modules.users import models as users_models