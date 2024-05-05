import sqlite3

class AlunoDAO:
    def __init__(self):
        self.db_path = 'controle_producao.db'  # O banco de dados está na mesma raiz que o código

    def get_alunos(self):
        """Retorna uma lista de nomes de alunos."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT nome FROM alunos ORDER BY nome")
            return [row[0] for row in cursor.fetchall()]
        
    def get_cursos(self):
        """Retorna uma lista de nomes de alunos."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT curso FROM alunos")
            return [row[0] for row in cursor.fetchall()]
        
    def get_orientadores(self):
        """Retorna uma lista de nomes de alunos."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT nome FROM alunos")
            return [row[0] for row in cursor.fetchall()]
        
    def get_relatorio_completo(self):
        """Retorna uma lista de todas as informações dos alunos."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                            SELECT nome, telefone, email, orientador, curso, sigla_curso, tipo_curso,
                            ano_ingresso, ano_conclusao, situacao, instituicao, prazo_entrega,
                            prorrogacao, tipo_tcc, tema, bolsa, tipo_bolsa, vinculo
                            FROM alunos ORDER BY nome
                        """)
            return cursor.fetchall()


    def get_aluno_info(self, nome):
        """Retorna as informações de um aluno específico pelo nome."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, nome, telefone, email, orientador, curso, sigla_curso, tipo_curso,
                       ano_ingresso, ano_conclusao, situacao, instituicao, prazo_entrega,
                       prorrogacao, tipo_tcc, tema, bolsa, tipo_bolsa, vinculo
                FROM alunos WHERE nome = ?""", (nome,))
            return cursor.fetchone()
        
    def insert_aluno(self, aluno_data):
        """Insere um novo aluno na tabela."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO alunos (nome, telefone, email, orientador, curso, sigla_curso, tipo_curso,
                                    ano_ingresso, ano_conclusao, situacao, instituicao, prazo_entrega,
                                    prorrogacao, tipo_tcc, tema, bolsa, tipo_bolsa, vinculo)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                           (aluno_data['nome'], aluno_data['telefone'], aluno_data['email'], 
                            aluno_data['orientador'], aluno_data['curso'], aluno_data['sigla_curso'], 
                            aluno_data['tipo_curso'], aluno_data['ano_ingresso'], aluno_data['ano_conclusao'],
                            aluno_data['situacao'], aluno_data['instituicao'], aluno_data['prazo_entrega'],
                            aluno_data['prorrogacao'], aluno_data['tipo_tcc'], aluno_data['tema'], 
                            aluno_data['bolsa'], aluno_data['tipo_bolsa'], aluno_data['vinculo']))
            conn.commit()

    def update_aluno(self, aluno_data):
        """Atualiza os dados de um aluno existente."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE alunos 
                SET nome=?, telefone=?, email=?, orientador=?, curso=?, sigla_curso=?, tipo_curso=?,
                    ano_ingresso=?, ano_conclusao=?, situacao=?, instituicao=?, prazo_entrega=?,
                    prorrogacao=?, tipo_tcc=?, tema=?, bolsa=?, tipo_bolsa=?, vinculo=?
                WHERE id=?""",
                           (aluno_data['nome'], aluno_data['telefone'], aluno_data['email'], aluno_data['orientador'],
                            aluno_data['curso'], aluno_data['sigla_curso'], aluno_data['tipo_curso'], 
                            aluno_data['ano_ingresso'], aluno_data['ano_conclusao'], aluno_data['situacao'], 
                            aluno_data['instituicao'], aluno_data['prazo_entrega'], aluno_data['prorrogacao'], 
                            aluno_data['tipo_tcc'], aluno_data['tema'], aluno_data['bolsa'], 
                            aluno_data['tipo_bolsa'], aluno_data['vinculo'], aluno_data['id']))

            conn.commit()
