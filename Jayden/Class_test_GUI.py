from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog	
import sys
from class_test import Artikel

banana = Artikel("Banane",2.5,500)  # Define the 'banana' variable here as well


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 240, 241, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.show_banana_dialog)
        self.pushButton.setText("Buy Bananas\n2.5€ per banana\n500 in stock")
        self.pushButton.setGeometry(QtCore.QRect(280, 240, 241, 171))
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setObjectName("Restock Bananas")
        self.pushButton2.clicked.connect(self.restock_banana)
        self.pushButton2.setText("Restock Bananas")
        self.pushButton2.setGeometry(QtCore.QRect(280, 431, 241, 50))
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    def restock_banana(self):
        banana.auffuellen(500)
        self.pushButton.setText(f"Buy Bananas\n2.5€ per banana\n{banana.bestand} in stock")

    def show_banana_dialog(self):
        num_bananas, ok = QtWidgets.QInputDialog.getInt(self.centralwidget, "Banana Quantity", "Enter the quantity of bananas:")
        if ok:
            self.buy_bananas(num_bananas)


    def buy_bananas(self, quantity):
        if banana.kaufen(quantity):
            price=2.5*quantity
            print(f"Du hast {quantity} Bananen für {price}€ gekauft.")
            banana.anzeigen()
            self.pushButton.setText(f"Buy Bananas\n2.5€ per banana\n{banana.bestand} in stock")
        else:
            print("Nicht genug Bananen auf Lager.")







if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
            


    
