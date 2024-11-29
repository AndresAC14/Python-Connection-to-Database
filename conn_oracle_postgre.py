import os
from dotenv import load_dotenv
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select

load_dotenv()


username = os.getenv("POSTGRESQL_USERNAME")
password = os.getenv("POSTGRESQL_PASSWORD")
host = os.getenv("POSTGRESQL_HOSTNAME")
port = os.getenv("POSTGRESQL_PORT")
db_name = os.getenv("POSTRESQL_DBNAME")


class Recipe(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=30)


# Con echo=True se muestran los comandos
oracle_url = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}"
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
