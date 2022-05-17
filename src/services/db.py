from sqlalchemy import create_engine, text


class DB:
    def __init__(self, db_name: str, host: str, port: str, username: str, password: str):
        """
        Init class
        :param db_name:
        :param host:
        :param port:
        :param username:
        :param password:
        """
        self.eng = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}")

    def search_ingredients_by_name(self, name:str, owner_id: str) -> list:
        """
        Get all ingredients by name
        :param name:
        :param owner_id:
        :return:
        """
        with self.eng.connect() as con:
            result_set = con.execute(text(
                f"SELECT DISTINCT ON (name) * FROM ingredients WHERE (owner_id={owner_id} or owner_id is null) and name like '%{name}%' ORDER BY name, owner_id"))
            return result_set
