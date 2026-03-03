import json
from pathlib import Path


class ProjectIO:
    def save_project(self, tree, target_dir, project_name):
        target_dir = Path(target_dir)

        root = tree.invisibleRootItem()

        surveys = []

        for i in range(root.childCount()):
            print(root.child(i))
            survey_frames = []
            survey_name = root.child(i).text(0)
            survey_dir = target_dir / survey_name
            Path.mkdir(survey_dir, parents=True, exist_ok=True)

            for j in range(root.child(i).childCount()):
                survey_frame_name = root.child(i).child(j).text(0)
                source_corrupted = root.child(i).child(j).model.source_corrupted


                df = root.child(i).child(j).model.data_frame
                file_path = survey_dir / survey_frame_name
                df.to_parquet(file_path)

                relative_path = file_path.relative_to(target_dir)
                survey_frame = {"name": survey_frame_name,
                                "file": str(relative_path),
                                "source_corrupted": source_corrupted}

                survey_frames.append(survey_frame)




            survey = {"name": survey_name,
                      "frames": survey_frames}
            surveys.append(survey)

        project = {"name": project_name,
                   "surveys": surveys}


        with open(target_dir / f"{project_name}.json", "w") as file:
            json.dump(project, file, indent=4)


    def load_project(self):
        return 0
