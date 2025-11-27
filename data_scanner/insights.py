import numpy as np
from scipy.stats import skew
class DataInsights:
    def __init__(self,df):
        self.df=df
    def skewness_suggestions(self):
        num_cols = self.df.select_dtypes(include=np.number).columns
        suggestions = {}
        for col in num_cols:
            sk = skew(self.df[col].dropna())
            if abs(sk) > 1:
                suggestions[col] = f"Highly skewed (skewness={sk:.2f}). Consider log transformation."
        return suggestions
    def correlation_analysis(self):
        corr = self.df.select_dtypes(include = np.number).corr()
        corr_unstacked = corr.unstack().sort_values(ascending=False)
        corr_unstacked = corr_unstacked[corr_unstacked.index.get_level_values(0) != corr_unstacked.index.get_level_values(1)]
        top_positives = corr_unstacked.head(5)
        top_negatives = corr_unstacked.tail(5)
        return {
            "top_positive":top_positives.to_dict(),
            "top_negative":top_negatives.to_dict()
        }
    def cardinality_warnings(self):
        cat_cols = self.df.select_dtypes(include=['object','category']).columns
        warnings = {}
        for col in cat_cols:
            unique_count = self.df[col].nunique()
            if unique_count > 50:
                warnings[col] = f"High cardinality detected ({unique_count} unique values). Check before one-hot encoding."
        return warnings