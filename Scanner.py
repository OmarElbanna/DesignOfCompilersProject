from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QAbstractItemView
from visual_automata.fa.dfa import VisualDFA
from automata.fa.dfa import DFA
from pandas import*
from graphviz import Digraph
from jupyterlab import*
from colormath import *


states = []
tokens = []
tokensTable=[]
tokentype = []

token = {
    '=': 'Equal operator',
    '<': 'Less than operator',
    '>': 'Greater than operator',
    '(': 'Open bracket',
    ')': 'Closed bracket',
    ';': 'Semicolon operator',
    '<=': 'Less than or equal',
    '>=': 'Greater than or equal',
    '&&': 'And operator',
    '||': 'Or operator',
    '!': 'Not operator'
}



def get_tokens():
    for i in tokensTable:
        if i in token.keys():
            tokentype.append(token.get(i))
        elif str(i[0]).isnumeric():
            tokentype.append("Number")
        else:
            tokentype.append("Identifier")


def scan():
    error = ""
    infl = open('inputfile.txt', 'r')
    xline = infl.readlines()
    state = "start"
    x = ""
    line = 0
    for i in xline:
        character = 0
        line += 1
        i = i + " "
        while character < len(i):
            if state == "start":
                if i[character] == '&' and i[character + 1] == '&':
                    tokens.append('&&')
                    tokensTable.append('&&')
                    character += 1
                elif i[character] == '|' and i[character + 1] == '|':
                    tokens.append('||')
                    tokensTable.append('||')
                    character += 1
                elif i[character] == '!':
                    tokens.append('!')
                    tokensTable.append('!')
                elif i[character] == '=':
                    tokens.append('=')
                    tokensTable.append('=')
                elif i[character] == '<' and i[character + 1] == '=':
                    tokens.append('<=')
                    tokensTable.append('<=')
                    character += 1
                elif i[character] == '<':
                    tokens.append('<')
                    tokensTable.append('<')
                elif i[character] == '>' and i[character + 1] == '=':
                    tokens.append('>=')
                    tokensTable.append('>=')
                    character += 1
                elif i[character] == '>':
                    tokens.append('>')
                    tokensTable.append('>')
                elif i[character] == '(':
                    tokens.append('(')
                    tokensTable.append('(')
                elif i[character] == ')':
                    tokens.append(')')
                    tokensTable.append(')')
                elif i[character].isalpha():
                    state = "letter"
                elif i[character].isdigit():
                    state = "Num"
                elif i[character].isspace():
                    pass
                else:
                    get_tokens()
                    error = f"token: {i[character]} is invalid in line: {line}"
                    return error
            if state == "letter":
                if i[character].isalpha() or i[character].isdigit():
                    x = x + i[character]

                elif not (i[character].isalpha() or i[character].isdigit()):
                    state = "start"
                    tokens.append("Identifier")
                    tokensTable.append(x)
                    character -= 1
                    x = ""

            if state == "decimal":
                if i[character].isdigit():
                    state = "Num"
                elif not i[character].isdigit():
                    x = x + i[character]
                    error = f"token: {x} is invalid in line: {line}"
                    get_tokens()
                    return error

            if state == "Num":
                if i[character].isdigit():
                    x = x + i[character]
                elif i[character].isalpha():
                    get_tokens()
                    error = f"invalid Number in line: {line}"
                    return error
                elif i[character] == ".":
                    state = "decimal"
                    x = x + i[character]
                else:
                    tokens.append("Number")
                    tokensTable.append(x)
                    character -= 1
                    state = "start"
                    x = ""
            character = character + 1

    get_tokens()
    return error


