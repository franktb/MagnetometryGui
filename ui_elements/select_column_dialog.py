# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_column_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_ColumnSelectDialog(object):
    def setupUi(self, ColumnSelectDialog):
        if not ColumnSelectDialog.objectName():
            ColumnSelectDialog.setObjectName(u"ColumnSelectDialog")
        ColumnSelectDialog.resize(363, 447)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ColumnSelectDialog.sizePolicy().hasHeightForWidth())
        ColumnSelectDialog.setSizePolicy(sizePolicy)
        ColumnSelectDialog.setMinimumSize(QSize(363, 447))
        ColumnSelectDialog.setMaximumSize(QSize(363, 474))
        self.verticalLayoutWidget = QWidget(ColumnSelectDialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 341, 429))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.selectFileButton = QPushButton(self.verticalLayoutWidget)
        self.selectFileButton.setObjectName(u"selectFileButton")

        self.horizontalLayout_5.addWidget(self.selectFileButton)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.lineEdit_file_path = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_file_path.setObjectName(u"lineEdit_file_path")

        self.verticalLayout.addWidget(self.lineEdit_file_path)

        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_11)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.lineEdit_time = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_time.setObjectName(u"lineEdit_time")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_time)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.lineEdit_day = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_day.setObjectName(u"lineEdit_day")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_day)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.lineEdit_mag_field = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_mag_field.setObjectName(u"lineEdit_mag_field")

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit_mag_field)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout_4.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.lineEdit_Gps_lat = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_Gps_lat.setObjectName(u"lineEdit_Gps_lat")

        self.formLayout_4.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineEdit_Gps_lat)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.formLayout_4.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.lineEdit_Gps_long = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_Gps_long.setObjectName(u"lineEdit_Gps_long")

        self.formLayout_4.setWidget(4, QFormLayout.ItemRole.FieldRole, self.lineEdit_Gps_long)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.formLayout_4.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.lineEdit_Gps_easting = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_Gps_easting.setObjectName(u"lineEdit_Gps_easting")

        self.formLayout_4.setWidget(5, QFormLayout.ItemRole.FieldRole, self.lineEdit_Gps_easting)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.formLayout_4.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.lineEdit_Gps_northing = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_Gps_northing.setObjectName(u"lineEdit_Gps_northing")

        self.formLayout_4.setWidget(6, QFormLayout.ItemRole.FieldRole, self.lineEdit_Gps_northing)

        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.formLayout_4.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.lineEdit_skipHeaderRows = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_skipHeaderRows.setObjectName(u"lineEdit_skipHeaderRows")

        self.formLayout_4.setWidget(7, QFormLayout.ItemRole.FieldRole, self.lineEdit_skipHeaderRows)

        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.formLayout_4.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.lineEdit_delimiter = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_delimiter.setObjectName(u"lineEdit_delimiter")

        self.formLayout_4.setWidget(8, QFormLayout.ItemRole.FieldRole, self.lineEdit_delimiter)


        self.verticalLayout.addLayout(self.formLayout_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.submitButton = QPushButton(self.verticalLayoutWidget)
        self.submitButton.setObjectName(u"submitButton")

        self.horizontalLayout_4.addWidget(self.submitButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(ColumnSelectDialog)

        QMetaObject.connectSlotsByName(ColumnSelectDialog)
    # setupUi

    def retranslateUi(self, ColumnSelectDialog):
        ColumnSelectDialog.setWindowTitle(QCoreApplication.translate("ColumnSelectDialog", u"Provide CSV column layout", None))
        self.label_7.setText(QCoreApplication.translate("ColumnSelectDialog", u"File:", None))
        self.selectFileButton.setText(QCoreApplication.translate("ColumnSelectDialog", u"Select", None))
        self.label_11.setText(QCoreApplication.translate("ColumnSelectDialog", u"Please provide the corresponding column indices, assuming indexing starts at 0.", None))
        self.label.setText(QCoreApplication.translate("ColumnSelectDialog", u"Reading time:", None))
        self.label_8.setText(QCoreApplication.translate("ColumnSelectDialog", u"Reading day:", None))
        self.label_2.setText(QCoreApplication.translate("ColumnSelectDialog", u"Magnetic field:", None))
        self.label_3.setText(QCoreApplication.translate("ColumnSelectDialog", u"GPS latitude:", None))
        self.label_4.setText(QCoreApplication.translate("ColumnSelectDialog", u"GPS longitude:", None))
        self.label_5.setText(QCoreApplication.translate("ColumnSelectDialog", u"GPS eastings:", None))
        self.label_6.setText(QCoreApplication.translate("ColumnSelectDialog", u"GPS Northings:", None))
        self.label_9.setText(QCoreApplication.translate("ColumnSelectDialog", u"Skip rows:", None))
        self.label_10.setText(QCoreApplication.translate("ColumnSelectDialog", u"Delimiter:", None))
        self.submitButton.setText(QCoreApplication.translate("ColumnSelectDialog", u"Submit", None))
    # retranslateUi

