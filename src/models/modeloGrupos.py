from database.db import get_connection
from .entities.Grupo import Grupo

class modeloGrupos():
    
    @classmethod
    def get_grupos(self):
        try:
            connection = get_connection()
            GruposA = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Grupos ORDER BY numero ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    grupo = Grupo(row[0], row[1], row[2], row[3],row[4],row[5])
                    GruposA.append(grupo.to_JSON())

            connection.close()
            return GruposA
        except Exception as ex:
            raise Exception(ex)