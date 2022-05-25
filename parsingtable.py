# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parsingtable.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QAbstractItemView


class Ui_ParsingTable(object):
    def setupUi(self, ParsingTable):
        ParsingTable.setObjectName("ParsingTable")
        ParsingTable.resize(1024, 335)
        ParsingTable.setWindowIcon(QtGui.QIcon('table.png'))
        self.tableWidget = QtWidgets.QTableWidget(ParsingTable)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1921, 561))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 7, item)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)



        self.retranslateUi(ParsingTable)
        QtCore.QMetaObject.connectSlotsByName(ParsingTable)

    def retranslateUi(self, ParsingTable):
        _translate = QtCore.QCoreApplication.translate
        ParsingTable.setWindowTitle(_translate("ParsingTable", "Parsing Table"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("ParsingTable", "exp"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("ParsingTable", "term"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("ParsingTable", "factor"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("ParsingTable", "comop"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("ParsingTable", "operand"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("ParsingTable", "exp\'"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("ParsingTable", "term\'"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("ParsingTable", "factor\'"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ParsingTable", "Identifier"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ParsingTable", ">"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ParsingTable", "<"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ParsingTable", "="))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ParsingTable", "||"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ParsingTable", "&&"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("ParsingTable", "!"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("ParsingTable", "$"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("ParsingTable", "exp->term exp\'"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("ParsingTable", "exp->term exp\'"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("ParsingTable", "term->factor term\'"))
        item = self.tableWidget.item(1, 6)
        item.setText(_translate("ParsingTable", "term->factor term\'"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("ParsingTable", "factor->operand factor\'"))
        item = self.tableWidget.item(2, 6)
        item.setText(_translate("ParsingTable", "factor->operand factor\'"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("ParsingTable", "comop->>"))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("ParsingTable", "comop-><"))
        item = self.tableWidget.item(3, 3)
        item.setText(_translate("ParsingTable", "comop->="))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("ParsingTable", "operand->identifier"))
        item = self.tableWidget.item(4, 6)
        item.setText(_translate("ParsingTable", "operand->! operand"))
        item = self.tableWidget.item(5, 4)
        item.setText(_translate("ParsingTable", "exp\'->|| term exp\'"))
        item = self.tableWidget.item(5, 7)
        item.setText(_translate("ParsingTable", "exp\'->e"))
        item = self.tableWidget.item(6, 4)
        item.setText(_translate("ParsingTable", "term\'->e"))
        item = self.tableWidget.item(6, 5)
        item.setText(_translate("ParsingTable", "term\'->&& factor term\'"))
        item = self.tableWidget.item(6, 7)
        item.setText(_translate("ParsingTable", "term\'->e"))
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("ParsingTable", "factor\'->comop operand factor\'"))
        item = self.tableWidget.item(7, 2)
        item.setText(_translate("ParsingTable", "factor\'->comop operand factor\'"))
        item = self.tableWidget.item(7, 3)
        item.setText(_translate("ParsingTable", "factor\'->comop operand factor\'"))
        item = self.tableWidget.item(7, 4)
        item.setText(_translate("ParsingTable", "factor\'->e"))
        item = self.tableWidget.item(7, 5)
        item.setText(_translate("ParsingTable", "factor\'->e"))
        item = self.tableWidget.item(7, 7)
        item.setText(_translate("ParsingTable", "factor\'->e"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ParsingTable = QtWidgets.QWidget()
    ui = Ui_ParsingTable()
    ui.setupUi(ParsingTable)
    ParsingTable.show()
    sys.exit(app.exec_())