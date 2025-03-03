import os
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


# Con echo=True se muestran los comandos
oracle_url = f"oracle+oracledb://{username}:{pw}@{hostname}/{sid}"
engine = create_engine(oracle_url, echo=True)

# En este momento se crea la tabla
SQLModel.metadata.create_all(engine)


def create_recipes():
    recipe1 = Recipe(id="9", name="Tortilla")
    recipe2 = Recipe(id="8", name="Sopa")

    with Session(engine) as session:
        session.add(recipe1)
        session.add(recipe2)

        session.commit()


def select_recipes():
    with Session(engine) as session:
        statement = select(Recipe)  # .where(Recipe.id == 15)
        reseta = session.exec(statement)
        for result in reseta:
            print(result)


create_recipes()
select_recipes()
