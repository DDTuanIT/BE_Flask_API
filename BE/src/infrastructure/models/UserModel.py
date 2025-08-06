from sqlachemy import Column, Integer, String
from infrastructure.databases.base import Base

class UserModel(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    role = Column(String(50), nullable=True)
