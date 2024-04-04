import pandas as pd
from .settings import GFORM_RESPONSES_EXPORT


df = pd.read_csv(GFORM_RESPONSES_EXPORT)
print(df)


def get_student_proficiency_by_id(id):
    proficiency = df.loc[df['student_id'] == id, 'proficiency'].values[0]
    return proficiency


def get_student_class_by_id(id):
    class_ = df.loc[df['student_id'] == id, 'student_class'].values[0]
    return class_


# print(get_student_proficiency_by_id(id=101))
