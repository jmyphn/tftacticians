import numpy as np
import pandas as pd
from sklearn.preprocessing import normalize
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse.linalg import svds
from helpers.utils import tokenize, champions

class SVDSearcher:
    def __init__(self, champion_descriptions, num_features=50):
        """
        Initialize the SVD search engine with champion descriptions
        
        Parameters:
        -----------
        champion_descriptions : list
            List of text descriptions for each champion
        num_features : int
            Number of latent features for SVD
        """
        self.champion_descriptions = champion_descriptions
        self.num_features = num_features
        self.champions = champions
        
        self.vectorizer = TfidfVectorizer(
            tokenizer=tokenize,
            stop_words='english',
            min_df=2,
            max_df=0.8
        )
        
        self.dt_matrix = self.vectorizer.fit_transform(champion_descriptions)
        
        # feature names/words
        self.features = self.vectorizer.get_feature_names_out()

        u, s, vt = svds(self.dt_matrix, k=num_features) # USV^T
        
        self.document_vectors = normalize(u @ np.diag(s))
        
        self.concept_term_matrix = vt
        
    def search(self, query):
        """
        Search for champions similar to the query
        
        Parameters:
        -----------
        query : str
            The search query
            
        Returns:
        --------
        np.ndarray
            Similarity scores for all champions
        """
        query_vector = self.vectorizer.transform([query])
        
        query_latent = query_vector @ self.concept_term_matrix.T        
        query_latent = normalize(query_latent)

        similarities = self.document_vectors @ query_latent.T # all similarities
        similarities = np.maximum(similarities, 0)
        
        # return similarity scores for all champions
        return similarities