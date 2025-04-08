import flet as ft
import math

# Flet sempre abre uma tela de desktop basicamente até a linha 7 foi configurando isso

# Configurando a página básica de onde a calculadora irá aparecer
def main(page: ft.Page):
    page.title = 'Calculadora'
    page.bgcolor = '#2d2d2d'
    page.window.width = 350
    page.window.height = 300

    todos_valores = ""  # Iniciando a variável vazia para receber os valores

    # Criando a parte onde o resultado é mostrado, basicamente a parte de cima da calculadora
    resultado_texto = ft.Text(value='0', size=28, color='white', text_align='right')

    # Define a função "entrar_valores", que será chamada quando o usuário clicar em algo

    #non local serve para não armazenar na váriavel global os valores
    def entrar_valores(e):
        nonlocal todos_valores
        todos_valores += str(e.control.text)
        resultado_texto.value = todos_valores
        page.update()

    # Define a função "limpar_tela" para resetar os valores
    def limpar_tela(e):
        nonlocal todos_valores
        todos_valores = ""  # Corrigido para atribuir em vez de comparar
        resultado_texto.value = '0'  # Corrigido para usar string
        page.update()

    # Define a função "calcular" para realizar operações matemáticas
    def calcular(e):
        nonlocal todos_valores
        try:
            # Função eval que faz as contas matemáticas e str converte o valor para string
            resultado_texto.value = str(eval(todos_valores))
            todos_valores = resultado_texto.value
        except:
            resultado_texto.value = 'Erro'
            todos_valores = ''
        page.update()

    def raiz_quadrada(e):
        nonlocal todos_valores
        conversao = float(todos_valores)
        resultado_texto.value = math.sqrt(conversao)
        todos_valores = str(resultado_texto.value)
        page.update()

    def potencia(e):
        nonlocal todos_valores
        conversao = float(todos_valores)
        resultado_texto.value = (conversao**2)
        todos_valores = str(resultado_texto.value)
        page.update()

    def divisao_por_um(e):
        nonlocal todos_valores
        conversao = float(todos_valores)
        resultado_texto.value = float(1 / conversao)
        todos_valores = str(resultado_texto.value)
        page.update()

    def ultimo_digito(e):
        nonlocal todos_valores
        todos_valores = todos_valores[:-1]
        resultado_texto.value = todos_valores
        page.update()
    
    # Configurando a tela do resultado
    tela = ft.Container(
        content=resultado_texto,
        bgcolor="#37474F",
        padding=10,
        border_radius=10,
        height=70,
        alignment=ft.alignment.center_right,
    )

    # Estilização dos botões
    estilo_numeros = {
        "height": 60,
        "bgcolor": "#4d4d4d",
        "color": "white",
        "expand": 1,
    }

    estilo_operadores = {
        "height": 60,
        "bgcolor": "#FF9500",
        "color": "white",
        "expand": 1,
    }

    estilo_limpar = {
        "height": 60,
        "bgcolor": "#FF3B30",
        "color": "white",
        "expand": 1,
    }

    estilo_igual = {
        "height": 60,
        "bgcolor": "#34C759",
        "color": "white",
        "expand": 1,
    }

    # Grade de botões da calculadora
    grade_de_botoes = [
        [
            ('%', estilo_operadores, entrar_valores),
            ('/', estilo_operadores, entrar_valores),
            ('*', estilo_operadores, entrar_valores),
            ('C', estilo_limpar, limpar_tela),
        ],
        [
            ('⨉²',estilo_operadores, potencia,entrar_valores),
            ('√', estilo_operadores, raiz_quadrada,entrar_valores),
            ('¹⁄ₓ', estilo_operadores, divisao_por_um,entrar_valores),
            ('CE', estilo_limpar, ultimo_digito,entrar_valores),
        ],
        [
            ('7', estilo_numeros, entrar_valores),
            ('8', estilo_numeros, entrar_valores),
            ('9', estilo_numeros, entrar_valores),
            ('-', estilo_operadores, entrar_valores),
        ],
        [
            ('4', estilo_numeros, entrar_valores),
            ('5', estilo_numeros, entrar_valores),
            ('6', estilo_numeros, entrar_valores),
            ('+', estilo_operadores, entrar_valores),
        ],
        [
            ('1', estilo_numeros, entrar_valores),
            ('2', estilo_numeros, entrar_valores),
            ('3', estilo_numeros, entrar_valores),
            ('=', estilo_igual, calcular),
        ],
        [  # Alterando o estilo do 0 pois ele é diferente
            ('0', {**estilo_numeros, "expand": 2}, entrar_valores),
            ('.', estilo_numeros, entrar_valores),
            ('⌫', estilo_operadores, ultimo_digito),
        ],
        
    ]

    botoes = []

    # Criação dos botões
    for linha in grade_de_botoes:
        linha_control = []
        for texto, estilo, handler, *_ in linha:
            botao = ft.ElevatedButton(
                text=texto,
                on_click=handler,**estilo,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    padding=0,
                ),
            )
            linha_control.append(botao)
        botoes.append(ft.Row(linha_control, spacing=5))

    # Criando a coluna principal
    page.add(
        ft.Column(
            [
                tela,
                ft.Column(botoes, spacing=5)
            ]
        )
    )


ft.app(target=main)