import sys
import pandas as pd
import numpy as np

from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidget,QTreeWidgetItem
from PySide6.QtGui import QStandardItemModel,QStandardItem, QFont, QColor
from PySide6.QtCore import Qt


class Survey(QTreeWidgetItem):
    def __init__( self, name):
        super().__init__( )
        self.setText(0, name)

class SurveyFrame(QTreeWidgetItem):
    def __init__( self, name, df):
        super().__init__()
        self.setText(0, name)
        self.df = df

class TreeUtil():
    def __init__(self, tree, selected_df):
        self.tree = tree
        self.selected_df = selected_df

    def checked_items(self):
        checked_items = []
        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                else:
                    if child.checkState(0) == Qt.Checked:
                        checked_items.append(child)

        recurse(self.tree.invisibleRootItem())

        survey_combined = pd.DataFrame()
        for item in checked_items:
            print(item.text(0))
            survey_combined = pd.concat([survey_combined, item.data_frame])

        self.selected_df = survey_combined
        print(survey_combined)


