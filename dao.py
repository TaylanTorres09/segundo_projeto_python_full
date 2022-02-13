from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class RetornaSession:
    @staticmethod
    def retornaSession():
        USUARIO = "root"
        SENHA = ""
        HOST = "localhost"
        BANCO = "desafio2"
        PORT = "3306"

        CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

        engine = create_engine(CONN, echo=False)
        Senssion = sessionmaker(bind=engine)
        session = Senssion()
        return engine, session