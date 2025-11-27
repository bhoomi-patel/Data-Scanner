import pandas as pd
class DataProfiler:
    def __init__(self,file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)

    def basic_summary(self):
        summary = {
            "num_rows":len(self.df),
            "num_cols":len(self.df.columns),
            "missing_values":self.df.isnull().sum().to_dict(),
            "data_types":self.df.dtypes.astype(str).to_dict()
        }
        return summary

    def numeric_summary(self):
        return self.df.describe().to_dict()

    def categorical_summary(self):
        cat_cols = self.df.select_dtypes(include=['object','category']).columns
        summary={}
        for col in cat_cols:
            summary[col]={
                "unique_values":self.df[col].nunique(),
                "most_common":self.df[col].value_counts().head(5).to_dict()
            }
        return summary
