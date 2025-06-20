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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_FFTWindow(object):
    def setupUi(self, FFTWindow):
        if not FFTWindow.objectName():
            FFTWindow.setObjectName(u"FFTWindow")
        FFTWindow.resize(1014, 667)
        self.centralwidget = QWidget(FFTWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(110, 30, 651, 391))
        self.verticalLayout2DMappingCanvas = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout2DMappingCanvas.setObjectName(u"verticalLayout2DMappingCanvas")
        self.verticalLayout2DMappingCanvas.setContentsMargins(0, 0, 0, 0)
        self.lineEditDepth = QLineEdit(self.centralwidget)
        self.lineEditDepth.setObjectName(u"lineEditDepth")
        self.lineEditDepth.setGeometry(QRect(840, 100, 113, 27))
        self.lineEditIterations = QLineEdit(self.centralwidget)
        self.lineEditIterations.setObjectName(u"lineEditIterations")
        self.lineEditIterations.setGeometry(QRect(840, 170, 113, 27))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(840, 80, 66, 19))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(840, 140, 66, 19))
        self.pushButton_StartIteration = QPushButton(self.centralwidget)
        self.pushButton_StartIteration.setObjectName(u"pushButton_StartIteration")
        self.pushButton_StartIteration.setGeometry(QRect(840, 230, 111, 27))
        FFTWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FFTWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1014, 24))
        FFTWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FFTWindow)
        self.statusbar.setObjectName(u"statusbar")
        FFTWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FFTWindow)

        QMetaObject.connectSlotsByName(FFTWindow)
    # setupUi

    def retranslateUi(self, FFTWindow):
        FFTWindow.setWindowTitle(QCoreApplication.translate("FFTWindow", u"MainWindow", None))
        self.lineEditDepth.setText(QCoreApplication.translate("FFTWindow", u"50.0", None))
        self.lineEditIterations.setText(QCoreApplication.translate("FFTWindow", u"3", None))
        self.label.setText(QCoreApplication.translate("FFTWindow", u"Depth:", None))
        self.label_2.setText(QCoreApplication.translate("FFTWindow", u"Iterations:", None))
        self.pushButton_StartIteration.setText(QCoreApplication.translate("FFTWindow", u"Do it!", None))
    # retranslateUi

