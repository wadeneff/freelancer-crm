from database.models import Base, Client
from sqlalchemy import create_engine, insert, select, update
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
        for client in clients:
            print(f"ID: {client.id} | Имя: {client.name} | Контакты: {client.contact} | Заметка: {client.note}")

        return clients

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
