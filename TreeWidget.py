import sys
import pandas as pd
import numpy as np
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidget,QTreeWidgetItem
from PySide6.QtGui import QStandardItemModel,QStandardItem, QFont, QColor
from PySide6.QtCore import Qt

from util.data_manipulation import DataManipulator
from threading import Thread

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
        self.checked_items_list = []
        self.data_manipulator = DataManipulator

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
        self.checked_items_list = checked_items
        recurse(self.tree.invisibleRootItem())
        survey_combined = pd.concat([item.data_frame for item in checked_items], ignore_index=True)
        self.selected_df = survey_combined
        #print("survey combined")
        #print(survey_combined)
        #print(survey_combined.shape)
        #print("  ")

    def ffill_outlier(self, max_mag, min_mag, max_long, min_long, max_lat, min_lat):
        for item in self.checked_items_list:
            self.data_manipulator.ffill_outlier_from_df(
                item.data_frame,max_mag, min_mag, max_long, min_long, max_lat, min_lat)
        self.checked_items()


    def dropna_outlier(self, max_mag, min_mag, max_long, min_long, max_lat, min_lat):
        for item in self.checked_items_list:
            self.data_manipulator.dropna_outlier_from_df(
                item.data_frame,max_mag, min_mag, max_long, min_long, max_lat, min_lat)
        self.checked_items()

    def drop_from_lasso_select(self, selected_points):
        for item in self.checked_items_list:
            thread = Thread(target=self.data_manipulator.drop_from_lasso_select,
                            args=(item.data_frame,
                                  selected_points))
            thread.start()

    def write_surveys_to_csv(self):
        self.checked_items()

        output_dir = "processed"
        os.makedirs(output_dir, exist_ok=True)

        for item in self.checked_items_list:
            filename = os.path.join(output_dir, item.text(0))
            item.data_frame.to_csv(filename, index=False)


