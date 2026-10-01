from datetime import datetime

from sqlalchemy import ForeignKey, MetaData, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

metadataObj = MetaData()

class Base(DeclarativeBase):
    pass

class Client(Base):
    __tablename__ = 'client'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    contact: Mapped[str] = mapped_column(nullable=False)
    note: Mapped[str] = mapped_column(default='Пусто')
    status: Mapped[str] = mapped_column(default='lead')
    createdAt: Mapped[datetime] = mapped_column(server_default=text('CURRENT_TIMESTAMP'))

class Project(Base):
    __tablename__ = 'project'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    clientId: Mapped[int] = mapped_column(ForeignKey(Client.id))
    title: Mapped[str] = mapped_column(nullable=False)
    budget: Mapped[str] = mapped_column(nullable=False)
    note: Mapped[str] = mapped_column(default='Пусто')
    deadline: Mapped[datetime] = mapped_column(default=None)
    createdAt: Mapped[datetime] = mapped_column(server_default=text('CURRENT_TIMESTAMP'))
