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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_ColumnSelectDialog(object):
    def setupUi(self, ColumnSelectDialog):
        if not ColumnSelectDialog.objectName():
            ColumnSelectDialog.setObjectName(u"ColumnSelectDialog")
        ColumnSelectDialog.resize(548, 451)
        self.buttonBox = QDialogButtonBox(ColumnSelectDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(130, 390, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(ColumnSelectDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 80, 101, 19))
        self.label_2 = QLabel(ColumnSelectDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 160, 101, 19))
        self.label_3 = QLabel(ColumnSelectDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 200, 91, 19))
        self.label_4 = QLabel(ColumnSelectDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 240, 101, 19))
        self.label_5 = QLabel(ColumnSelectDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 280, 91, 19))
        self.lineEdit_time = QLineEdit(ColumnSelectDialog)
        self.lineEdit_time.setObjectName(u"lineEdit_time")
        self.lineEdit_time.setGeometry(QRect(170, 80, 113, 27))
        self.lineEdit_mag_field = QLineEdit(ColumnSelectDialog)
        self.lineEdit_mag_field.setObjectName(u"lineEdit_mag_field")
        self.lineEdit_mag_field.setGeometry(QRect(170, 160, 113, 27))
        self.lineEdit_Gps_lat = QLineEdit(ColumnSelectDialog)
        self.lineEdit_Gps_lat.setObjectName(u"lineEdit_Gps_lat")
        self.lineEdit_Gps_lat.setGeometry(QRect(170, 200, 113, 27))
        self.lineEdit_Gps_long = QLineEdit(ColumnSelectDialog)
        self.lineEdit_Gps_long.setObjectName(u"lineEdit_Gps_long")
        self.lineEdit_Gps_long.setGeometry(QRect(170, 240, 113, 27))
        self.lineEdit_Gps_easting = QLineEdit(ColumnSelectDialog)
        self.lineEdit_Gps_easting.setObjectName(u"lineEdit_Gps_easting")
        self.lineEdit_Gps_easting.setGeometry(QRect(170, 280, 113, 27))
        self.label_6 = QLabel(ColumnSelectDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 320, 101, 19))
        self.lineEdit_Gps_northing = QLineEdit(ColumnSelectDialog)
        self.lineEdit_Gps_northing.setObjectName(u"lineEdit_Gps_northing")
        self.lineEdit_Gps_northing.setGeometry(QRect(170, 320, 113, 27))
        self.label_8 = QLabel(ColumnSelectDialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(60, 120, 101, 19))
        self.lineEdit_day = QLineEdit(ColumnSelectDialog)
        self.lineEdit_day.setObjectName(u"lineEdit_day")
        self.lineEdit_day.setGeometry(QRect(170, 120, 113, 27))
        self.label_7 = QLabel(ColumnSelectDialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 40, 66, 19))
        self.lineEdit_file_path = QLineEdit(ColumnSelectDialog)
        self.lineEdit_file_path.setObjectName(u"lineEdit_file_path")
        self.lineEdit_file_path.setGeometry(QRect(170, 40, 113, 27))
        self.selectFileButton = QPushButton(ColumnSelectDialog)
        self.selectFileButton.setObjectName(u"selectFileButton")
        self.selectFileButton.setGeometry(QRect(330, 40, 88, 27))
        self.submitButton = QPushButton(ColumnSelectDialog)
        self.submitButton.setObjectName(u"submitButton")
        self.submitButton.setGeometry(QRect(390, 340, 88, 27))

        self.retranslateUi(ColumnSelectDialog)
        self.buttonBox.accepted.connect(ColumnSelectDialog.accept)
        self.buttonBox.rejected.connect(ColumnSelectDialog.reject)

        QMetaObject.connectSlotsByName(ColumnSelectDialog)
    # setupUi

    def retranslateUi(self, ColumnSelectDialog):
        ColumnSelectDialog.setWindowTitle(QCoreApplication.translate("ColumnSelectDialog", u"Column Select Dialog", None))
        self.label.setText(QCoreApplication.translate("ColumnSelectDialog", u"Reading Time", None))
        self.label_2.setText(QCoreApplication.translate("ColumnSelectDialog", u"Magnetic Field", None))
        self.label_3.setText(QCoreApplication.translate("ColumnSelectDialog", u"Gps Latitude", None))
        self.label_4.setText(QCoreApplication.translate("ColumnSelectDialog", u"Gps Longitude", None))
        self.label_5.setText(QCoreApplication.translate("ColumnSelectDialog", u"Gps Easting", None))
        self.label_6.setText(QCoreApplication.translate("ColumnSelectDialog", u"Gps Northing", None))
        self.label_8.setText(QCoreApplication.translate("ColumnSelectDialog", u"Reading Day", None))
        self.label_7.setText(QCoreApplication.translate("ColumnSelectDialog", u"TextLabel", None))
        self.selectFileButton.setText(QCoreApplication.translate("ColumnSelectDialog", u"Select", None))
        self.submitButton.setText(QCoreApplication.translate("ColumnSelectDialog", u"Submit", None))
    # retranslateUi

