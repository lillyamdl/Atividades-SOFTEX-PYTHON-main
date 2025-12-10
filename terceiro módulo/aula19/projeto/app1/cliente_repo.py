from app1.db import Database

class ClienteRepository:
    def __init__(self, db: Database):
        self.db = db
    
    def listar_todos(self):
        sql = "SELECT id, nome, email, telefone, criado_em FROM cliente ORDER BY criado_em DESC"
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        finally:
            conn.close()
    
    def criar(self, nome: str, email: str, telefone: str):
        sql = "INSERT INTO cliente (nome, email, telefone) VALUES (%s, %s, %s)"
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (nome, email, telefone))
            cliente_id = cursor.lastrowid
            conn.commit()
            cursor.close()
            return cliente_id
        finally:
            conn.close()
    
    def buscar_por_id(self, cliente_id: int):
        sql = "SELECT id, nome, email, telefone, criado_em FROM cliente WHERE id = %s"
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql, (cliente_id,))
            resultado = cursor.fetchone()
            cursor.close()
            return resultado
        finally:
            conn.close()
    
    def atualizar_telefone(self,cliente_id : int, novo_telefone : str):
        sql = " update cliente set telefone = %s where id = %s"
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql, (novo_telefone, cliente_id))
            conn.commit()
            linhas_afetadas = cursor.rowcount()
            cursor.close()
            return linhas_afetadas > 0
        finally:
            conn.close()
    
    def remover(self,cliente_id : int):
        sql = "delete from cliente where id = %s"
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql, (cliente_id,))
            conn.commit()
            linhas = cursor.rowcount()
            cursor.close()
            return linhas > 0
        finally:
            conn.close()

