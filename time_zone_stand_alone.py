from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import os
from PyQt5.QtMultimedia import QSound
from forex_time_zone import Ui_Dialog
from datetime import datetime as dt


class forex_time_zone(Ui_Dialog):
    """
    Forex market zone to be implement in an overall interface
    """
    def __init__(self, w):
        self.setupUi(w)
        self.current_hour = dt.now().hour
        self.hour_operation_london = [hour for hour in range(3,12)]
        self.hour_operation_new_york = [hour for hour in range(8,17)]
        self.hour_operation_sydney = [hour for hour in range(17,25)]+[1]
        self.hour_operation_tokyo = [hour for hour in range(19,25)]+[1,2,3]
        self.layout_time_set_up()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.check_zone_change)
        self.timer.setInterval(60000)
        self.timer.setSingleShot(False)
        self.timer.start()
        self.current_market = list()


    def layout_time_set_up(self):
        """
        Create the qtable layout
        """
        self.tableWidget =  QtWidgets.QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(24)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.tableWidget.setHorizontalHeaderLabels([str(i) for i in range(1,25)])
        index_vertical = ["London","New York","Sydney","Tokyo"]
        self.tableWidget.setVerticalHeaderLabels(index_vertical)
        self.verticalLayout.addWidget(self.tableWidget)

        self.set_zone_color_mark()
        self.check_zone_change(opening_gui=True)

    def set_zone_color_mark(self):
        """
        Set the color of the background by zone
        """
        for i in range(0,4):
            if i==0:
                list_hour = self.hour_operation_london
                color = QtCore.Qt.green
            elif i==1:
                list_hour = self.hour_operation_new_york
                color = QtCore.Qt.red
            elif i==2:
                list_hour = self.hour_operation_sydney
                color = QtCore.Qt.darkMagenta
            elif i ==3:
                list_hour = self.hour_operation_tokyo
                color = QtCore.Qt.yellow
            for j in list_hour:
                self.tableWidget.setItem(i,j-1,QtWidgets.QTableWidgetItem())
                self.tableWidget.item(i,j-1).setBackground(color)

    def check_zone_change(self,opening_gui=False):
        """
        place a marker on the zone of the current market(s)
        """
        if self.current_hour<dt.now().hour or (self.current_hour==24 and dt.now().hour==0) or opening_gui:
            self.set_zone_color_mark()
            self.current_hour = dt.now().hour
            self.current_market = list()
            color = QtCore.Qt.darkGray
            if self.current_hour in self.hour_operation_london:
                self.tableWidget.item(0,self.current_hour-1).setBackground(color)
                self.current_market.append("London")

            if self.current_hour in self.hour_operation_new_york:
                self.tableWidget.item(1,self.current_hour-1).setBackground(color)
                self.current_market.append("New york")

            if self.current_hour in self.hour_operation_sydney:
                self.tableWidget.item(2,self.current_hour-1).setBackground(color)
                self.current_market.append("Sydney")

            if self.current_hour in self.hour_operation_tokyo:
                self.tableWidget.item(3,self.current_hour-1).setBackground(color)
                self.current_market.append("Tokyo")
def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QDialog()
    prog = forex_time_zone(w)
    w.show()
    app.exec_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 