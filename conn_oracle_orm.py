import os
import oracledb
from dotenv import load_dotenv
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select

load_dotenv()


username = os.getenv("ORACLE_USERNAME")
pw = os.getenv("ORACLE_PASSWORD")
hostname = os.getenv("ORACLE_HOSTNAME")
sid = os.getenv("ORACLE_SID")


class Recipe(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=30)


recipe1 = Recipe(id="12", name="Pizza")

engine = create_engine(f"oracle+oracledb://{username}:{pw}@{hostname}/{sid}", echo=True)

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(recipe1)
    statement = select(Recipe).where(Recipe.id == 12)
    reseta = session.exec(statement)
    for result in reseta:
        print(result)
    # session.commit()
