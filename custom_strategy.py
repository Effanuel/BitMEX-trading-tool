import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QPushButton, QRadioButton, QLineEdit, QVBoxLayout, QLabel


from market_maker.market_maker import OrderManager
from market_maker.main import Ui

from market_maker.utils.math import orders_distribution


class CustomOrderManager(OrderManager, Ui):
    """A sample order manager for implementing your own custom strategy"""

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        OrderManager.__init__(self)

        # super(OrderManager, self).__init__()

    def start123(self) -> None:
        self.window = Ui.__init__(self)
        self.app.exec_()

    def submitOrder(self) -> None:
        print(self.start.text(), self.end.text(), "OK")
        props = {
            "quantity": float(self.quantity.text()),
            "n_tp": int(self.n_tp.text()),  # has to be whole number
            "start": self.start.text(),
            "end": self.end.text(),
            "side": self.side,
            "symbol": self.symbol,
        }

        print("start", self.start)
        bulk_orders = orders_distribution(self.distribution, props)

        # bulk_orders.append({"price": 8000.0, "orderQty": 100, "side": "Buy"})
        # bulk_orders.append({"price": 8800.0, "orderQty": 100, "side": "Buy"})
        # bulk_orders.append({"price": 8888.0, "orderQty": 100, "side": "Buy"})
        try:
            self.exchange.create_bulk_orders(bulk_orders)
        except Exception as e:
            self.error.setText(str(e))

    def place_orders(self) -> None:
        # implement your custom strategy here
        print("converge")
        buy_orders = []
        sell_orders = []

        # populate buy and sell orders, e.g.
        # buy_orders.append({'price': 999.0, 'orderQty': 100, 'side': "Buy"})
        # sell_orders.append({'price': 1001.0, 'orderQty': 100, 'side': "Sell"})

        # self.converge_orders(buy_orders, sell_orders)

    def run_loop(self):
        print("loop")


def run() -> None:
    order_manager = CustomOrderManager()

    # Try/except just keeps ctrl-c from printing an ugly stacktrace
    try:
        print("order 111")
        order_manager.start123()
        # order_manager.run_loop()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()


if __name__ == "__main__":
    run()

