from sqlalchemy import create_engine, BigInteger, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, declarative_base

engine = create_engine('postgresql://postgres:12345@localhost:5432/postgres')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String, nullable=False)

    notes: Mapped['Note'] = relationship('Note', uselist=True)


class Note(Base):
    __tablename__ = 'notes'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(ForeignKey('users.tg_id'), unique=True, nullable=False)
    note: Mapped[str] = mapped_column(String(500), nullable=False)

    user: Mapped['User'] = relationship('User')

def create_database():
    Base.metadata.create_all(engine)