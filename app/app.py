from PySide2 import QtWidgets

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculatrice") 
        self.setup_ui()           
        self.set_default_value()  # definir des valeurs par defaut dans les champs
        self.setup_connections()  
        self.resize(300, 100)



    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)    #QVBoxLayout ==> Pour avoir une disposition verticale

        # Definition de widgets :
        self.le_v1 = QtWidgets.QLineEdit()
        self.le_v2 = QtWidgets.QLineEdit()
        self.cbb_ops = QtWidgets.QComboBox()
        self.le_result = QtWidgets.QLineEdit()
        self.btn_calc = QtWidgets.QPushButton("=")
        self.btn_clear = QtWidgets.QPushButton("Reset")

        # Ajouter les widgets dans le Layout :
        self.main_layout.addWidget(self.le_v1)
        self.main_layout.addWidget(self.cbb_ops)
        self.main_layout.addWidget(self.le_v2)
        self.main_layout.addWidget(self.btn_calc)
        self.main_layout.addWidget(self.btn_clear)
        self.main_layout.addWidget(self.le_result)



    def set_default_value(self):
        
        self.le_v1.setText("")
        self.le_v2.setText("")
        self.le_result.setText("0")
        self.cbb_ops.addItems(["+", "-", "*", "/", "%"])

    def setup_connections(self):
        self.btn_calc.clicked.connect(self.calc)
        self.btn_clear.clicked.connect(self.clear)
    
    def calc(self):
        v1 = self.le_v1.text()
        v2 = self.le_v2.text()
        ops = self.cbb_ops.currentText()
        if v1 == "" or v2 =="":
            self.le_result.setText ("Input Error")
        else:
            if v1.isdigit() and v2.isdigit():
                if ops == "+":
                    #rslt = int(v1) + int(v2)
                    self.le_result.setText (str(int(v1) + int(v2)))
                elif ops == "-":
                    #rslt = int(v1) - int(v2)
                    self.le_result.setText (str(int(v1) - int(v2)))
                elif ops == "*":
                    #rslt = int(v1) * int(v2)
                    self.le_result.setText (str(int(v1) * int(v2)))
                elif ops == "/":
                    #rslt = int(v1) / int(v2)
                    self.le_result.setText (str(int(v1) / int(v2)))
                elif ops == "%":
                    #rslt = int(v1) % int(v2)
                    self.le_result.setText (str(int(v1) % int(v2)))
            else:
                print("Input Error")
                self.le_result.setText ("Input Error")
        

    def clear(self):
        self.le_result.setText ("0")
        self.le_v1.setText("")
        self.le_v2.setText("") 

app = QtWidgets.QApplication([])      # creer une application
win = App()                           # utiliser pour afficher la fenetre
win.show()                            #  afficher le widget

app.exec_()