import sqlite3

class OrientadorDAO:
    def __init__(self):
        self.db_path = 'controle_producao.db'  # O banco de dados está na mesma raiz que o código

    def get_orientadores(self):
        """Retorna uma lista de nomes de orientadores."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT nome FROM orientadores ORDER BY nome")
            return [row[0] for row in cursor.fetchall()]

    def get_orientador_info(self, nome):
        """Retorna as informações de um orientador específico pelo nome."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, nome, telefone, email, vinculo, instituicao
                FROM orientadores WHERE nome = ?""", (nome,))
            return cursor.fetchone()

    def insert_orientador(self, orientador_data):
        """Insere um novo orientador na tabela."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO orientadores (nome, telefone, email, vinculo, instituicao)
                VALUES (?, ?, ?, ?, ?)""",
                           (orientador_data['nome'], orientador_data['telefone'], orientador_data['email'], 
                            orientador_data['vinculo'], orientador_data['instituicao']))
            conn.commit()

    def update_orientador(self, orientador_data):
        """Atualiza os dados de um orientador existente."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE orientadores 
                SET nome=?, telefone=?, email=?, vinculo=?, instituicao=?
                WHERE id=?""",
                           (orientador_data['nome'], orientador_data['telefone'], orientador_data['email'],
                            orientador_data['vinculo'], orientador_data['instituicao'], orientador_data['id']))
            conn.commit()
