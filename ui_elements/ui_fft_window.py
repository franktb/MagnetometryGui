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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_FFTWindow(object):
    def setupUi(self, FFTWindow):
        if not FFTWindow.objectName():
            FFTWindow.setObjectName(u"FFTWindow")
        FFTWindow.resize(1390, 892)
        self.centralwidget = QWidget(FFTWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_layer = QPushButton(self.centralwidget)
        self.pushButton_layer.setObjectName(u"pushButton_layer")

        self.gridLayout.addWidget(self.pushButton_layer, 3, 1, 1, 1)

        self.verticalLayout2DMappingCanvas = QVBoxLayout()
        self.verticalLayout2DMappingCanvas.setObjectName(u"verticalLayout2DMappingCanvas")

        self.gridLayout.addLayout(self.verticalLayout2DMappingCanvas, 0, 0, 4, 1)

        self.pushButton_StartIteration = QPushButton(self.centralwidget)
        self.pushButton_StartIteration.setObjectName(u"pushButton_StartIteration")

        self.gridLayout.addWidget(self.pushButton_StartIteration, 2, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lineEditDepth = QLineEdit(self.centralwidget)
        self.lineEditDepth.setObjectName(u"lineEditDepth")

        self.verticalLayout.addWidget(self.lineEditDepth)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.comboBox_display = QComboBox(self.centralwidget)
        self.comboBox_display.addItem("")
        self.comboBox_display.addItem("")
        self.comboBox_display.addItem("")
        self.comboBox_display.setObjectName(u"comboBox_display")

        self.verticalLayout.addWidget(self.comboBox_display)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_eastingsSampleRate = QLineEdit(self.centralwidget)
        self.lineEdit_eastingsSampleRate.setObjectName(u"lineEdit_eastingsSampleRate")

        self.gridLayout_2.addWidget(self.lineEdit_eastingsSampleRate, 5, 1, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)

        self.comboBoxDisplayedLayer = QComboBox(self.centralwidget)
        self.comboBoxDisplayedLayer.setObjectName(u"comboBoxDisplayedLayer")

        self.gridLayout_2.addWidget(self.comboBoxDisplayedLayer, 1, 1, 1, 1)

        self.lineEditcubeYdown = QLineEdit(self.centralwidget)
        self.lineEditcubeYdown.setObjectName(u"lineEditcubeYdown")

        self.gridLayout_2.addWidget(self.lineEditcubeYdown, 3, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)

        self.lineEditIterations = QLineEdit(self.centralwidget)
        self.lineEditIterations.setObjectName(u"lineEditIterations")

        self.gridLayout_2.addWidget(self.lineEditIterations, 4, 1, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.lineEditLayers = QLineEdit(self.centralwidget)
        self.lineEditLayers.setObjectName(u"lineEditLayers")

        self.gridLayout_2.addWidget(self.lineEditLayers, 0, 1, 1, 1)

        self.lineEditcubeYup = QLineEdit(self.centralwidget)
        self.lineEditcubeYup.setObjectName(u"lineEditcubeYup")

        self.gridLayout_2.addWidget(self.lineEditcubeYup, 2, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 6, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_2.addWidget(self.lineEdit_2, 6, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.comboBox_scaleType = QComboBox(self.centralwidget)
        self.comboBox_scaleType.addItem("")
        self.comboBox_scaleType.addItem("")
        self.comboBox_scaleType.setObjectName(u"comboBox_scaleType")

        self.verticalLayout.addWidget(self.comboBox_scaleType)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 2, 1)

        self.gridLayout.setColumnStretch(0, 2)
        FFTWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FFTWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1390, 24))
        FFTWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FFTWindow)
        self.statusbar.setObjectName(u"statusbar")
        FFTWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FFTWindow)

        QMetaObject.connectSlotsByName(FFTWindow)
    # setupUi

    def retranslateUi(self, FFTWindow):
        FFTWindow.setWindowTitle(QCoreApplication.translate("FFTWindow", u"MainWindow", None))
        self.pushButton_layer.setText(QCoreApplication.translate("FFTWindow", u"Do Layer", None))
        self.pushButton_StartIteration.setText(QCoreApplication.translate("FFTWindow", u"Do it!", None))
        self.label.setText(QCoreApplication.translate("FFTWindow", u"Depth:", None))
        self.lineEditDepth.setText(QCoreApplication.translate("FFTWindow", u"50.0", None))
        self.label_6.setText(QCoreApplication.translate("FFTWindow", u"Display:", None))
        self.comboBox_display.setItemText(0, QCoreApplication.translate("FFTWindow", u"Fixed depth", None))
        self.comboBox_display.setItemText(1, QCoreApplication.translate("FFTWindow", u"Layers", None))
        self.comboBox_display.setItemText(2, QCoreApplication.translate("FFTWindow", u"Bathymetry", None))

        self.label_7.setText(QCoreApplication.translate("FFTWindow", u"Layers:", None))
        self.label_10.setText(QCoreApplication.translate("FFTWindow", u"Depth low:", None))
        self.lineEditcubeYdown.setText(QCoreApplication.translate("FFTWindow", u"-20", None))
        self.label_4.setText(QCoreApplication.translate("FFTWindow", u"Eastings points:", None))
        self.label_2.setText(QCoreApplication.translate("FFTWindow", u"Iterations:", None))
        self.lineEditIterations.setText(QCoreApplication.translate("FFTWindow", u"3", None))
        self.label_8.setText(QCoreApplication.translate("FFTWindow", u"Depth up:", None))
        self.label_9.setText(QCoreApplication.translate("FFTWindow", u"Display:", None))
        self.lineEditLayers.setText(QCoreApplication.translate("FFTWindow", u"5", None))
        self.lineEditcubeYup.setText(QCoreApplication.translate("FFTWindow", u"-10", None))
        self.label_5.setText(QCoreApplication.translate("FFTWindow", u"Northings points:", None))
        self.label_3.setText(QCoreApplication.translate("FFTWindow", u"Scale type:", None))
        self.comboBox_scaleType.setItemText(0, QCoreApplication.translate("FFTWindow", u"Linear scale", None))
        self.comboBox_scaleType.setItemText(1, QCoreApplication.translate("FFTWindow", u"Logarithmic scale", None))

    # retranslateUi

