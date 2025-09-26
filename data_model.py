from PySide6.QtWidgets import QTreeWidgetItem
from PySide6.QtCore import Qt


class MyQTreeWidgetItem(QTreeWidgetItem):
    def __init__(self, name):
        super().__init__()
        self.setText(0, name)
        self.setFlags(self.flags() | Qt.ItemIsEditable)
        self.name = name

    def change_text(self):
        self.name = self.text(0)




class Survey(MyQTreeWidgetItem):
    def __init__(self, name):
        super().__init__(name)



class SurveyFrame(MyQTreeWidgetItem):
    def __init__(self, name, data_frame, source_corrupted):
        super().__init__(name)
        self.data_frame = data_frame
        self.source_corrupted = source_corrupted


class Anomaly(MyQTreeWidgetItem):
    def __init__(self, name, coordinates, user_defined):
        super().__init__(name)
        self.coordinates = coordinates
        self.user_defined = user_defined

