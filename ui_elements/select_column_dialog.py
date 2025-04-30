# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_column_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_ColumnSelectDialog(object):
    def setupUi(self, ColumnSelectDialog):
        if not ColumnSelectDialog.objectName():
            ColumnSelectDialog.setObjectName(u"ColumnSelectDialog")
        ColumnSelectDialog.resize(448, 445)
        self.label_7 = QLabel(ColumnSelectDialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 20, 66, 19))
        font = QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.lineEdit_file_path = QLineEdit(ColumnSelectDialog)
        self.lineEdit_file_path.setObjectName(u"lineEdit_file_path")
        self.lineEdit_file_path.setGeometry(QRect(40, 60, 350, 27))
        self.selectFileButton = QPushButton(ColumnSelectDialog)
        self.selectFileButton.setObjectName(u"selectFileButton")
        self.selectFileButton.setGeometry(QRect(300, 20, 88, 27))
        self.submitButton = QPushButton(ColumnSelectDialog)
        self.submitButton.setObjectName(u"submitButton")
        self.submitButton.setGeometry(QRect(300, 370, 88, 27))
        self.layoutWidget = QWidget(ColumnSelectDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 100, 351, 260))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_time = QLineEdit(self.layoutWidget)
        self.lineEdit_time.setObjectName(u"lineEdit_time")

        self.gridLayout.addWidget(self.lineEdit_time, 0, 1, 1, 1)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.lineEdit_day = QLineEdit(self.layoutWidget)
        self.lineEdit_day.setObjectName(u"lineEdit_day")

        self.gridLayout.addWidget(self.lineEdit_day, 1, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit_mag_field = QLineEdit(self.layoutWidget)
        self.lineEdit_mag_field.setObjectName(u"lineEdit_mag_field")

        self.gridLayout.addWidget(self.lineEdit_mag_field, 2, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.lineEdit_Gps_lat = QLineEdit(self.layoutWidget)
        self.lineEdit_Gps_lat.setObjectName(u"lineEdit_Gps_lat")

        self.gridLayout.addWidget(self.lineEdit_Gps_lat, 3, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.lineEdit_Gps_long = QLineEdit(self.layoutWidget)
        self.lineEdit_Gps_long.setObjectName(u"lineEdit_Gps_long")

        self.gridLayout.addWidget(self.lineEdit_Gps_long, 4, 1, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.lineEdit_Gps_easting = QLineEdit(self.layoutWidget)
        self.lineEdit_Gps_easting.setObjectName(u"lineEdit_Gps_easting")

        self.gridLayout.addWidget(self.lineEdit_Gps_easting, 5, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.lineEdit_Gps_northing = QLineEdit(self.layoutWidget)
        self.lineEdit_Gps_northing.setObjectName(u"lineEdit_Gps_northing")

        self.gridLayout.addWidget(self.lineEdit_Gps_northing, 6, 1, 1, 1)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)

        self.lineEdit_skipHeaderRows = QLineEdit(self.layoutWidget)
        self.lineEdit_skipHeaderRows.setObjectName(u"lineEdit_skipHeaderRows")

        self.gridLayout.addWidget(self.lineEdit_skipHeaderRows, 7, 1, 1, 1)


        self.retranslateUi(ColumnSelectDialog)

        QMetaObject.connectSlotsByName(ColumnSelectDialog)
    # setupUi

    def retranslateUi(self, ColumnSelectDialog):
        ColumnSelectDialog.setWindowTitle(QCoreApplication.translate("ColumnSelectDialog", u"Column Select Dialog", None))
        self.label_7.setText(QCoreApplication.translate("ColumnSelectDialog", u"File:", None))
        self.selectFileButton.setText(QCoreApplication.translate("ColumnSelectDialog", u"Select", None))
        self.submitButton.setText(QCoreApplication.translate("ColumnSelectDialog", u"Submit", None))
        self.label.setText(QCoreApplication.translate("ColumnSelectDialog", u"Reading Time", None))
        self.label_8.setText(QCoreApplication.translate("ColumnSelectDialog", u"Reading Day", None))
        self.label_2.setText(QCoreApplication.translate("ColumnSelectDialog", u"Magnetic Field", None))
        self.label_3.setText(QCoreApplication.translate("ColumnSelectDialog", u"Gps Latitude", None))
        self.label_4.setText(QCoreApplication.translate("ColumnSelectDialog", u"Gps Longitude", None))
        self.label_5.setText(QCoreApplication.translate("ColumnSelectDialog", u"Gps Easting", None))
        self.label_6.setText(QCoreApplication.translate("ColumnSelectDialog", u"Gps Northing", None))
        self.label_9.setText(QCoreApplication.translate("ColumnSelectDialog", u"Skip rows", None))
    # retranslateUi

