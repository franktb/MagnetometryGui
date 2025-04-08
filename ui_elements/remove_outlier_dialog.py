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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_RemoveOutlierDialog(object):
    def setupUi(self, RemoveOutlierDialog):
        if not RemoveOutlierDialog.objectName():
            RemoveOutlierDialog.setObjectName(u"RemoveOutlierDialog")
        RemoveOutlierDialog.resize(471, 419)
        self.lineEdit_maxMagField = QLineEdit(RemoveOutlierDialog)
        self.lineEdit_maxMagField.setObjectName(u"lineEdit_maxMagField")
        self.lineEdit_maxMagField.setGeometry(QRect(190, 20, 113, 27))
        self.lineEdit_minMagField = QLineEdit(RemoveOutlierDialog)
        self.lineEdit_minMagField.setObjectName(u"lineEdit_minMagField")
        self.lineEdit_minMagField.setGeometry(QRect(190, 60, 113, 27))
        self.lineEdit_maxLongVal = QLineEdit(RemoveOutlierDialog)
        self.lineEdit_maxLongVal.setObjectName(u"lineEdit_maxLongVal")
        self.lineEdit_maxLongVal.setGeometry(QRect(190, 100, 113, 27))
        self.lineEdit_minLongVal = QLineEdit(RemoveOutlierDialog)
        self.lineEdit_minLongVal.setObjectName(u"lineEdit_minLongVal")
        self.lineEdit_minLongVal.setGeometry(QRect(190, 140, 113, 27))
        self.label = QLabel(RemoveOutlierDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 20, 141, 19))
        self.label_2 = QLabel(RemoveOutlierDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 60, 131, 20))
        self.label_3 = QLabel(RemoveOutlierDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 100, 101, 20))
        self.label_4 = QLabel(RemoveOutlierDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 140, 91, 19))
        self.submitButton = QPushButton(RemoveOutlierDialog)
        self.submitButton.setObjectName(u"submitButton")
        self.submitButton.setGeometry(QRect(340, 220, 88, 27))
        self.lineEdit_minLatVal = QLineEdit(RemoveOutlierDialog)
        self.lineEdit_minLatVal.setObjectName(u"lineEdit_minLatVal")
        self.lineEdit_minLatVal.setGeometry(QRect(190, 220, 113, 27))
        self.lineEdit_maxLatVal = QLineEdit(RemoveOutlierDialog)
        self.lineEdit_maxLatVal.setObjectName(u"lineEdit_maxLatVal")
        self.lineEdit_maxLatVal.setGeometry(QRect(190, 180, 113, 27))
        self.label_5 = QLabel(RemoveOutlierDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 220, 91, 20))
        self.label_6 = QLabel(RemoveOutlierDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 180, 91, 20))

        self.retranslateUi(RemoveOutlierDialog)

        QMetaObject.connectSlotsByName(RemoveOutlierDialog)
    # setupUi

    def retranslateUi(self, RemoveOutlierDialog):
        RemoveOutlierDialog.setWindowTitle(QCoreApplication.translate("RemoveOutlierDialog", u"Remove Outlier", None))
        self.label.setText(QCoreApplication.translate("RemoveOutlierDialog", u"Max Magnetic Field", None))
        self.label_2.setText(QCoreApplication.translate("RemoveOutlierDialog", u"Min Magnetic Field", None))
        self.label_3.setText(QCoreApplication.translate("RemoveOutlierDialog", u"Max Long Val", None))
        self.label_4.setText(QCoreApplication.translate("RemoveOutlierDialog", u"Min Long Val", None))
        self.submitButton.setText(QCoreApplication.translate("RemoveOutlierDialog", u"Submit", None))
        self.label_5.setText(QCoreApplication.translate("RemoveOutlierDialog", u"Min Lat Val", None))
        self.label_6.setText(QCoreApplication.translate("RemoveOutlierDialog", u"Max Lat Val", None))
    # retranslateUi

