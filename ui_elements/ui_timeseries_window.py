# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timeseries_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QSizePolicy,
    QSpacerItem, QStatusBar, QToolBar, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1241, 881)
        self.actionDraw1D = QAction(MainWindow)
        self.actionDraw1D.setObjectName(u"actionDraw1D")
        icon = QIcon()
        icon.addFile(u":/icons/area-chart-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionDraw1D.setIcon(icon)
        self.actionDinural_correction = QAction(MainWindow)
        self.actionDinural_correction.setObjectName(u"actionDinural_correction")
        icon1 = QIcon()
        icon1.addFile(u":/icons/magnetic-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionDinural_correction.setIcon(icon1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(9)
        self.verticalLayoutTimeSeriesCanvas = QVBoxLayout()
        self.verticalLayoutTimeSeriesCanvas.setObjectName(u"verticalLayoutTimeSeriesCanvas")

        self.gridLayout.addLayout(self.verticalLayoutTimeSeriesCanvas, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit_smoothingWindow = QLineEdit(self.centralwidget)
        self.lineEdit_smoothingWindow.setObjectName(u"lineEdit_smoothingWindow")

        self.verticalLayout.addWidget(self.lineEdit_smoothingWindow)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.lineEdit_ambientWindow = QLineEdit(self.centralwidget)
        self.lineEdit_ambientWindow.setObjectName(u"lineEdit_ambientWindow")

        self.verticalLayout.addWidget(self.lineEdit_ambientWindow)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 2, 1)

        self.verticalLayoutTimeSeriesCanvas_2 = QVBoxLayout()
        self.verticalLayoutTimeSeriesCanvas_2.setObjectName(u"verticalLayoutTimeSeriesCanvas_2")

        self.gridLayout.addLayout(self.verticalLayoutTimeSeriesCanvas_2, 1, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1241, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionDinural_correction)
        self.toolBar.addAction(self.actionDraw1D)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDraw1D.setText(QCoreApplication.translate("MainWindow", u"Draw1D", None))
        self.actionDinural_correction.setText(QCoreApplication.translate("MainWindow", u"Dinural correction", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Smoothing window size:", None))
        self.lineEdit_smoothingWindow.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ambient estimation window size:", None))
        self.lineEdit_ambientWindow.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

