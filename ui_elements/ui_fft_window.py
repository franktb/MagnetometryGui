# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fft_main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_FFTWindow(object):
    def setupUi(self, FFTWindow):
        if not FFTWindow.objectName():
            FFTWindow.setObjectName(u"FFTWindow")
        FFTWindow.resize(1065, 523)
        self.centralwidget = QWidget(FFTWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 711, 391))
        self.verticalLayout2DMappingCanvas = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout2DMappingCanvas.setObjectName(u"verticalLayout2DMappingCanvas")
        self.verticalLayout2DMappingCanvas.setContentsMargins(0, 0, 0, 0)
        self.pushButton_StartIteration = QPushButton(self.centralwidget)
        self.pushButton_StartIteration.setObjectName(u"pushButton_StartIteration")
        self.pushButton_StartIteration.setGeometry(QRect(30, 430, 111, 27))
        self.pushButton_layer = QPushButton(self.centralwidget)
        self.pushButton_layer.setObjectName(u"pushButton_layer")
        self.pushButton_layer.setGeometry(QRect(160, 430, 88, 27))
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(750, 20, 281, 391))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lineEditDepth = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEditDepth.setObjectName(u"lineEditDepth")

        self.verticalLayout.addWidget(self.lineEditDepth)

        self.label_6 = QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.comboBox_display = QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_display.addItem("")
        self.comboBox_display.addItem("")
        self.comboBox_display.setObjectName(u"comboBox_display")

        self.verticalLayout.addWidget(self.comboBox_display)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lineEditIterations = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEditIterations.setObjectName(u"lineEditIterations")

        self.verticalLayout.addWidget(self.lineEditIterations)

        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.lineEdit_eastingsSampleRate = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_eastingsSampleRate.setObjectName(u"lineEdit_eastingsSampleRate")

        self.verticalLayout.addWidget(self.lineEdit_eastingsSampleRate)

        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.comboBox_scaleType = QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_scaleType.addItem("")
        self.comboBox_scaleType.addItem("")
        self.comboBox_scaleType.setObjectName(u"comboBox_scaleType")

        self.verticalLayout.addWidget(self.comboBox_scaleType)

        FFTWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FFTWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1065, 24))
        FFTWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FFTWindow)
        self.statusbar.setObjectName(u"statusbar")
        FFTWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FFTWindow)

        QMetaObject.connectSlotsByName(FFTWindow)
    # setupUi

    def retranslateUi(self, FFTWindow):
        FFTWindow.setWindowTitle(QCoreApplication.translate("FFTWindow", u"MainWindow", None))
        self.pushButton_StartIteration.setText(QCoreApplication.translate("FFTWindow", u"Do it!", None))
        self.pushButton_layer.setText(QCoreApplication.translate("FFTWindow", u"Do Layer", None))
        self.label.setText(QCoreApplication.translate("FFTWindow", u"Depth:", None))
        self.lineEditDepth.setText(QCoreApplication.translate("FFTWindow", u"50.0", None))
        self.label_6.setText(QCoreApplication.translate("FFTWindow", u"Display:", None))
        self.comboBox_display.setItemText(0, QCoreApplication.translate("FFTWindow", u"Fixed depth", None))
        self.comboBox_display.setItemText(1, QCoreApplication.translate("FFTWindow", u"Bathymetry", None))

        self.label_2.setText(QCoreApplication.translate("FFTWindow", u"Iterations:", None))
        self.lineEditIterations.setText(QCoreApplication.translate("FFTWindow", u"3", None))
        self.label_4.setText(QCoreApplication.translate("FFTWindow", u"Eastings sampling rate:", None))
        self.label_5.setText(QCoreApplication.translate("FFTWindow", u"Northings sampling rate:", None))
        self.label_3.setText(QCoreApplication.translate("FFTWindow", u"Scale type:", None))
        self.comboBox_scaleType.setItemText(0, QCoreApplication.translate("FFTWindow", u"Linear scale", None))
        self.comboBox_scaleType.setItemText(1, QCoreApplication.translate("FFTWindow", u"Logarithmic scale", None))

    # retranslateUi

