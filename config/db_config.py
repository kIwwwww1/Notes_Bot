from datetime import datetime
from sqlalchemy import DateTime, create_engine, BigInteger, String, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship, declarative_base
from typing import List


engine = create_engine('postgresql://postgres:12345@localhost:5432/postgres', echo=False)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String, nullable=False)

    notes: Mapped[List['Note']] = relationship('Note', uselist=True)


class Note(Base):
    __tablename__ = 'notes'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(ForeignKey('users.tg_id'), nullable=False)
    note: Mapped[str] = mapped_column(String(500), nullable=False)
    adding_time: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    user: Mapped['User'] = relationship('User')

def create_database():
    Base.metadata.create_all(engine)

# Для запуска нужно быть в корне проета и ввести для запуска 
# python3 -m config.bot_config