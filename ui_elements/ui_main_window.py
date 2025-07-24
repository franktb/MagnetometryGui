# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QStatusBar, QToolBar, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1585, 889)
        self.actionblubb = QAction(MainWindow)
        self.actionblubb.setObjectName(u"actionblubb")
        self.actionDinuralCorrection = QAction(MainWindow)
        self.actionDinuralCorrection.setObjectName(u"actionDinuralCorrection")
        icon = QIcon()
        icon.addFile(u":/icons/magnetic-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionDinuralCorrection.setIcon(icon)
        self.actionSmoothSurvey = QAction(MainWindow)
        self.actionSmoothSurvey.setObjectName(u"actionSmoothSurvey")
        icon1 = QIcon()
        icon1.addFile(u":/icons/improvement-performance-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionSmoothSurvey.setIcon(icon1)
        self.actioncalcResiduals = QAction(MainWindow)
        self.actioncalcResiduals.setObjectName(u"actioncalcResiduals")
        icon2 = QIcon()
        icon2.addFile(u":/icons/calculator-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actioncalcResiduals.setIcon(icon2)
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
        icon3 = QIcon()
        icon3.addFile(u":/icons/drawingIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionDrawSelect.setIcon(icon3)
        self.actionRemoveOutlier = QAction(MainWindow)
        self.actionRemoveOutlier.setObjectName(u"actionRemoveOutlier")
        icon4 = QIcon()
        icon4.addFile(u":/icons/eraser-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionRemoveOutlier.setIcon(icon4)
        self.actionCSV = QAction(MainWindow)
        self.actionCSV.setObjectName(u"actionCSV")
        self.actionGeoTiff = QAction(MainWindow)
        self.actionGeoTiff.setObjectName(u"actionGeoTiff")
        self.action_spawn_FFTWindow = QAction(MainWindow)
        self.action_spawn_FFTWindow.setObjectName(u"action_spawn_FFTWindow")
        self.action_spawn_FFTWindow.setCheckable(True)
        self.action_spawn_FFTWindow.setEnabled(True)
        self.actionExport_Survey = QAction(MainWindow)
        self.actionExport_Survey.setObjectName(u"actionExport_Survey")
        self.actionanomalyDetection = QAction(MainWindow)
        self.actionanomalyDetection.setObjectName(u"actionanomalyDetection")
        icon5 = QIcon()
        icon5.addFile(u":/icons/search-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionanomalyDetection.setIcon(icon5)
        self.action_spawn_TimeSeriesWindow = QAction(MainWindow)
        self.action_spawn_TimeSeriesWindow.setObjectName(u"action_spawn_TimeSeriesWindow")
        self.action_spawn_TimeSeriesWindow.setCheckable(True)
        self.actionDraw1D = QAction(MainWindow)
        self.actionDraw1D.setObjectName(u"actionDraw1D")
        icon6 = QIcon()
        icon6.addFile(u":/icons/area-chart-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionDraw1D.setIcon(icon6)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.treeWidget = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"File Tree");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")

        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)

        self.verticalLayout2DMappingCanvas = QVBoxLayout()
        self.verticalLayout2DMappingCanvas.setObjectName(u"verticalLayout2DMappingCanvas")

        self.gridLayout.addLayout(self.verticalLayout2DMappingCanvas, 0, 1, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.layerWidget = QListWidget(self.centralwidget)
        self.layerWidget.setObjectName(u"layerWidget")

        self.verticalLayout.addWidget(self.layerWidget)

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

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.lineEdit_nthSelectWindow = QLineEdit(self.centralwidget)
        self.lineEdit_nthSelectWindow.setObjectName(u"lineEdit_nthSelectWindow")

        self.verticalLayout.addWidget(self.lineEdit_nthSelectWindow)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.lineEdit_eastingsSampleRate = QLineEdit(self.centralwidget)
        self.lineEdit_eastingsSampleRate.setObjectName(u"lineEdit_eastingsSampleRate")

        self.verticalLayout.addWidget(self.lineEdit_eastingsSampleRate)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.lineEdit_northingsSampleRate = QLineEdit(self.centralwidget)
        self.lineEdit_northingsSampleRate.setObjectName(u"lineEdit_northingsSampleRate")

        self.verticalLayout.addWidget(self.lineEdit_northingsSampleRate)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.comboBox_Scale_type = QComboBox(self.centralwidget)
        self.comboBox_Scale_type.addItem("")
        self.comboBox_Scale_type.addItem("")
        self.comboBox_Scale_type.setObjectName(u"comboBox_Scale_type")

        self.verticalLayout.addWidget(self.comboBox_Scale_type)


        self.gridLayout.addLayout(self.verticalLayout, 0, 3, 1, 1)

        self.verticalLayoutTimeSeriesCanvas = QVBoxLayout()
        self.verticalLayoutTimeSeriesCanvas.setObjectName(u"verticalLayoutTimeSeriesCanvas")

        self.gridLayout.addLayout(self.verticalLayoutTimeSeriesCanvas, 1, 0, 1, 2)

        self.verticalLayoutTimeSeriesCanvas_2 = QVBoxLayout()
        self.verticalLayoutTimeSeriesCanvas_2.setObjectName(u"verticalLayoutTimeSeriesCanvas_2")

        self.gridLayout.addLayout(self.verticalLayoutTimeSeriesCanvas_2, 1, 2, 1, 2)

        self.gridLayout.setRowStretch(0, 3)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setColumnStretch(3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1585, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuOpen_Survey = QMenu(self.menuFile)
        self.menuOpen_Survey.setObjectName(u"menuOpen_Survey")
        self.menuExport_Grid = QMenu(self.menuFile)
        self.menuExport_Grid.setObjectName(u"menuExport_Grid")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuOpen_Survey.menuAction())
        self.menuFile.addAction(self.actionExport_Survey)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuExport_Grid.menuAction())
        self.menuOpen_Survey.addAction(self.actionFrom_BOB_CSV)
        self.menuOpen_Survey.addAction(self.actionFrom_Sealink_Folder)
        self.menuOpen_Survey.addSeparator()
        self.menuOpen_Survey.addAction(self.actionFrom_Custom_CSV)
        self.menuExport_Grid.addAction(self.actionCSV)
        self.menuExport_Grid.addAction(self.actionGeoTiff)
        self.menuView.addAction(self.action_spawn_TimeSeriesWindow)
        self.menuView.addAction(self.action_spawn_FFTWindow)
        self.toolBar.addAction(self.actionRemoveOutlier)
        self.toolBar.addAction(self.actionDinuralCorrection)
        self.toolBar.addAction(self.actioncalcResiduals)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDraw1D)
        self.toolBar.addAction(self.actionDrawSelect)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionanomalyDetection)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Magnetometry", None))
        self.actionblubb.setText(QCoreApplication.translate("MainWindow", u"blubb", None))
        self.actionDinuralCorrection.setText(QCoreApplication.translate("MainWindow", u"DinuralCorrection", None))
#if QT_CONFIG(tooltip)
        self.actionDinuralCorrection.setToolTip(QCoreApplication.translate("MainWindow", u"Diurnal correction", None))
#endif // QT_CONFIG(tooltip)
        self.actionSmoothSurvey.setText(QCoreApplication.translate("MainWindow", u"SmoothSurvey", None))
        self.actioncalcResiduals.setText(QCoreApplication.translate("MainWindow", u"calcResiduals", None))
#if QT_CONFIG(tooltip)
        self.actioncalcResiduals.setToolTip(QCoreApplication.translate("MainWindow", u"Calculate residuals based on ambient field", None))
#endif // QT_CONFIG(tooltip)
        self.actionSomething_Else.setText(QCoreApplication.translate("MainWindow", u"Something Else", None))
        self.actionNew_Project.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
        self.actionSave_Project.setText(QCoreApplication.translate("MainWindow", u"Save Project", None))
        self.actionOpen_Project.setText(QCoreApplication.translate("MainWindow", u"Open Project", None))
        self.actionFrom_BOB_CSV.setText(QCoreApplication.translate("MainWindow", u"From BOB CSV", None))
        self.actionFrom_Sealink_Folder.setText(QCoreApplication.translate("MainWindow", u"From Sealink Folder", None))
        self.actionFrom_Custom_CSV.setText(QCoreApplication.translate("MainWindow", u"From Custom CSV", None))
        self.actionDrawSelect.setText(QCoreApplication.translate("MainWindow", u"DrawSelect", None))
        self.actionRemoveOutlier.setText(QCoreApplication.translate("MainWindow", u"RemoveOutlier", None))
        self.actionCSV.setText(QCoreApplication.translate("MainWindow", u"CSV", None))
        self.actionGeoTiff.setText(QCoreApplication.translate("MainWindow", u"GeoTiff", None))
        self.action_spawn_FFTWindow.setText(QCoreApplication.translate("MainWindow", u"Downward continuation", None))
        self.actionExport_Survey.setText(QCoreApplication.translate("MainWindow", u"Export Survey", None))
        self.actionanomalyDetection.setText(QCoreApplication.translate("MainWindow", u"anomalyDetection", None))
        self.action_spawn_TimeSeriesWindow.setText(QCoreApplication.translate("MainWindow", u"Timeseries representation", None))
        self.actionDraw1D.setText(QCoreApplication.translate("MainWindow", u"Draw1D", None))
#if QT_CONFIG(tooltip)
        self.actionDraw1D.setToolTip(QCoreApplication.translate("MainWindow", u"Draw a timeseries representation of selected surveys", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Display Layers:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Smoothing window size:", None))
        self.lineEdit_smoothingWindow.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ambient estimation window size:", None))
        self.lineEdit_ambientWindow.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Time sampling rate:", None))
        self.lineEdit_nthSelectWindow.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Eastings sampling rate:", None))
        self.lineEdit_eastingsSampleRate.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Northings sampling rate:", None))
        self.lineEdit_northingsSampleRate.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Scale type:", None))
        self.comboBox_Scale_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Linear scale", None))
        self.comboBox_Scale_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Logarithmic scale", None))

        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuOpen_Survey.setTitle(QCoreApplication.translate("MainWindow", u"Import Survey", None))
        self.menuExport_Grid.setTitle(QCoreApplication.translate("MainWindow", u"Export Grid", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"&Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"&View", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

