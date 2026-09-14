from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QDoubleSpinBox,
    QPushButton,
    QScrollArea,
)


class FloatListWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Scrollable area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Widget containing the rows
        self.rows_widget = QWidget()
        self.rows_layout = QVBoxLayout(self.rows_widget)
        self.rows_layout.setContentsMargins(0, 0, 0, 0)
        self.rows_layout.setSpacing(4)

        # Important: keep rows at the top
        self.rows_layout.addStretch()

        scroll.setWidget(self.rows_widget)

        main_layout.addWidget(scroll)

        # Add button stays outside the scroll area
        self.add_button = QPushButton("+ Add value")
        self.add_button.clicked.connect(self.add_value)
        main_layout.addWidget(self.add_button)

    def add_value(self, value=0.0):
        row = QWidget()
        row_layout = QHBoxLayout(row)
        row_layout.setContentsMargins(0, 0, 0, 0)

        spinbox = QDoubleSpinBox()
        spinbox.setDecimals(4)
        spinbox.setRange(-1e9, 1e9)
        spinbox.setSingleStep(0.1)
        spinbox.setValue(value)

        remove_button = QPushButton("×")
        remove_button.setFixedWidth(30)
        remove_button.setToolTip("Remove value")
        remove_button.clicked.connect(
            lambda: self.remove_row(row)
        )

        row_layout.addWidget(spinbox)
        row_layout.addWidget(remove_button)

        # Insert before the stretch
        self.rows_layout.insertWidget(
            self.rows_layout.count() - 1,
            row
        )

    def remove_row(self, row):
        self.rows_layout.removeWidget(row)
        row.deleteLater()

    def values(self):
        result = []

        for i in range(self.rows_layout.count() - 1):
            row = self.rows_layout.itemAt(i).widget()
            spinbox = row.findChild(QDoubleSpinBox)
            result.append(spinbox.value())

        return result