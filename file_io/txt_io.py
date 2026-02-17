import pandas as pd
import os
from data_model import Survey, SurveyFrame
from PySide6.QtCore import Qt
from multiprocessing import Queue

from util.coordinate_transformation import CoordinateTransformation
from worker import PWorker


class ReadMagCSV():
    def read_from_BOBCSV(self, filename, delimiter, skiprows, project):
        queue = Queue()
        myPworker = PWorker(pd.read_csv,
                            result_queue=queue,
                            filepath_or_buffer=filename,
                            delimiter=delimiter,
                            skiprows=skiprows,
                            usecols=["Reading_Date", "Reading_Time", "Magnetic_Field", "GPS_Latitude", "GPS_Longitude",
                                     "GPS_Easting", "GPS_Northing"],
                            engine="c",
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
        print(survey_frame_raw.columns)
        survey_frame_raw = survey_frame_raw.drop(
            columns=['Reading_Date', 'Reading_Time']
        )
        survey_frame_raw.rename(columns={r"GPS_Latitude": r"Latitude",
                                         r"GPS_Longitude": r"Longitude",
                                         r"GPS_Easting": r"UTM_Easting",
                                         r"GPS_Northing": r"UTM_Northing"}, inplace=True)
        survey_frame_raw = survey_frame_raw.astype({"Magnetic_Field": "float64",
                                                    "Latitude": "float64",
                                                    "Longitude": "float64",
                                                    "UTM_Easting": "float64",
                                                    "UTM_Northing": "float64"
                                                    })

        survey_id = os.path.basename(filename)
        new_survey = Survey(survey_id)
        new_survey.setCheckState(0, Qt.Checked)
        project.tree.addTopLevelItem(new_survey)
        new_survey_frame = SurveyFrame(survey_id, survey_frame_raw, False)
        new_survey_frame.setCheckState(0, Qt.Checked)
        new_survey.addChild(new_survey_frame)
        project.checked_items()

    def read_from_SeaLINKFolderXYZ(self, path, project):
        """

        :param path:
        :param project:
        :return:
        """

        # For a full record the following columns are required.
        required_cols = ["/Date", "Time", "Field_Mag1", "Longitude", "Latitude",
                         "UTM_Easting", "UTM_Northing"]
        missing_eastnorth = False

        corrupted = []
        survey_id = os.path.basename(path)
        new_survey = Survey(survey_id)
        new_survey.setCheckState(0, Qt.Checked)
        project.tree.addTopLevelItem(new_survey)

        print(os.listdir(path))
        lst = os.listdir(path)
        lst.sort()
        for file in lst:
            if file.endswith(".XYZ"):
                print(file)
                try:
                    survey_frame_header = pd.read_csv(os.path.join(path, file),
                                                      delimiter=",",
                                                      nrows=0,
                                                      engine="python",
                                                      on_bad_lines="warn",
                                                      comment="/ ")
                    missing_cols = set(required_cols) - set(survey_frame_header.columns)

                    # All required columns are present
                    if not missing_cols:
                        usecols = ["/Date", "Time", "Field_Mag1", "Longitude", "Latitude",
                                   "UTM_Easting", "UTM_Northing"]

                    # Old Sealink files often only contain latitudes and longitudes
                    elif missing_cols == {"UTM_Easting", "UTM_Northing"}:
                        usecols = ["/Date", "Time", "Field_Mag1", "Longitude", "Latitude"]
                        missing_eastnorth = True

                    survey_frame_raw = pd.read_csv(os.path.join(path, file),
                                                   delimiter=",",
                                                   usecols=usecols,
                                                   engine="python",
                                                   on_bad_lines="warn",
                                                   comment="/ ")

                    survey_frame_raw.drop(survey_frame_raw.loc[survey_frame_raw["Time"] == "Time"].index, inplace=True)
                    survey_frame_raw.rename(columns={r"Field_Mag1": r"Magnetic_Field"}, inplace=True)

                    if missing_eastnorth:
                        converted_easting, converted_northings = CoordinateTransformation.longlat_to_eastnorth(
                            survey_frame_raw["Longitude"].astype(float),
                            survey_frame_raw["Latitude"].astype(float))
                        survey_frame_raw.loc[:, "UTM_Easting"] = converted_easting
                        survey_frame_raw.loc[:, "UTM_Northing"] = converted_northings

                    survey_frame_raw = survey_frame_raw.astype({"Magnetic_Field": "float64",
                                                                "Latitude": "float64",
                                                                "Longitude": "float64",
                                                                "UTM_Easting": "float64",
                                                                "UTM_Northing": "float64"
                                                                })

                    # Two-step datetime parsing since "parse_dates" was deprecated at development time
                    survey_frame_raw['datetime'] = pd.to_datetime(
                        survey_frame_raw.pop('/Date') + ' ' + survey_frame_raw.pop('Time'))

                    new_survey_frame = SurveyFrame(os.path.basename(file), survey_frame_raw, False)
                    new_survey_frame.setCheckState(0, Qt.Checked)
                    new_survey.addChild(new_survey_frame)


                # Is thrown if the file is empty
                except pd.errors.EmptyDataError:
                    print("Empty file", file)

                except:
                    corrupted.append(os.path.join(path, file))
                    print(file)

        project.checked_items()

    def read_from_customCSV(self, configs, project):
        print(configs["file"])
        survey_frame_raw = pd.read_csv(configs["file"],
                                       delimiter=configs["delimiter"],
                                       skiprows=configs["skip"],
                                       usecols=[configs["date"],
                                                configs["time"],
                                                configs["mag"],
                                                configs["lat"],
                                                configs["long"],
                                                configs["east"],
                                                configs["north"]],
                                       engine="c",
                                       low_memory=False)

        # Two-step datetime parsing since "parse_dates" was deprecated at development time
        survey_frame_raw['datetime'] = pd.to_datetime(
            survey_frame_raw[configs["date"]] + ' ' + survey_frame_raw[configs["time"]])
        print(survey_frame_raw.columns)
        survey_frame_raw = survey_frame_raw.drop(
            columns=[configs["date"], configs["time"]]
        )
        survey_frame_raw.rename(columns={configs["mag"]: r"Magnetic_Field",
                                         configs["lat"]: r"Latitude",
                                         configs["long"]: r"Longitude",
                                         configs["east"]: r"UTM_Easting",
                                         configs["north"]: r"UTM_Northing"}, inplace=True)
        survey_frame_raw = survey_frame_raw.astype({"Magnetic_Field": "float64",
                                                    "Latitude": "float64",
                                                    "Longitude": "float64",
                                                    "UTM_Easting": "float64",
                                                    "UTM_Northing": "float64"
                                                    })
        print(survey_frame_raw)

        survey_id = os.path.basename(configs["file"])
        new_survey = Survey(survey_id)
        new_survey.setCheckState(0, Qt.Checked)
        project.tree.addTopLevelItem(new_survey)
        new_survey_frame = SurveyFrame(survey_id, survey_frame_raw, False)
        new_survey_frame.setCheckState(0, Qt.Checked)
        new_survey.addChild(new_survey_frame)
        project.checked_items()


class WriteMagCSV():
    def write_to_CSV(self, filename, data_frame, columns, sep=","):
        data_frame.to_csv(path_or_buf=filename,
                          sep=sep)
