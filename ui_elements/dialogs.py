from ui_elements.select_column_dialog import Ui_ColumnSelectDialog
from ui_elements.remove_outlier_dialog import Ui_RemoveOutlierDialog
from PySide6.QtCore import QThreadPool, Slot, Signal, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QInputDialog, QTreeWidget, \
    QTreeWidgetItem, QDialog
from PySide6.QtGui import QIntValidator


class ColumnSelectDlg(QDialog):
    data_signal = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ColumnSelectDialog()
        self.ui.setupUi(self)

        self.ui.selectFileButton.clicked.connect(self.open_file_dialog)
        self.ui.submitButton.clicked.connect(self.send_data)

        self.validator = QIntValidator(0, 100000, self)
        self.ui.lineEdit_skipHeaderRows.setValidator(self.validator)


    def open_file_dialog(self):
        selected_survey = QFileDialog.getOpenFileName(filter="All Files(*);;Text files(*.csv *.txt)")
        if selected_survey[0].endswith((".txt", ".csv")):
            self.ui.lineEdit_file_path.setText(selected_survey[0])

    def send_data(self):
        inputs = {
            "file": self.ui.lineEdit_file_path.text(),
            "date": self.ui.lineEdit_day.text(),
            "time": self.ui.lineEdit_time.text(),
            "mag": self.ui.lineEdit_mag_field.text(),
            "lat": self.ui.lineEdit_Gps_lat.text(),
            "long": self.ui.lineEdit_Gps_long.text(),
            "east": self.ui.lineEdit_Gps_easting.text(),
            "north": self.ui.lineEdit_Gps_northing.text(),
            "skip": int(self.ui.lineEdit_skipHeaderRows.text()),
            "delimiter": self.ui.lineEdit_delimiter.text()
        }

        if all([lineEdit != "" for lineEdit in inputs.values()]):
            print("HEREEEEE")
            self.data_signal.emit(inputs)
            self.accept()
        else:
            alert_box = QMessageBox.critical(
                self,
                "Empty input!",
                "Some fields are empty! Continue editing?",
                buttons=QMessageBox.Ok | QMessageBox.Discard,
                defaultButton=QMessageBox.Discard,
            )

            if alert_box==QMessageBox.Discard:
                self.reject()


class RemoveOutlierDlg(QDialog):
    data_signal = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_RemoveOutlierDialog()
        self.ui.setupUi(self)
        self.ui.submitButton.clicked.connect(self.send_data)

    def send_data(self):
        inputs = [
            self.ui.lineEdit_maxMagField.text(),
            self.ui.lineEdit_minMagField.text(),
            self.ui.lineEdit_maxLongVal.text(),
            self.ui.lineEdit_minLongVal.text(),
            self.ui.lineEdit_maxLatVal.text(),
            self.ui.lineEdit_minLatVal.text(),
            self.ui.comboBox.currentText()
        ]
        self.data_signal.emit(inputs)
        self.accept()
