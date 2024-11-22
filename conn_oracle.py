import os
import oracledb
from dotenv import load_dotenv

load_dotenv()


username = os.getenv("ORACLE_USERNAME")
pw = os.getenv("ORACLE_PASSWORD")
hostname = os.getenv("ORACLE_HOSTNAME")
sid = os.getenv("ORACLE_SID")


connection = oracledb.connect(user=username, password=pw, host=hostname, sid=sid)
cursor = connection.cursor()

query = """
CREATE TABLE RECETA (
    ID NUMBER PRIMARY KEY,
    NAME VARCHAR2(30)
)
"""
cursor.execute(query)


query = """INSERT INTO RECETA VALUES (7, 'AGUA')"""
cursor.execute(query)

query = """
SELECT *
FROM RECETA
"""
for result in cursor.execute(query):
    print(result)


connection.commit()

cursor.close()
connection.close()
