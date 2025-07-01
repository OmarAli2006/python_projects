# Practica del metodo factory para la conexion a sistemas de gestiomn de bases de datos
# Creado por: Omar Chanel Ali Fuertes

class DatabaseConnection:
    def connect(self):
        raise NotImplementedError("Subclase debe implementar por las subclases")

#clases concretas para diferentes sistemas de gestion de bases de datos
class MySQLConnection(DatabaseConnection):
    def connect(self):
        print("Conectando a MySQL")
        
class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        print("Conectando a PostgreSQL")

class OracleConnection(DatabaseConnection):
    def connect(self):
        print("Conectando a Oracle")

class SQLiteConnection(DatabaseConnection):
    def connect(self):
        print("Conectando a SQLite")

#fabrica de conexiones a sistemas de gestion de bases de datos
class DatabaseConnectionFactory:
    @staticmethod
    def create_connection(connection_type):
        if connection_type == "mysql":
            return MySQLConnection()
        elif connection_type == "postgresql":
            return PostgreSQLConnection()
        elif connection_type == "oracle":
            return OracleConnection()
        elif connection_type == "sqlite":
            return SQLiteConnection()
        else:
            raise ValueError("Tipo de conexion no reconocido")
            

if __name__ == "__main__":
    # Crear una conexion a MySQL
    mysql = DatabaseConnectionFactory.create_connection("mysql")
    mysql.connect()
    
    # Crear una conexion a PostgreSQL
    postgresql = DatabaseConnectionFactory.create_connection("postgresql")
    postgresql.connect()
    
    # Crear una conexion a Oracle
    oracle = DatabaseConnectionFactory.create_connection("oracle")
    oracle.connect()
    
    # Crear una conexion a SQLite
    sqlite = DatabaseConnectionFactory.create_connection("sqlite")
    sqlite.connect()

    mongo = DatabaseConnectionFactory.create_connection("mongo")
    mongo.connect()