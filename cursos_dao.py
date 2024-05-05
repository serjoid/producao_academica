import sqlite3

class CursoDAO:
    def __init__(self):
        self.db_path = 'controle_producao.db'  # O banco de dados está na mesma raiz que o código

    def get_cursos(self):
        """Retorna uma lista de nomes de cursos."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT nome_curso FROM cursos ORDER BY nome_curso")
            return [row[0] for row in cursor.fetchall()]

    def get_curso_info(self, nome_curso):
        """Retorna as informações de um curso específico pelo nome."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, nome_curso, sigla
                FROM cursos WHERE nome_curso = ?""", (nome_curso,))
            return cursor.fetchone()

    def insert_curso(self, curso_data):
        """Insere um novo curso na tabela."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO cursos (nome_curso, sigla)
                VALUES (?, ?)""",
                           (curso_data['nome_curso'], curso_data['sigla']))
            conn.commit()

    def update_curso(self, curso_data):
        """Atualiza os dados de um curso existente."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            print("Valores dos parâmetros:", curso_data['nome_curso'], curso_data['sigla'], curso_data['id'])  # Corrigido aqui
            cursor.execute("""
            UPDATE cursos 
            SET nome_curso=?, sigla=?
            WHERE id=?  
            """,
            (curso_data['nome_curso'], curso_data['sigla'], curso_data['id']))  # Corrigido aqui