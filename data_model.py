from PySide6.QtWidgets import QTreeWidgetItem

class Survey(QTreeWidgetItem):
    def __init__(self, name):
        super().__init__()
        self.setText(0, name)


class SurveyFrame(QTreeWidgetItem):
    def __init__(self, name, data_frame, source_corrupted):
        super().__init__()
        self.setText(0, name)
        self.data_frame = data_frame
        self.source_corrupted = source_corrupted


class Anomaly(QTreeWidgetItem):
    def __init__(self, name, coordinates, user_defined):
        super().__init__()
        self.setText(0, name)
        self.coordinates = coordinates
        self.user_defined = user_defined

