import sqlite3
import flet as ft


class Relatorios:
    def __init__(self):
        self.db_path = 'controle_producao.db'  # O banco de dados está na mesma raiz que o código

    def get_relatorio(self):
        """Retorna os dados para o DataTable."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Consulta SQL para recuperar todos os dados
            cursor.execute("""
                            SELECT nome, sigla_curso, orientador, ano_ingresso, ano_conclusao, 
                                tema, bolsa, vinculo
                            FROM alunos
                            ORDER BY nome
                            """)

            # Extrai os dados da consulta
            dados_alunos = cursor.fetchall()

            # Cria as linhas do DataTable
            rows = []
            for aluno in dados_alunos:
                cells = [
                    ft.DataCell(ft.Text(valor, size=10, selectable=True)) for valor in aluno
                ]
                rows.append(ft.DataRow(cells=cells))

            return rows
