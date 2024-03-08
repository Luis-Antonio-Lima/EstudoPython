import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout

class JanelaControles(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Clientes")
        self.setGeometry(15, 20, 500, 300)

        # criar um layout para organizar os componentes
        layout = QVBoxLayout()

        # Label para o título da janela
        label_titulo = QLabel("Gerenciar os Clientes")
        label_titulo.setStyleSheet("QLabel{font-size:30pt;color:#600;font-weight:bold}")

        # Criar elementos de texto para pedir ao usuário entrar com dados dos clientes.
        # Criaremos as labels(rótulo)
        label_nome = QLabel("Nome do Cliente:")
        label_nome.setStyleSheet("QLabel{font-family:arial; font-size:15pt; font-weight:bold}")
        label_email = QLabel("Email:")
        label_email.setStyleSheet("QLabel{font-family:arial; font-size:15pt; font-weight:bold}")
        label_telefone = QLabel("Telefone:")
        label_telefone.setStyleSheet("QLabel{font-family:arial; font-size:15pt; font-weight:bold}")

        # Criar elementos para que os usuário possam escrever o que as labels estão pedindo
        edit_nome = QLineEdit()
        edit_nome.setStyleSheet("QLineEdit{padding:10px; border-radius:10px; font-size:8.5pt; background-color: 000}")
        edit_email = QLineEdit()
        edit_email.setStyleSheet("QLineEdit{padding:10px; border-radius:10px; font-size:8.5pt; background-color: 000}")
        edit_telefone = QLineEdit()
        edit_telefone.setStyleSheet("QLineEdit{padding:10px; border-radius:10px; font-size:8.5pt; background-color: 000}")

        # Criar um controle de botão para realizar um possível cadastro
        botao_cadastro = QPushButton("Cadastrar")
        botao_cadastro.setStyleSheet("QWidget{background-color: #fff}")
        # Adicionar os controles de label e edit ao layout
        layout.addWidget(label_titulo)
        
        layout.addWidget(label_nome)
        layout.addWidget(edit_nome)

        layout.addWidget(label_email)
        layout.addWidget(edit_email)

        layout.addWidget(label_telefone)
        layout.addWidget(edit_telefone)

        layout.addWidget(botao_cadastro)
        
        # adicionar o layout na janela
        self.setLayout(layout)
        self.setStyleSheet("QWidget{background-color: #80d8ff}")

app = QApplication(sys.argv)
tela = JanelaControles()
tela.show()
app.exec_()