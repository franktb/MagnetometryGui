# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'remove_outlier_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QFormLayout, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_RemoveOutlierDialog(object):
    def setupUi(self, RemoveOutlierDialog):
        if not RemoveOutlierDialog.objectName():
            RemoveOutlierDialog.setObjectName(u"RemoveOutlierDialog")
        RemoveOutlierDialog.resize(373, 282)
        self.formLayout = QFormLayout(RemoveOutlierDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(RemoveOutlierDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.doubleSpinBox_maxMagField = QDoubleSpinBox(RemoveOutlierDialog)
        self.doubleSpinBox_maxMagField.setObjectName(u"doubleSpinBox_maxMagField")
        self.doubleSpinBox_maxMagField.setMaximum(1000000.000000000000000)
        self.doubleSpinBox_maxMagField.setSingleStep(0.000100000000000)
        self.doubleSpinBox_maxMagField.setValue(49000.000000000000000)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_maxMagField)

        self.label_2 = QLabel(RemoveOutlierDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.doubleSpinBox_minMagField = QDoubleSpinBox(RemoveOutlierDialog)
        self.doubleSpinBox_minMagField.setObjectName(u"doubleSpinBox_minMagField")
        self.doubleSpinBox_minMagField.setMaximum(1000000.000000000000000)
        self.doubleSpinBox_minMagField.setSingleStep(0.000100000000000)
        self.doubleSpinBox_minMagField.setValue(46000.000000000000000)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_minMagField)

        self.label_5 = QLabel(RemoveOutlierDialog)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.doubleSpinBox_minLat = QDoubleSpinBox(RemoveOutlierDialog)
        self.doubleSpinBox_minLat.setObjectName(u"doubleSpinBox_minLat")
        self.doubleSpinBox_minLat.setMinimum(-90.000000000000000)
        self.doubleSpinBox_minLat.setMaximum(90.000000000000000)
        self.doubleSpinBox_minLat.setSingleStep(0.100000000000000)
        self.doubleSpinBox_minLat.setValue(51.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_minLat)

        self.label_6 = QLabel(RemoveOutlierDialog)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.doubleSpinBox_maxLat = QDoubleSpinBox(RemoveOutlierDialog)
        self.doubleSpinBox_maxLat.setObjectName(u"doubleSpinBox_maxLat")
        self.doubleSpinBox_maxLat.setMinimum(-90.000000000000000)
        self.doubleSpinBox_maxLat.setMaximum(90.000000000000000)
        self.doubleSpinBox_maxLat.setSingleStep(0.100000000000000)
        self.doubleSpinBox_maxLat.setValue(52.000000000000000)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_maxLat)

        self.label_4 = QLabel(RemoveOutlierDialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.doubleSpinBox_minLong = QDoubleSpinBox(RemoveOutlierDialog)
        self.doubleSpinBox_minLong.setObjectName(u"doubleSpinBox_minLong")
        self.doubleSpinBox_minLong.setMinimum(-180.000000000000000)
        self.doubleSpinBox_minLong.setMaximum(180.000000000000000)
        self.doubleSpinBox_minLong.setSingleStep(0.100000000000000)
        self.doubleSpinBox_minLong.setValue(-9.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_minLong)

        self.label_3 = QLabel(RemoveOutlierDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.doubleSpinBox_maxLong = QDoubleSpinBox(RemoveOutlierDialog)
        self.doubleSpinBox_maxLong.setObjectName(u"doubleSpinBox_maxLong")
        self.doubleSpinBox_maxLong.setMinimum(-180.000000000000000)
        self.doubleSpinBox_maxLong.setMaximum(180.000000000000000)
        self.doubleSpinBox_maxLong.setSingleStep(0.100000000000000)
        self.doubleSpinBox_maxLong.setValue(-7.000000000000000)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_maxLong)

        self.label_7 = QLabel(RemoveOutlierDialog)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.comboBox = QComboBox(RemoveOutlierDialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.comboBox)

        self.submitButton = QPushButton(RemoveOutlierDialog)
        self.submitButton.setObjectName(u"submitButton")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.submitButton)


        self.retranslateUi(RemoveOutlierDialog)

        QMetaObject.connectSlotsByName(RemoveOutlierDialog)
    # setupUi

    def retranslateUi(self, RemoveOutlierDialog):
        RemoveOutlierDialog.setWindowTitle(QCoreApplication.translate("RemoveOutlierDialog", u"Outlier handeling", None))
        self.label.setText(QCoreApplication.translate("RemoveOutlierDialog", u"Max magnetic field [nT]:", None))
        self.label_2.setText(QCoreApplication.translate("RemoveOutlierDialog", u"Min magnetic field [nT]:", None))
        self.label_5.setText(QCoreApplication.translate("RemoveOutlierDialog", u"South latitude [\u00b0]:", None))
        self.label_6.setText(QCoreApplication.translate("RemoveOutlierDialog", u"North latitude [\u00b0]:", None))
        self.label_4.setText(QCoreApplication.translate("RemoveOutlierDialog", u"West longitude [\u00b0]:", None))
        self.label_3.setText(QCoreApplication.translate("RemoveOutlierDialog", u"East longitude [\u00b0]:", None))
        self.label_7.setText(QCoreApplication.translate("RemoveOutlierDialog", u"Action:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("RemoveOutlierDialog", u"Remove entry", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("RemoveOutlierDialog", u"Use last value", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("RemoveOutlierDialog", u"Interpolate neighbours", None))

        self.submitButton.setText(QCoreApplication.translate("RemoveOutlierDialog", u"Submit", None))
    # retranslateUi

