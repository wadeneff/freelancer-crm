from database.models import Base, Client
from sqlalchemy import create_engine, delete, insert, select, update
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///database/database.sql"

engine = create_engine(
    url=DATABASE_URL,
    echo=True
)

session = sessionmaker(engine)


def initDb() -> None:
    Base.metadata.create_all(engine)


def getClients():
    with session() as s:
        query = select(Client)
        res = s.execute(query)
        clients = res.scalars().all()

        return clients

def getClient(id):
    with session() as s:
        query = select(Client).where(Client.id==id)
        res = s.execute(query)
        client = res.scalar_one()
        return client

def addClient(name: str, contact: str, note: str) -> None:
    with session() as s:
        stmt = (
            insert(Client)
            .values(
                name=name,
                contact=contact,
                note=note
            )
        )
        s.execute(stmt)
        s.commit()

def deleteClient(id: int):
    with session() as s:
        stmt = delete(Client).where(Client.id == id)
        s.execute(stmt)
        s.commit()