##  GUI CODE
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        # Form.setMaximumSize(1080, 720)
        Form.setMinimumSize(1080, 720)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.hide()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setMaximumSize(QtCore.QSize(403, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 1, 1, 1)
        self.tableWidget.setColumnWidth(0, 0)
        self.tableWidget.setColumnWidth(1, 0)
        self.tableWidget.resizeColumnsToContents()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.textEdit, self.pushButton)
        self.pushButton.clicked.connect(lambda: self.scan())
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pushButton_3.clicked.connect(lambda: self.GenerateDFA())
        self.pushButton_4.clicked.connect(lambda: self.ShowRegex())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Tiny Scanner"))
        Form.setWindowIcon(QtGui.QIcon('icon.png'))
        self.textEdit.setPlaceholderText(_translate("Form", "Please write your Code here..."))
        self.pushButton.setText(_translate("Form", "Scan Code"))
        self.pushButton_3.setText(_translate("Form", "DFA"))
        self.pushButton_4.setText(_translate("Form", "REGEX"))
        self.pushButton.setShortcut(_translate("Form", "Return"))
        self.label.setText(_translate("Form", "chars = [a-z A-Z]\nnums = [0-9]\noper=(<|=|<=|>|>=| || |&&)\n(!* (chars+ (nums|chars)* | nums+)) (oper !*(chars+(nums|chars)*|nums+))*\n"))
    def ShowRegex(self):
        self.label.show()
    def GenerateDFA(self):

        dfa = DFA(
            states={'q0', 'q1', 'q2','q3','Dead'},
            input_symbols={'Identifier', 'Number', '<', '<=', '=', '>', '>=','&&','||','!'},
            transitions={
                'q0': {'Identifier': 'q1', 'Number': 'q1', '<': 'Dead','>': 'Dead','<=': 'Dead','>=': 'Dead','=': 'Dead','&&': 'Dead','||': 'Dead','!': 'q0'},
                'q1': {'Number': 'Dead', 'Identifier': 'Dead', '||': 'q2', '&&': 'q2', '=': 'q2', '>': 'q2', '>=': 'q2', '<': 'q2', '<=': 'q2','!': 'Dead'},
                'q2': {'Identifier': 'q3', 'Number': 'q3', '&&': 'Dead', '||': 'Dead', '>': 'Dead', '>=': 'Dead', '<': 'Dead', '<=': 'Dead', '=': 'Dead','!': 'q2'},
                'q3': {'Identifier': 'Dead', 'Number': 'Dead', '<': 'q0', '>': 'q0', '<=': 'q0', '>=': 'q0', '=': 'q0', '&&': 'q0', '||': 'q0','!': 'Dead'},
                'Dead': {'Identifier': 'Dead', 'Number': 'Dead', '<': 'Dead', '>': 'Dead', '<=': 'Dead', '>=': 'Dead','=': 'Dead', '&&': 'Dead', '||': 'Dead','!': 'Dead'}
            },
            initial_state='q0',
            final_states={'q3','q1'}

        )
        if dfa.accepts_input(tokens):
            print("final state is :" + str(dfa.read_input(tokens)))
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("The last state is not accepted")
            msg.setWindowTitle("Error")
            msg.exec_()
        try:
            b = dfa.read_input_stepwise(tokens)
        except:
            print("not valid")
        count = 0
        try:
            for i in b:
                states.append(str(i))
                count += 1
        except:
            print("the last state is not valid")

        row = 0
        for x in states[1:]:
            col = 2
            cell = QTableWidgetItem(str(x))
            self.tableWidget.setItem(row, col, cell)
            cell.setTextAlignment(Qt.AlignCenter)
            row += 1
        visualizedDfa= VisualDFA(dfa)
        visualizedDfa.show_diagram(filename='DFA',view=True,state_seperation=5)
        print(states)
        states.clear()

    def scan(self):
        tokens.clear()
        tokensTable.clear()
        tokentype.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        s = self.textEdit.toPlainText()
        infl = open('inputfile.txt', 'w')
        infl.write(s)
        infl.close()
        t = scan()
        self.populateTable()
        print(tokens)
        print(tokentype)
        if t != "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Invalid Token!")
            msg.setInformativeText(t)
            msg.setWindowTitle("Error")
            msg.exec_()

    def populateTable(self):
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(len(tokens) - 1)
        self.tableWidget.setHorizontalHeaderLabels(['Token Name', 'Token Type', 'DFA State'])


        row = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row + 1)
        row = 0
        for r in tokensTable:
            col = 0
            cell = QTableWidgetItem(str(r))
            self.tableWidget.setItem(row, col, cell)
            cell.setTextAlignment(Qt.AlignCenter)
            row += 1

        row = 0
        for r in tokentype:
            col = 1
            cell = QTableWidgetItem(str(r))
            self.tableWidget.setItem(row, col, cell)
            cell.setTextAlignment(Qt.AlignCenter)
            row += 1




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
