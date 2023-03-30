import sqlite3
from src.models.usuario import Usuario

class UsuarioDAO:

    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = UsuarioDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db', check_same_thread=False)

    def comparar_email(self, email):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT email FROM Usuarios WHERE email = '{email}';
        """)
        resultado = self.cursor.fetchone()
        if resultado != None:
            self.conn.commit()
            self.cursor.close()
            return True
        self.conn.commit()
        self.cursor.close()
        return False

    def comparar_senha(self, senha):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT senha FROM Usuarios WHERE senha = '{senha}';
        """)
        resultado = self.cursor.fetchone()
        if resultado != None:
            self.conn.commit()
            self.cursor.close()
            return True
        self.conn.commit()
        self.cursor.close()
        return False

    def cadastrar_usuario(self, usuario):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Usuarios (id, nome, email, senha)
            VALUES(?,?,?,?);
        """, (usuario.get_id(), usuario.get_nome(), usuario.get_email(), usuario.get_senha()))
        self.conn.commit()
        self.cursor.close()

    def procurar_usuario(self, nome):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Usuarios
            WHERE nome = '{nome}';
        """)
        user = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            user = Usuario(id=resultado[0], nome=resultado[1], email=resultado[2], senha=resultado[3])
        self.cursor.close()
        return user