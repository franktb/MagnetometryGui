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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFormLayout,
    QGridLayout, QHeaderView, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QSpinBox, QStatusBar, QToolBar,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
import ui_elements.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1523, 1171)
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
        self.actionRename_Project = QAction(MainWindow)
        self.actionRename_Project.setObjectName(u"actionRename_Project")
        self.actionFrom_SENSYS_CSV = QAction(MainWindow)
        self.actionFrom_SENSYS_CSV.setObjectName(u"actionFrom_SENSYS_CSV")
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

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.spinBoxSmoothingWindow = QSpinBox(self.centralwidget)
        self.spinBoxSmoothingWindow.setObjectName(u"spinBoxSmoothingWindow")
        self.spinBoxSmoothingWindow.setMaximum(1000000)
        self.spinBoxSmoothingWindow.setValue(20)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBoxSmoothingWindow)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.spinBoxAmbientWindow = QSpinBox(self.centralwidget)
        self.spinBoxAmbientWindow.setObjectName(u"spinBoxAmbientWindow")
        self.spinBoxAmbientWindow.setMaximum(10000000)
        self.spinBoxAmbientWindow.setValue(500)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBoxAmbientWindow)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.spinBoxTimeRate = QSpinBox(self.centralwidget)
        self.spinBoxTimeRate.setObjectName(u"spinBoxTimeRate")
        self.spinBoxTimeRate.setMinimum(1)
        self.spinBoxTimeRate.setMaximum(10000000)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.spinBoxTimeRate)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.spinBoxEastings = QSpinBox(self.centralwidget)
        self.spinBoxEastings.setObjectName(u"spinBoxEastings")
        self.spinBoxEastings.setMaximum(1000000)
        self.spinBoxEastings.setValue(1000)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.spinBoxEastings)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.spinBoxNorthings = QSpinBox(self.centralwidget)
        self.spinBoxNorthings.setObjectName(u"spinBoxNorthings")
        self.spinBoxNorthings.setMaximum(1000000)
        self.spinBoxNorthings.setValue(1000)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.spinBoxNorthings)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.doubleSpinBoxRasterX = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxRasterX.setObjectName(u"doubleSpinBoxRasterX")
        self.doubleSpinBoxRasterX.setMaximum(1000000.000000000000000)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.doubleSpinBoxRasterX)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.doubleSpinBoxRasterY = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxRasterY.setObjectName(u"doubleSpinBoxRasterY")
        self.doubleSpinBoxRasterY.setMaximum(1000000.000000000000000)

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.doubleSpinBoxRasterY)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.comboBox_Scale_type = QComboBox(self.centralwidget)
        self.comboBox_Scale_type.addItem("")
        self.comboBox_Scale_type.addItem("")
        self.comboBox_Scale_type.setObjectName(u"comboBox_Scale_type")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.comboBox_Scale_type)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.doubleSpinBoxSobel = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxSobel.setObjectName(u"doubleSpinBoxSobel")
        self.doubleSpinBoxSobel.setDecimals(3)
        self.doubleSpinBoxSobel.setMaximum(1.000000000000000)
        self.doubleSpinBoxSobel.setSingleStep(0.000100000000000)
        self.doubleSpinBoxSobel.setValue(0.999000000000000)

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.doubleSpinBoxSobel)


        self.verticalLayout.addLayout(self.formLayout)


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
        self.menubar.setGeometry(QRect(0, 0, 1523, 24))
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
        self.menuFile.addAction(self.actionRename_Project)
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
        self.menuOpen_Survey.addAction(self.actionFrom_SENSYS_CSV)
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
        self.actionRename_Project.setText(QCoreApplication.translate("MainWindow", u"Rename Project", None))
        self.actionFrom_SENSYS_CSV.setText(QCoreApplication.translate("MainWindow", u"From SENSYS CSV", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Display Layers:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Smoothing window:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ambient window:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Time sampling rate:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Eastings sampling rate:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Northings sampling rate:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Rastersize x:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Rastersize y:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Scale type:", None))
        self.comboBox_Scale_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Linear scale", None))
        self.comboBox_Scale_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Logarithmic scale", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Sobel threshold:", None))
#if QT_CONFIG(tooltip)
        self.doubleSpinBoxSobel.setToolTip(QCoreApplication.translate("MainWindow", u"Percentile threshold for Sobel gradient magnitude used to detect anomalies.", None))
#endif // QT_CONFIG(tooltip)
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuOpen_Survey.setTitle(QCoreApplication.translate("MainWindow", u"Import Survey", None))
        self.menuExport_Grid.setTitle(QCoreApplication.translate("MainWindow", u"Export Grid", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"&Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"&View", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

