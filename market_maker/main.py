from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtWidgets import QPushButton, QRadioButton, QLineEdit, QVBoxLayout, QLabel


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi("TradingUI.ui", self)  # Load the .ui file
        # =================================================
        self.quantity = self.findChild(QLineEdit, "quantity")
        self.n_tp = self.findChild(QLineEdit, "n_tp")
        self.start = self.findChild(QLineEdit, "start")
        self.end = self.findChild(QLineEdit, "end")
        self.side = "Sell"
        self.distribution = "uniform"
        self.symbol = "XBTUSD"

        # self.error = self.findChild(QLabel, 'currentPrice').text()

        self.error = self.findChild(QLabel, "currentPrice")
        # =================================================
        self.submitButton = self.findChild(QPushButton, "submit")
        self.submitButton.clicked.connect(self.submitOrder)

        # SIDE
        layoutSide = self.findChild(QVBoxLayout, "side")
        # SELL
        self.sellRadio = self.findChild(QRadioButton, "Sell")
        self.sellRadio.setChecked(True)
        self.sellRadio.toggled.connect(lambda: self.__setSide(self.sellRadio))
        # BUY
        self.buyRadio = self.findChild(QRadioButton, "Buy")
        self.buyRadio.toggled.connect(lambda: self.__setSide(self.buyRadio))

        # DISTRIBUTION
        layoutDistribution = self.findChild(QVBoxLayout, "distribution")
        # UNIFORM
        self.uniformRadio = self.findChild(QRadioButton, "uniform")
        self.uniformRadio.setChecked(True)
        self.uniformRadio.toggled.connect(
            lambda: self.__setDistribution(self.uniformRadio)
        )
        # NORMAL
        self.normalRadio = self.findChild(QRadioButton, "normal")
        self.normalRadio.toggled.connect(
            lambda: self.__setDistribution(self.normalRadio)
        )
        # POSITIVE
        self.positiveRadio = self.findChild(QRadioButton, "positive")
        self.positiveRadio.toggled.connect(
            lambda: self.__setDistribution(self.positiveRadio)
        )
        # NEGATIVE
        self.negativeRadio = self.findChild(QRadioButton, "negative")
        self.negativeRadio.toggled.connect(
            lambda: self.__setDistribution(self.negativeRadio)
        )
        # ADDING TO LAYOUT
        layoutSide.addWidget(self.sellRadio)
        layoutSide.addWidget(self.buyRadio)
        layoutDistribution.addWidget(self.uniformRadio)
        layoutDistribution.addWidget(self.normalRadio)
        layoutDistribution.addWidget(self.positiveRadio)
        layoutDistribution.addWidget(self.negativeRadio)

        self.show()  # Show the GUI

    def submitOrder(self):
        print(f"pressed button {self.start.text()} {self.distribution}")

    def __setSide(self, radio):
        if radio.text() == "Sell" and radio.isChecked():
            self.side = radio.text()
        elif radio.text() == "Buy" and radio.isChecked():
            self.side = radio.text()

    def __setDistribution(self, radio):
        if radio.text() == "uniform" and radio.isChecked():
            self.distribution = radio.text()
        elif radio.text() == "normal" and radio.isChecked():
            self.distribution = radio.text()
        elif radio.text() == "positive" and radio.isChecked():
            self.distribution = radio.text()
        elif radio.text() == "negative" and radio.isChecked():
            self.distribution = radio.text()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()


if __name__ == "__main__":
    main()
