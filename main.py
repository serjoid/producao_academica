import flet as ft
import alunos_dao
import orientadores_dao
import cursos_dao
import relatorios
import pandas as pd

def main(page: ft.Page):
    page.theme_mode = "LIGHT"
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.BOOK, color="WHITE"),
        #leading_width=40,
        title=ft.Text("Acompanhamento da produção acadêmica - CEPEP", color="WHITE"),
        center_title=True,
        bgcolor=ft.colors.BLUE
    )
    page.scroll = True

    aluno_dao = alunos_dao.AlunoDAO()
    orientador_dao = orientadores_dao.OrientadorDAO()
    curso_dao = cursos_dao.CursoDAO()
    relatorios_ = relatorios.Relatorios()
    # Dropdowns
    dropdown_alunos =  ft.Dropdown(width=800, on_change=None)
    dropdown_cursos =  ft.Dropdown(width=800, on_change=None)
    dropdown_orientadores = ft.Dropdown(width=800, on_change=None)
    dropdown_status = ft.Dropdown(width=300, on_change=None, label="Situação")
    dropdown_filtro_cursos = ft.Dropdown(width=300, on_change=None, label="Curso")
    dropdown_filtro_orientadores = ft.Dropdown(width=300, on_change=None, label="Orientador")

    # variáveis para gerar o relatório
    dados_relatorio = relatorios_.get_relatorio()
    columns = [
            ft.DataColumn(ft.Text("Nome", width=150, size=10)),
            ft.DataColumn(ft.Text("Sigla Curso", width=50, size=10)),
            ft.DataColumn(ft.Text("Orientador", width=150, size=10)),
            ft.DataColumn(ft.Text("Ano Ingresso", width=50, size=10)),
            ft.DataColumn(ft.Text("Ano Conclusao", width=50, size=10)),
            ft.DataColumn(ft.Text("Tema", width=300, size=10)),
            ft.DataColumn(ft.Text("Bolsa", width=50, size=10)),
            ft.DataColumn(ft.Text("Vinculo", width=150, size=10)),
        ]

        # Cria o datatable
    datatable = ft.Container(
                    
                    ft.DataTable(
                            columns=columns,
                            rows=dados_relatorio,
                            border=ft.border.all(1, "black")
                        ),
                width=1300
                )

    # Garantir que todos os TextField são inicializados com read_only=True
    nome_aluno = ft.TextField(label="Nome", width=800, read_only=True)
    telefone_aluno = ft.TextField(label="Telefone", width=800, read_only=True)
    email_aluno = ft.TextField(label="Email", width=800, read_only=True)
    orientador = ft.TextField(label="Orientador", width=800, read_only=True)
    curso = ft.TextField(label="Curso", width=800, read_only=True)
    tipo_curso = ft.TextField(label="Tipo de curso", width=800, read_only=True)
    sigla_curso = ft.TextField(label="Sigla do curso", width=800, read_only=True)
    ano_ingresso = ft.TextField(label="Ano de ingresso", width=800, read_only=True)
    ano_conclusao = ft.TextField(label="Ano previsto de conclusão", width=800, read_only=True)
    situacao = ft.TextField(label="Situação atual", width=800, read_only=True)
    instituicao = ft.TextField(label="Instituição", width=800, read_only=True)
    prazo_entrega = ft.TextField(label="Prazo de entrega do TCC", width=800, read_only=True)
    prorrogacao = ft.TextField(label="Prorrogação", width=800, read_only=True)
    tipo_tcc = ft.TextField(label="Tipo de TCC", width=800, read_only=True)
    tema = ft.TextField(label="Tema do TCC", width=800, read_only=True)
    bolsa = ft.TextField(label="Bolsa", width=800, read_only=True)
    tipo_bolsa = ft.TextField(label="Tipo de bolsa", width=800, read_only=True)
    vinculo = ft.TextField(label="Vínculo", width=800, read_only=True)

    def load_alunos():
        alunos = aluno_dao.get_alunos()
        dropdown_alunos.options = [ft.dropdown.Option(text=nome) for nome in alunos]
        dropdown_alunos.update()

    def load_cursos():
        cursos = aluno_dao.get_cursos()
        dropdown_cursos.options = [ft.dropdown.Option(text=curso) for curso in cursos]
        dropdown_cursos.update()

    def load_orientadores():
        orientadores = aluno_dao.get_orientadores()
        dropdown_orientadores.options = [ft.dropdown.Option(text=orientador) for orientador in orientadores]
        dropdown_orientadores.update()

    # exportar relatório
    def export_to_excel(e: ft.FilePickerResultEvent):
        # Obter os dados do relatório completo
        dados_relatorio = aluno_dao.get_relatorio_completo()
        # Converte os dados em um DataFrame do pandas
        df_alunos = pd.DataFrame(dados_relatorio, columns=[
            "Nome", "Telefone", "Email", "Orientador", "Curso", "Sigla_Curso", "Tipo_Curso",
            "Ano_Ingresso", "Ano_Conclusao", "Situacao", "Instituicao", "Prazo_Entrega",
            "Prorrogacao", "Tipo_TCC", "Tema", "Bolsa", "Tipo_Bolsa", "Vinculo"
        ])
        # Salva o DataFrame em um arquivo Excel
        df_alunos.to_excel("relatorio_cepep.xlsx", index=False)
        # Cria o FilePicker
        file_picker = ft.FilePicker.save_file()
        # Adiciona o FilePicker à overlay da página
        page.overlay.append(file_picker)
        # Abre o FilePicker
        # Atualiza a página para exibir o FilePicker
        page.update()





    # Atualiza os campos com informações do aluno selecionado
    def on_aluno_selected(e):
        global id_aluno
        aluno_info = aluno_dao.get_aluno_info(e.control.value)
        if aluno_info:
            id_aluno = aluno_info[0]
            nome_aluno.value = aluno_info[1]
            telefone_aluno.value = aluno_info[2]
            email_aluno.value = aluno_info[3]
            orientador.value = aluno_info[4]
            curso.value = aluno_info[5]
            tipo_curso.value = aluno_info[6]
            sigla_curso.value = aluno_info[7]
            ano_ingresso.value = aluno_info[8]
            ano_conclusao.value = aluno_info[9]
            situacao.value = aluno_info[10]
            instituicao.value = aluno_info[11]
            prazo_entrega.value = aluno_info[12]
            prorrogacao.value = aluno_info[13]
            tipo_tcc.value = aluno_info[14]
            tema.value = aluno_info[15]
            bolsa.value = aluno_info[16]
            tipo_bolsa.value = aluno_info[17]
            vinculo.value = aluno_info[18]
            # Chamar o método update para cada TextField para atualizar a interface
            for field in [nome_aluno, telefone_aluno, email_aluno, orientador, curso, tipo_curso, sigla_curso, ano_ingresso, ano_conclusao,
                        situacao, instituicao, prazo_entrega, prorrogacao, tipo_tcc, tema, bolsa, tipo_bolsa, vinculo]:
                field.update()

    # Conecte o evento de mudança do dropdown à função de atualização
    dropdown_alunos.on_change = on_aluno_selected

    def botao_alunos(e):
        menu_alunos.visible = True
        nome_aluno.read_only = True
        telefone_aluno.read_only = True
        email_aluno.read_only = True
        orientador.read_only = True
        curso.read_only = True
        tipo_curso.read_only = True
        sigla_curso.read_only = True
        ano_ingresso.read_only = True
        ano_conclusao.read_only = True
        situacao.read_only = True
        instituicao.read_only = True
        prazo_entrega.read_only = True
        prorrogacao.read_only = True
        tipo_tcc.read_only = True
        tema.read_only = True
        bolsa.read_only = True
        tipo_bolsa.read_only = True
        vinculo.read_only = True
        # visibilidade dos botões
        botao_cadastro_cursos.visible = False
        dropdown_cursos.visible = False
        menu_cursos.visible = False
        botao_cadastro_orientadores.visible = False
        dropdown_orientadores.visible = False
        botao_salvar_orientadores.visible = False
        menu_orientadores.visible = False
        botao_cadastro_alunos.visible = False
        botao_salvar_alunos.visible = False
        menu_relatorios.visible = False
        dropdown_alunos.visible = True
        # Limpa os valores
        nome_aluno.value = ""
        telefone_aluno.value = ""
        email_aluno.value = ""
        orientador.value = ""
        curso.value = ""
        tipo_curso.value = ""
        sigla_curso.value = ""
        ano_ingresso.value = ""
        ano_conclusao.value = ""
        situacao.value = ""
        instituicao.value = ""
        prazo_entrega.value = ""
        prorrogacao.value = ""
        tipo_tcc.value = ""
        tema.value = ""
        bolsa.value = ""
        tipo_bolsa.value = ""
        vinculo.value = ""
        dropdown_alunos.value = ""
        load_alunos()
        page.update()

    def botao_atualizar_alunos(e):
        nome_aluno.read_only = False
        telefone_aluno.read_only = False
        email_aluno.read_only = False
        orientador.read_only = False
        curso.read_only = False
        tipo_curso.read_only = False
        sigla_curso.read_only = False
        ano_ingresso.read_only = False
        ano_conclusao.read_only = False
        situacao.read_only = False
        instituicao.read_only = False
        prazo_entrega.read_only = False
        prorrogacao.read_only = False
        tipo_tcc.read_only = False
        tema.read_only = False
        bolsa.read_only = False
        tipo_bolsa.read_only = False
        vinculo.read_only = False
        botao_cadastro_alunos.visible = False
        botao_salvar_alunos.visible = True
        dropdown_alunos.visible = True
        alert_update_dialog()
        load_alunos()
        page.update()

    def botao_cadastrar_alunos(e):
        nome_aluno.read_only = False
        telefone_aluno.read_only = False
        email_aluno.read_only = False
        orientador.read_only = False
        curso.read_only = False
        tipo_curso.read_only = False
        sigla_curso.read_only = False
        ano_ingresso.read_only = False
        ano_conclusao.read_only = False
        situacao.read_only = False
        instituicao.read_only = False
        prazo_entrega.read_only = False
        prorrogacao.read_only = False
        tipo_tcc.read_only = False
        tema.read_only = False
        bolsa.read_only = False
        tipo_bolsa.read_only = False
        vinculo.read_only = False
        # visibilidade dos botões
        botao_cadastro_cursos.visible = False
        dropdown_cursos.visible = False
        menu_cursos.visible = False
        botao_cadastro_orientadores.visible = False
        dropdown_orientadores.visible = False
        botao_salvar_orientadores.visible = False
        menu_orientadores.visible = False
        botao_cadastro_alunos.visible = True
        dropdown_alunos.visible = False
        botao_salvar_alunos.visible = False
        #limpar valores do textfield
        nome_aluno.value = ""
        telefone_aluno.value = ""
        email_aluno.value = ""
        orientador.value = ""
        curso.value = ""
        tipo_curso.value = ""
        sigla_curso.value = ""
        ano_ingresso.value = ""
        ano_conclusao.value = ""
        situacao.value = ""
        instituicao.value = ""
        prazo_entrega.value = ""
        prorrogacao.value = ""
        tipo_tcc.value = ""
        tema.value = ""
        bolsa.value = ""
        tipo_bolsa.value = ""
        vinculo.value = ""
        dropdown_alunos.value = ""
        alert_update_dialog()
        load_alunos()
        page.update()

    def insert_new_aluno(e):
        aluno_data = {
            'nome': nome_aluno.value,
            'telefone': telefone_aluno.value,
            'email': email_aluno.value,
            'orientador': orientador.value,
            'curso': curso.value,
            'tipo_curso': tipo_curso.value,
            'sigla_curso': sigla_curso.value,
            'ano_ingresso': ano_ingresso.value,
            'ano_conclusao': ano_conclusao.value,
            'situacao': situacao.value,
            'instituicao': instituicao.value,
            'prazo_entrega': prazo_entrega.value,
            'prorrogacao': prorrogacao.value,
            'tipo_tcc': tipo_tcc.value,
            'tema': tema.value,
            'bolsa': bolsa.value,
            'tipo_bolsa': tipo_bolsa.value,
            'vinculo': vinculo.value
        }
        # Chamar o método de atualização da DAO
        aluno_dao.insert_aluno(aluno_data)
        nome_aluno.read_only = True
        telefone_aluno.read_only = True
        email_aluno.read_only = True
        orientador.read_only = True
        curso.read_only = True
        tipo_curso.read_only = True
        sigla_curso.read_only = True
        ano_ingresso.read_only = True
        ano_conclusao.read_only = True
        situacao.read_only = True
        instituicao.read_only = True
        prazo_entrega.read_only = True
        prorrogacao.read_only = True
        tipo_tcc.read_only = True
        tema.read_only = True
        bolsa.read_only = True
        tipo_bolsa.read_only = True
        vinculo.read_only = True
        show_confirmation_dialog()
        page.update()

    def save_aluno(e):
        # Coletar dados dos TextField
        aluno_data = {
            'id': int(id_aluno),
            'nome': nome_aluno.value,
            'telefone': telefone_aluno.value,
            'email': email_aluno.value,
            'orientador': orientador.value,
            'curso': curso.value,
            'tipo_curso': tipo_curso.value,
            'sigla_curso': sigla_curso.value,
            'ano_ingresso': ano_ingresso.value,
            'ano_conclusao': ano_conclusao.value,
            'situacao': situacao.value,
            'instituicao': instituicao.value,
            'prazo_entrega': prazo_entrega.value,
            'prorrogacao': prorrogacao.value,
            'tipo_tcc': tipo_tcc.value,
            'tema': tema.value,
            'bolsa': bolsa.value,
            'tipo_bolsa': tipo_bolsa.value,
            'vinculo': vinculo.value
        }
        # Chamar o método de atualização da DAO
        aluno_dao.update_aluno(aluno_data)
        nome_aluno.read_only = True
        telefone_aluno.read_only = True
        email_aluno.read_only = True
        orientador.read_only = True
        curso.read_only = True
        tipo_curso.read_only = True
        sigla_curso.read_only = True
        ano_ingresso.read_only = True
        ano_conclusao.read_only = True
        situacao.read_only = True
        instituicao.read_only = True
        prazo_entrega.read_only = True
        prorrogacao.read_only = True
        tipo_tcc.read_only = True
        tema.read_only = True
        bolsa.read_only = True
        tipo_bolsa.read_only = True
        vinculo.read_only = True
        botao_salvar_alunos.visible = False
        load_alunos()
        show_confirmation_dialog()
        page.update()

    def cls_show_confirmation_dialog(e):
        show_confirmation_dialog.open = False
        page.update()

    def show_confirmation_dialog():
        show_confirmation_dialog.open = True
        confirmation_dialog = ft.AlertDialog(
            title=ft.Text("Confirmação"),
            content=ft.Text("Operação realizada com sucesso."),
            actions=[
                ft.TextButton("OK", on_click=cls_show_confirmation_dialog)
            ]
        )
        page.dialog = confirmation_dialog
        confirmation_dialog.open = True
        page.update()

    def alert_update_dialog():
        alert_update_dialog.open = True
        confirmation_dialog = ft.AlertDialog(
            title=ft.Text("Atenção"),
            content=ft.Text("As alterações não poderão ser desfeitas."),
            actions=[
                ft.TextButton("OK", on_click=cls_show_confirmation_dialog)
            ]
        )
        page.dialog = confirmation_dialog
        confirmation_dialog.open = True
        page.update()

    # Garantir que todos os TextField são inicializados com read_only=True (orientadores)
    nome_orientador = ft.TextField(label="Nome", width=800, read_only=True)
    telefone_orientador = ft.TextField(label="Telefone", width=800, read_only=True)
    email_orientador = ft.TextField(label="Email", width=800, read_only=True)
    vinculo_orientador = ft.TextField(label="Vínculo", width=800, read_only=True)
    instituicao_orientador = ft.TextField(label="Instituição", width=800, read_only=True)
    

    def load_orientadores():
        orientadores = orientador_dao.get_orientadores()
        dropdown_orientadores.options = [ft.dropdown.Option(text=nome) for nome in orientadores]
        dropdown_orientadores.update()

    # Atualiza os campos com informações do orientador selecionado
    def on_orientador_selected(e):
        global id_orientador
        orientador_info = orientador_dao.get_orientador_info(e.control.value)
        if orientador_info:
            id_orientador = orientador_info[0]
            nome_orientador.value = orientador_info[1]
            telefone_orientador.value = orientador_info[2]
            email_orientador.value = orientador_info[3]
            vinculo_orientador.value = orientador_info[4]
            instituicao_orientador.value = orientador_info[5]
            for field in [nome_orientador, telefone_orientador, email_orientador, vinculo_orientador, instituicao_orientador]:
                field.update()

    # Conecte o evento de mudança do dropdown à função de atualização
    dropdown_orientadores.on_change = on_orientador_selected

    def botao_orientadores(e):
        menu_orientadores.visible = True
        nome_orientador.read_only = True
        telefone_orientador.read_only = True
        email_orientador.read_only = True
        vinculo_orientador.read_only = True
        instituicao_orientador.read_only = True
        # visibilidade dos botões
        botao_cadastro_cursos.visible = False
        dropdown_cursos.visible = False
        menu_cursos.visible = False
        botao_cadastro_alunos.visible = False
        dropdown_alunos.visible = False
        botao_salvar_alunos.visible = False
        menu_alunos.visible = False
        botao_cadastro_orientadores.visible = False
        botao_salvar_orientadores.visible = False
        dropdown_orientadores.visible = True
        menu_relatorios.visible=False
        # Limpa os valores
        dropdown_orientadores.value = ""
        nome_orientador.value = ""
        telefone_orientador.value = ""
        email_orientador.value = ""
        vinculo_orientador.value = ""
        instituicao_orientador.value = ""
        load_orientadores()
        page.update()

    def botao_atualizar_orientadores(e):
        nome_orientador.read_only = False
        telefone_orientador.read_only = False
        email_orientador.read_only = False
        vinculo_orientador.read_only = False
        instituicao_orientador.read_only = False
        # visibilidade dos botões
        botao_cadastro_cursos.visible = False
        dropdown_cursos.visible = False
        menu_cursos.visible = False
        botao_cadastro_alunos.visible = False
        dropdown_alunos.visible = False
        botao_salvar_alunos.visible = False
        menu_alunos.visible = False
        botao_salvar_orientadores.visible = True
        dropdown_orientadores.visible = True
        alert_update_dialog()
        load_orientadores()
        page.update()

    def botao_cadastrar_orientadores(e):
        nome_orientador.read_only = False
        telefone_orientador.read_only = False
        email_orientador.read_only = False
        vinculo_orientador.read_only = False
        instituicao_orientador.read_only = False
        # visibilidade dos botões
        botao_cadastro_cursos.visible = False
        dropdown_cursos.visible = False
        botao_salvar_cursos.visible = False
        menu_alunos.visible = False
        botao_cadastro_orientadores.visible = True
        dropdown_orientadores.visible = False
        botao_salvar_orientadores.visible = False
        botao_cadastro_cursos.visible = False
        dropdown_cursos.visible = False
        botao_cadastro_cursos.visible = True
        #limpar valores do textfield
        nome_orientador.value = ""
        telefone_orientador.value = ""
        email_orientador.value = ""
        vinculo_orientador.value = ""
        instituicao_orientador.value = ""
        alert_update_dialog()
        load_orientadores()
        page.update()

    def insert_new_orientador(e):
        orientador_data = {
            'nome': nome_orientador.value,
            'telefone': telefone_orientador.value,
            'email': email_orientador.value,
            'vinculo': vinculo_orientador.value,
            'instituicao': instituicao_orientador.value
        }
        # Chamar o método de atualização da DAO
        orientador_dao.insert_orientador(orientador_data)
        # retorna os campos para somente leitura
        nome_orientador.read_only = True
        telefone_orientador.read_only = True
        email_orientador.read_only = True
        vinculo_orientador.read_only = True
        instituicao_orientador.read_only = True
        show_confirmation_dialog()
        page.update()

    def save_orientador(e):
        # Coletar dados dos TextField
        orientador_data = {
            'id': int(id_orientador),
            'nome': nome_orientador.value,
            'telefone': telefone_orientador.value,
            'email': email_orientador.value,
            'vinculo': vinculo_orientador.value,
            'instituicao': instituicao_orientador.value
        }
        # Chamar o método de atualização da DAO
        orientador_dao.update_orientador(orientador_data)
        nome_orientador.read_only = True
        telefone_orientador.read_only = True
        email_orientador.read_only = True
        vinculo_orientador.read_only = True
        instituicao_orientador.read_only = True
        botao_salvar_orientadores.visible = False
        load_orientadores()
        show_confirmation_dialog()
        page.update()


    def cls_show_confirmation_dialog(e):
        show_confirmation_dialog.open = False
        page.update()

    def show_confirmation_dialog():
        show_confirmation_dialog.open = True
        confirmation_dialog = ft.AlertDialog(
            title=ft.Text("Confirmação"),
            content=ft.Text("Operação realizada com sucesso."),
            actions=[
                ft.TextButton("OK", on_click=cls_show_confirmation_dialog)
            ]
        )
        page.dialog = confirmation_dialog
        confirmation_dialog.open = True
        page.update()

    def alert_update_dialog():
        alert_update_dialog.open = True
        confirmation_dialog = ft.AlertDialog(
            title=ft.Text("Atenção"),
            content=ft.Text("As alterações não poderão ser desfeitas."),
            actions=[
                ft.TextButton("OK", on_click=cls_show_confirmation_dialog)
            ]
        )
        page.dialog = confirmation_dialog
        confirmation_dialog.open = True
        page.update()

    # Garantir que todos os TextField são inicializados com read_only=True (cursos)
    nome_curso = ft.TextField(label="Nome do curso", width=800, read_only=True)
    sigla = ft.TextField(label="Sigla do curso", width=800, read_only=True)

    def load_cursos():
        cursos = curso_dao.get_cursos()
        dropdown_cursos.options = [ft.dropdown.Option(text=nome_curso) for nome_curso in cursos]
        dropdown_cursos.update()

    # Atualiza os campos com informações do orientador selecionado
    def on_curso_selected(e):
        global id_curso
        curso_info = curso_dao.get_curso_info(e.control.value)
        if curso_info:
            id_curso = curso_info[0]
            nome_curso.value = curso_info[1]
            sigla.value = curso_info[2]
            for field in [nome_curso, sigla]:
                field.update()

    # Conecte o evento de mudança do dropdown à função de atualização
    dropdown_cursos.on_change = on_curso_selected

    def botao_cursos(e):
        menu_cursos.visible = True
        nome_curso.read_only = True
        sigla.read_only = True       
	    # visibilidade dos botões
        botao_cadastro_alunos.visible = False
        dropdown_alunos.visible = False
        botao_salvar_alunos.visible = False
        menu_alunos.visible = False
        botao_cadastro_orientadores.visible = False
        botao_cadastro_cursos.visible = False
        botao_salvar_orientadores.visible = False
        botao_salvar_cursos.visible = False
        dropdown_orientadores.visible = False
        menu_orientadores.visible = False
        dropdown_cursos.visible = True
        menu_relatorios.visible = False
        # Limpa os valores
        dropdown_cursos.value = ""
        nome_curso.value = ""
        sigla.value = ""
        load_cursos()
        page.update()

    def botao_atualizar_cursos(e):
        nome_curso.read_only = False
        sigla.read_only = False       
        # visibilidade dos botoes
        botao_cadastro_alunos.visible = False
        dropdown_alunos.visible = False
        botao_salvar_alunos.visible = False
        menu_alunos.visible = False
        botao_salvar_orientadores.visible = False
        dropdown_orientadores.visible = False
        menu_orientadores.visible = False
        botao_salvar_cursos.visible = True
        botao_cadastro_cursos.visible = False
        menu_relatorios.visible = False
        dropdown_cursos.visible = True
        alert_update_dialog()
        load_cursos()
        page.update()

    def botao_cadastrar_cursos(e):
        nome_curso.read_only = False
        sigla.read_only = False       
	    # visibilidade dos botões
        botao_cadastro_cursos.visible = False
        dropdown_cursos.visible = False
        botao_salvar_cursos.visible = False
        menu_alunos.visible = False
        botao_cadastro_orientadores.visible = False
        dropdown_orientadores.visible = False
        botao_salvar_orientadores.visible = False
        dropdown_cursos.visivle = False
        menu_relatorios.visible = False
        botao_cadastro_cursos.visible = True
        #limpar valores do textfield
        nome_curso.value = ""
        sigla.value = ""     
        alert_update_dialog()
        load_cursos()
        page.update()
    
    def insert_new_curso(e):
        curso_data = {
            'nome_curso': nome_curso.value,
            'sigla': sigla.value            
        }
        # Chamar o método de atualização da DAO
        curso_dao.insert_curso(curso_data)
	    # retorna os campos para somente leitura
        nome_curso.read_only = True
        sigla.read_only = True
        # tira a visibilidade do botao cadastro para evitar duplicatas
        botao_cadastro_alunos.visible = False
        show_confirmation_dialog()
        page.update()

    def save_curso(e):
        # Coletar dados dos TextField
        curso_data = {
            'nome_curso': nome_curso.value,
            'sigla': sigla.value,  
            'id': int(id_curso)
        }
        # Chamar o método de atualização da DAO
        curso_dao.update_curso(curso_data)
        nome_curso.read_only = True
        sigla.read_only = True      
        botao_salvar_cursos.visible = False
        load_cursos()
        show_confirmation_dialog()
        page.update()

    def cls_show_confirmation_dialog(e):
        show_confirmation_dialog.open = False
        page.update()

    def show_confirmation_dialog():
        show_confirmation_dialog.open = True
        confirmation_dialog = ft.AlertDialog(
            title=ft.Text("Confirmação"),
            content=ft.Text("Operação realizada com sucesso."),
            actions=[
                ft.TextButton("OK", on_click=cls_show_confirmation_dialog)
            ]
        )
        page.dialog = confirmation_dialog
        confirmation_dialog.open = True
        page.update()

    def alert_update_dialog():
        alert_update_dialog.open = True
        confirmation_dialog = ft.AlertDialog(
            title=ft.Text("Atenção"),
            content=ft.Text("As alterações não poderão ser desfeitas."),
            actions=[
                ft.TextButton("OK", on_click=cls_show_confirmation_dialog)
            ]
        )
        page.dialog = confirmation_dialog
        confirmation_dialog.open = True
        page.update()

    def botao_inicio(e):
        menu_alunos.visible = False
        menu_orientadores.visible = False
        menu_cursos.visible = False
        menu_relatorios.visible = False
        page.update()

    def botao_relatorios(e):
        menu_alunos.visible = False
        menu_orientadores.visible = False
        menu_cursos.visible = False
        menu_relatorios.visible = True
        load_cursos()
        load_orientadores()
        page.update()

    # Botões
    botao_salvar_alunos = ft.ElevatedButton(text="Salvar", width=200, on_click=save_aluno, visible=False)
    botao_cadastro_alunos = ft.ElevatedButton(text="Cadastrar", width=200, on_click=insert_new_aluno, visible=False)
    botao_salvar_orientadores = ft.ElevatedButton(text="Salvar", width=200, on_click=save_orientador, visible=False)
    botao_cadastro_orientadores = ft.ElevatedButton(text="Cadastrar", width=200, on_click=insert_new_orientador, visible=False)
    botao_salvar_cursos = ft.ElevatedButton(text="Salvar", width=200, on_click=save_curso)
    botao_cadastro_cursos = ft.ElevatedButton(text="Cadastrar", width=200, on_click=insert_new_curso)
    botao_exportar_relatorio = ft.ElevatedButton(text="Exportar relatório", width=200, on_click=export_to_excel)

    #menu de navegação
    menu_navigation = ft.Column(
            controls=[
                ft.ElevatedButton(text="Início", width=200, on_click=botao_inicio),
                ft.ElevatedButton(text="Alunos", width=200, on_click=botao_alunos),
                ft.ElevatedButton(text="Orientadores", width=200, on_click=botao_orientadores),
                ft.ElevatedButton(text="Cursos", width=200, on_click=botao_cursos),
                ft.ElevatedButton(text="Relatórios", width=200, on_click=botao_relatorios)
            ], width=200           
        )

    data_relatorios = ft.ResponsiveRow(
        controls=[
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            dropdown_filtro_cursos,
                            dropdown_filtro_orientadores,
                            dropdown_status,
                            botao_exportar_relatorio 
                        ]
                    ), datatable
                ]
            )
        ]
    )

    data_aluno = ft.Row(
        controls=[
            ft.Column(
                controls=[
                        nome_aluno, telefone_aluno, email_aluno, orientador,
                        curso, tipo_curso, sigla_curso, ano_ingresso, ano_conclusao, situacao,
                        instituicao, prazo_entrega, prorrogacao, tipo_tcc, tema, bolsa,
                        tipo_bolsa, vinculo, botao_salvar_alunos, botao_cadastro_alunos
                        ]
            )
        ]
    )

    data_orientador = ft.Row(
        controls=[
    ft.Column(
        controls=[
                nome_orientador, telefone_orientador, email_orientador, vinculo_orientador, instituicao_orientador,
                botao_salvar_orientadores, botao_cadastro_orientadores
                ]
    )
        ]
    )

    data_curso = ft.Row(
        controls=[
            ft.Column(
                controls=[
                        nome_curso, sigla,
                        botao_salvar_cursos, botao_cadastro_cursos
                        ]
                    )
                ]
            )

    menu_alunos = ft.Column(
                controls=[
                    ft.Row(
                    controls=[
                        ft.ElevatedButton(text="Cadastrar", width=200, on_click=botao_cadastrar_alunos),
                        ft.ElevatedButton(text="Atualizar", width=200, on_click=botao_atualizar_alunos)
                    ]
                    ), dropdown_alunos,
                    data_aluno
                ], visible=False
            )
    
    menu_orientadores = ft.Column(
                controls=[
                    ft.Row(
                    controls=[
                        ft.ElevatedButton(text="Cadastrar", width=200, on_click=botao_cadastrar_orientadores),
                        ft.ElevatedButton(text="Atualizar", width=200, on_click=botao_atualizar_orientadores)
                    ]
                    ),
                    dropdown_orientadores,
                    data_orientador
                ], visible=False
            )
    
    menu_cursos = ft.Column(
                controls=[
                    ft.Row(
                    controls=[
                        ft.ElevatedButton(text="Cadastrar", width=200, on_click=botao_cadastrar_cursos),
                        ft.ElevatedButton(text="Atualizar", width=200, on_click=botao_atualizar_cursos)
                    ]
                    ),
                    dropdown_cursos,
                    data_curso
                ], visible=False
            )
    
    menu_relatorios = ft.Column(
        controls=[
            data_relatorios
        ], visible=False
    )
    
    diviser = ft.VerticalDivider(width=2)

    main_menu = ft.Row(
        controls=[
            menu_navigation,
            diviser,
            menu_alunos,
            menu_orientadores,
            menu_cursos,
            menu_relatorios
        ], vertical_alignment=ft.CrossAxisAlignment.STRETCH
    )
    
    

    page.add(main_menu)
    load_alunos()

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8550)