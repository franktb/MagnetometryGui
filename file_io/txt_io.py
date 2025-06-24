import pandas as pd
import os
from data_model import Survey, SurveyFrame
from PySide6.QtCore import Qt
from multiprocessing import Queue

from worker import PWorker


class ReadMagCSV():
    def read_from_BOBCSV(self, filename, delimiter, skiprows, project):
        queue = Queue()
        myPworker = PWorker(pd.read_csv,
                            result_queue=queue,
                            filepath_or_buffer=filename,
                            delimiter=delimiter,
                            skiprows=skiprows,
                            usecols=["Reading_Date", "Reading_Time", "Magnetic_Field", "GPS_Latitude","GPS_Longitude", "GPS_Easting", "GPS_Northing"],
                            engine ="c",
                            low_memory=False,
                            dtype=str
                            )
        myPworker.start()
        survey_frame_raw = queue.get()
        myPworker.join()


        # The BOB software indicated missing GPS locations by "*"
        survey_frame_raw = survey_frame_raw[survey_frame_raw["GPS_Longitude"].str.contains(r"\*") == False]

        # Two-step datetime parsing since "parse_dates" was deprecated at development time
        survey_frame_raw['datetime'] = pd.to_datetime(
            survey_frame_raw['Reading_Date'] + ' ' + survey_frame_raw['Reading_Time'])

        survey_frame_raw.rename(columns={r"GPS_Latitude": r"Latitude",
                                         r"GPS_Longitude": r"Longitude",
                                         r"GPS_Easting": r"UTM_Easting",
                                         r"GPS_Northing": r"UTM_Northing"}, inplace=True)
        survey_frame_raw = survey_frame_raw.astype({"Magnetic_Field":"float64",
                                 "Latitude":"float64",
                                 "Longitude":"float64",
                                 "UTM_Easting":"float64",
                                 "UTM_Northing":"float64"
                                                    })

        survey_id = os.path.basename(filename)
        new_survey = Survey(survey_id)
        new_survey.setCheckState(0,Qt.Checked)
        project.tree.addTopLevelItem(new_survey)
        new_survey_frame = SurveyFrame(survey_id, survey_frame_raw, False)
        new_survey_frame.setCheckState(0,Qt.Checked)
        new_survey.addChild(new_survey_frame)
        project.checked_items()
        

    def read_from_SeaLINKFolderXYZ(self, path, project):
        corrupted = []
        survey_id = os.path.basename(path)
        new_survey = Survey(survey_id)
        new_survey.setCheckState(0, Qt.Checked)
        project.tree.addTopLevelItem(new_survey)

        print(os.listdir(path))
        for file in os.listdir(path):
            if file.endswith(".XYZ"):
                try:
                    survey_frame_raw = pd.read_csv(os.path.join(path, file),
                                                   delimiter=",",
                                                   usecols=["/Date", "Time", "Field_Mag1", "Longitude", "Latitude","UTM_Easting","UTM_Northing"],
                                                   engine="python",
                                                   on_bad_lines="warn",
                                                   comment="/ ")



                    survey_frame_raw.drop(survey_frame_raw.loc[survey_frame_raw["Time"] == "Time"].index, inplace=True)
                    survey_frame_raw.rename(columns={r"Field_Mag1": r"Magnetic_Field"}, inplace=True)

                    survey_frame_raw = survey_frame_raw.astype({"Magnetic_Field": "float64",
                                             "Latitude": "float64",
                                             "Longitude": "float64",
                                            })

                    # Two-step datetime parsing since "parse_dates" was deprecated at development time
                    survey_frame_raw['datetime'] = pd.to_datetime(
                        survey_frame_raw.pop('/Date') + ' ' + survey_frame_raw.pop('Time'))

                    new_survey_frame = SurveyFrame(os.path.basename(file), survey_frame_raw, False)
                    new_survey_frame.setCheckState(0, Qt.Checked)
                    new_survey.addChild(new_survey_frame)

                except:
                    corrupted.append(os.path.join(path, file))

        project.checked_items()
        

    def read_from_customCSV(self, filename, delimiter, skiprows, usecols ,project):
        survey_frame_raw = pd.read_csv(filename,
                                       delimiter=delimiter,
                                       skiprows=skiprows,
                                       usecols = usecols,
                                       #usecols=["Reading_Date", "Reading_Time", "Magnetic_Field", "GPS_Latitude",
                                       #         "GPS_Longitude", "GPS_Easting", "GPS_Northing"],
                                       engine="c",
                                       low_memory=False)

        # The BOB software indicated missing GPS locations by "*"
        survey_frame_raw = survey_frame_raw[survey_frame_raw["GPS_Longitude"].str.contains(r"\*") == False]
        print(survey_frame_raw.columns.values)
        # Two-step datetime parsing since "parse_dates" was deprecated at development time
        survey_frame_raw['datetime'] = pd.to_datetime(
            survey_frame_raw['Reading_Date'] + ' ' + survey_frame_raw['Reading_Time'])

        #survey_frame_raw.rename(columns={r"GPS_Latitude": r"Latitude", r"GPS_Longitude": r"Longitude"},
        #                        inplace=True)
        survey_frame_raw.columns = ['Date', 'Time', 'Easting', 'Northing', 'Magnetic_Field']
        survey_frame_raw.astype({"Magnetic_Field": "float64",
                                 "Latitude": "float64",
                                 "Longitude": "float64",
                                 "GPS_Easting": "float64",
                                 "GPS_Northing": "float64"})

        survey_id = os.path.basename(filename)
        new_survey = Survey(survey_id)
        new_survey.setCheckState(0, Qt.Checked)
        project.tree.addTopLevelItem(new_survey)
        new_survey_frame = SurveyFrame(survey_id, survey_frame_raw, False)
        new_survey_frame.setCheckState(0, Qt.Checked)
        new_survey.addChild(new_survey_frame)
        project.checked_items()
        
class WriteMag():
    def write_to_CSV(self, filename, data_frame, columns,sep=","):
        data_frame.to_csv(path_or_buf=filename,
                          sep=sep)
