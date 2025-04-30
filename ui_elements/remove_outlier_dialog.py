# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'remove_outlier_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_RemoveOutlierDialog(object):
    def setupUi(self, RemoveOutlierDialog):
        if not RemoveOutlierDialog.objectName():
            RemoveOutlierDialog.setObjectName(u"RemoveOutlierDialog")
        RemoveOutlierDialog.resize(437, 345)
        self.submitButton = QPushButton(RemoveOutlierDialog)
        self.submitButton.setObjectName(u"submitButton")
        self.submitButton.setGeometry(QRect(290, 260, 88, 27))
        self.widget = QWidget(RemoveOutlierDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 20, 329, 227))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_maxMagField = QLineEdit(self.widget)
        self.lineEdit_maxMagField.setObjectName(u"lineEdit_maxMagField")

        self.gridLayout.addWidget(self.lineEdit_maxMagField, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_minMagField = QLineEdit(self.widget)
        self.lineEdit_minMagField.setObjectName(u"lineEdit_minMagField")

        self.gridLayout.addWidget(self.lineEdit_minMagField, 1, 1, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_maxLongVal = QLineEdit(self.widget)
        self.lineEdit_maxLongVal.setObjectName(u"lineEdit_maxLongVal")

        self.gridLayout.addWidget(self.lineEdit_maxLongVal, 2, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.lineEdit_minLongVal = QLineEdit(self.widget)
        self.lineEdit_minLongVal.setObjectName(u"lineEdit_minLongVal")

        self.gridLayout.addWidget(self.lineEdit_minLongVal, 3, 1, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.lineEdit_maxLatVal = QLineEdit(self.widget)
        self.lineEdit_maxLatVal.setObjectName(u"lineEdit_maxLatVal")

        self.gridLayout.addWidget(self.lineEdit_maxLatVal, 4, 1, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.lineEdit_minLatVal = QLineEdit(self.widget)
        self.lineEdit_minLatVal.setObjectName(u"lineEdit_minLatVal")

        self.gridLayout.addWidget(self.lineEdit_minLatVal, 5, 1, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 6, 1, 1, 1)


        self.retranslateUi(RemoveOutlierDialog)

        QMetaObject.connectSlotsByName(RemoveOutlierDialog)
    # setupUi

    def retranslateUi(self, RemoveOutlierDialog):
        RemoveOutlierDialog.setWindowTitle(QCoreApplication.translate("RemoveOutlierDialog", u"Remove Outlier", None))
        self.submitButton.setText(QCoreApplication.translate("RemoveOutlierDialog", u"Submit", None))
        self.label.setText(QCoreApplication.translate("RemoveOutlierDialog", u"Max Magnetic Field:", None))
        self.lineEdit_maxMagField.setText(QCoreApplication.translate("RemoveOutlierDialog", u"49000", None))
        self.label_2.setText(QCoreApplication.translate("RemoveOutlierDialog", u"Min Magnetic Field:", None))
        self.lineEdit_minMagField.setText(QCoreApplication.translate("RemoveOutlierDialog", u"48000", None))
        self.label_3.setText(QCoreApplication.translate("RemoveOutlierDialog", u"Max Long Val:", None))
        self.lineEdit_maxLongVal.setText(QCoreApplication.translate("RemoveOutlierDialog", u"-7.2", None))
        self.label_4.setText(QCoreApplication.translate("RemoveOutlierDialog", u"Min Long Val:", None))
        self.lineEdit_minLongVal.setText(QCoreApplication.translate("RemoveOutlierDialog", u"-8.7", None))
        self.label_6.setText(QCoreApplication.translate("RemoveOutlierDialog", u"Max Lat Val:", None))
        self.lineEdit_maxLatVal.setText(QCoreApplication.translate("RemoveOutlierDialog", u"52.", None))
        self.label_5.setText(QCoreApplication.translate("RemoveOutlierDialog", u"Min Lat Val:", None))
        self.lineEdit_minLatVal.setText(QCoreApplication.translate("RemoveOutlierDialog", u"51.", None))
        self.label_7.setText(QCoreApplication.translate("RemoveOutlierDialog", u"Action:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("RemoveOutlierDialog", u"Remove entry", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("RemoveOutlierDialog", u"Use last value", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("RemoveOutlierDialog", u"Interpolate neighbours", None))

    # retranslateUi

