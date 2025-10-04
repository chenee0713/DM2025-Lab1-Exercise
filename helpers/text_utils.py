import re
from typing import List
import pandas as pd
_WORD_RE = re.compile(r"\w+")

def clean_text(s: str) -> str:
    if not isinstance(s, str):
        return ""
    s = re.sub(r"http\S+|www\.\S+", "", s)
    return s.lower().strip()

def tokenize_simple(s: str) -> List[str]:
    s = clean_text(s)
    return _WORD_RE.findall(s)

def describe_missing_rowwise(df: pd.DataFrame) -> pd.Series:
    return df.isna().sum(axis=1)
