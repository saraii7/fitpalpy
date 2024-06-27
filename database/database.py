import sqlite3

class Database:
    def __init__(self, db_name="fitpal.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                apellido TEXT,
                email TEXT UNIQUE,
                contraseña TEXT,
                tipo_usuario TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS rutinas (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                descripcion TEXT,
                usuario_id INTEGER,
                FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
            )
        ''')
        self.connection.commit()

    def agregar_usuario(self, nombre, apellido, email, contraseña, tipo_usuario):
        self.cursor.execute('''
            INSERT INTO usuarios (nombre, apellido, email, contraseña, tipo_usuario)
            VALUES (?, ?, ?, ?, ?)
        ''', (nombre, apellido, email, contraseña, tipo_usuario))
        self.connection.commit()

    def obtener_usuario(self, email):
        self.cursor.execute('''
            SELECT * FROM usuarios WHERE email = ?
        ''', (email,))
        return self.cursor.fetchone()