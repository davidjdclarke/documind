import pandas as pd

from typing import List


class Questions:
    def __init__(self, file_path: str = "resources/questions.csv"):
        self.file_path = file_path
        self.questions = pd.read_csv(self.file_path)
        
    def get_questions(self, type: str) -> List:
        return self.questions.iloc[self.questions["type"] == type]