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

        latlon_provided = all([inputs["lat"], inputs["long"]])
        eastnorth_provided = all([inputs["east"], inputs["north"]])

        latlon_missing = not any([inputs["lat"], inputs["long"]])
        eastnorth_missing = not any([inputs["east"], inputs["north"]])

        if all([lineEdit != "" for lineEdit in inputs.values()]):
            print("HEREEEEE")
            self.data_signal.emit(inputs)
            self.accept()

        elif latlon_provided and eastnorth_missing:
            info_box = QMessageBox.information(
                self,
                "Eastings and northings are missing.",
                "Those will be estimated based on provided latitudes and longitudes.",
                buttons=QMessageBox.Ok | QMessageBox.Cancel,
                defaultButton=QMessageBox.Ok,
            )
            if info_box == QMessageBox.Ok:
                inputs["east"] = None
                inputs["north"] = None
                self.data_signal.emit(inputs)
                self.accept()

        elif eastnorth_provided and latlon_missing:
            info_box = QMessageBox.information(
                self,
                "Latitudes and longitudes are missing.",
                "Those will be estimated based on provided eastings and northings.",
                buttons=QMessageBox.Ok | QMessageBox.Cancel,
                defaultButton=QMessageBox.Ok,
            )
            if info_box == QMessageBox.Ok:
                inputs["lat"] = None
                inputs["long"] = None
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

            if alert_box == QMessageBox.Discard:
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
