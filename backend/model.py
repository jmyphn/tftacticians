import pandas as pd
import numpy as np
from sklearn.preprocessing import normalize
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse.linalg import svds
import re


# Stores the Information Retrieval System model
def tokenize(s):
    return re.split(r"\W+", s.lower())
