# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QToolBar,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(963, 889)
        self.actionblubb = QAction(MainWindow)
        self.actionblubb.setObjectName(u"actionblubb")
        self.actionDinuralCorrection = QAction(MainWindow)
        self.actionDinuralCorrection.setObjectName(u"actionDinuralCorrection")
        self.actionSmoothSurvey = QAction(MainWindow)
        self.actionSmoothSurvey.setObjectName(u"actionSmoothSurvey")
        self.actioncalcResiduals = QAction(MainWindow)
        self.actioncalcResiduals.setObjectName(u"actioncalcResiduals")
        self.actionSomething_Else = QAction(MainWindow)
        self.actionSomething_Else.setObjectName(u"actionSomething_Else")
        self.actionNew_Project = QAction(MainWindow)
        self.actionNew_Project.setObjectName(u"actionNew_Project")
        self.actionSave_Project = QAction(MainWindow)
        self.actionSave_Project.setObjectName(u"actionSave_Project")
        self.actionOpen_Project = QAction(MainWindow)
        self.actionOpen_Project.setObjectName(u"actionOpen_Project")
        self.actionFrom_BOB_CSV = QAction(MainWindow)
        self.actionFrom_BOB_CSV.setObjectName(u"actionFrom_BOB_CSV")
        self.actionFrom_Sealink_Folder = QAction(MainWindow)
        self.actionFrom_Sealink_Folder.setObjectName(u"actionFrom_Sealink_Folder")
        self.actionFrom_Custom_CSV = QAction(MainWindow)
        self.actionFrom_Custom_CSV.setObjectName(u"actionFrom_Custom_CSV")
        self.actionDrawSelect = QAction(MainWindow)
        self.actionDrawSelect.setObjectName(u"actionDrawSelect")
        icon = QIcon()
        icon.addFile(u"../icons/drawingIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.actionDrawSelect.setIcon(icon)
        self.actionRemoveOutlier = QAction(MainWindow)
        self.actionRemoveOutlier.setObjectName(u"actionRemoveOutlier")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(320, 530, 931, 271))
        self.verticalLayoutTimeSeriesCanvas = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayoutTimeSeriesCanvas.setObjectName(u"verticalLayoutTimeSeriesCanvas")
        self.verticalLayoutTimeSeriesCanvas.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(320, 10, 931, 501))
        self.verticalLayout2DMappingCanvas = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout2DMappingCanvas.setObjectName(u"verticalLayout2DMappingCanvas")
        self.verticalLayout2DMappingCanvas.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 520, 88, 27))
        self.treeWidget = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"File Tree");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(10, 10, 291, 501))
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 580, 291, 221))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 560, 291, 19))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 963, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuOpen_Survey = QMenu(self.menuFile)
        self.menuOpen_Survey.setObjectName(u"menuOpen_Survey")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuOpen_Survey.menuAction())
        self.menuOpen_Survey.addAction(self.actionFrom_BOB_CSV)
        self.menuOpen_Survey.addAction(self.actionFrom_Sealink_Folder)
        self.menuOpen_Survey.addSeparator()
        self.menuOpen_Survey.addAction(self.actionFrom_Custom_CSV)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDinuralCorrection)
        self.toolBar.addAction(self.actionSmoothSurvey)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actioncalcResiduals)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDrawSelect)
        self.toolBar.addAction(self.actionRemoveOutlier)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Magnetometry", None))
        self.actionblubb.setText(QCoreApplication.translate("MainWindow", u"blubb", None))
        self.actionDinuralCorrection.setText(QCoreApplication.translate("MainWindow", u"DinuralCorrection", None))
#if QT_CONFIG(tooltip)
        self.actionDinuralCorrection.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">DC</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.actionSmoothSurvey.setText(QCoreApplication.translate("MainWindow", u"SmoothSurvey", None))
        self.actioncalcResiduals.setText(QCoreApplication.translate("MainWindow", u"calcResiduals", None))
        self.actionSomething_Else.setText(QCoreApplication.translate("MainWindow", u"Something Else", None))
        self.actionNew_Project.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
        self.actionSave_Project.setText(QCoreApplication.translate("MainWindow", u"Save Project", None))
        self.actionOpen_Project.setText(QCoreApplication.translate("MainWindow", u"Open Project", None))
        self.actionFrom_BOB_CSV.setText(QCoreApplication.translate("MainWindow", u"From BOB CSV", None))
        self.actionFrom_Sealink_Folder.setText(QCoreApplication.translate("MainWindow", u"From Sealink Folder", None))
        self.actionFrom_Custom_CSV.setText(QCoreApplication.translate("MainWindow", u"From Custom CSV", None))
        self.actionDrawSelect.setText(QCoreApplication.translate("MainWindow", u"DrawSelect", None))
        self.actionRemoveOutlier.setText(QCoreApplication.translate("MainWindow", u"RemoveOutlier", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Display Layers", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuOpen_Survey.setTitle(QCoreApplication.translate("MainWindow", u"Import Survey", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

