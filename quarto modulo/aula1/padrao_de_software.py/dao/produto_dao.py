class ProdutoDAO:
    def __init__(self, db_name1 = 'produto.db'):
        self.db_name1 = db_name1
        self._criar_tabela()
    
    def _criar_tabela(self):
        with sqlite3.connect(self.db_name1) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS produto (
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    nome TEXT NOT NULL
                )
             ''')
    
    def salvar(self):
        with sqlite3.connect(self.db_name1) as conn:
            cursor = conn. cursor()
            cursor.execute('SELECT nome FROM produto')
            rows = cursor.fetchall
            return [produto(nome) for nome in rows]