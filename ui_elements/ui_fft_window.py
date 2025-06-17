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
    QMenuBar, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

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
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(840, 100, 113, 27))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(840, 170, 113, 27))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(840, 80, 66, 19))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(840, 140, 66, 19))
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
        self.label.setText(QCoreApplication.translate("FFTWindow", u"Depth:", None))
        self.label_2.setText(QCoreApplication.translate("FFTWindow", u"Iterations:", None))
    # retranslateUi

