from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

user = 'root'
passwd = 'BibliotecaFastapi'

user1 = "myuser"
passwd1 = "biblioteca"

host = '127.0.0.1'
bbdd = 'mysql_biblioteca_fastapi'

SQLALCHEMY_DATABASE_URL = f"mysql+mysqldb://{user}:{passwd}@{host}/{bbdd}"

conf_bbdd = {
    'pool_size': 10,
    'max_overflow': 20
}

engine = create_engine(SQLALCHEMY_DATABASE_URL, **conf_bbdd)

"""
PARA CONECTARSE => "mysql+mysqldb://u:pi@host/bd" => OJO poner IP 127.0.0.1
engine = create_engine(
    # "mysql+mysqldb://myuser:biblioteca@127.0.0.1/mysql_biblioteca_fastapi", => para usuario
    "mysql+mysqldb://root:BibliotecaFastapi@127.0.0.1/mysql_biblioteca_fastapi", => root
    pool_size=10, max_overflow=20)

"""
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# https://fastapi.tiangolo.com/tutorial/sql-databases/#__tabbed_1_2
