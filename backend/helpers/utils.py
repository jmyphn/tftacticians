import numpy as np
import re
import os

champions = ["Ahri", "Annie", "Ashe", "AurelionSol", "Blitzcrank", "Caitlyn",
             "ChoGath", "Darius", "Ekko", "Ezreal", "Fiora", "Fizz", "Gangplank",
             "Graves", "Irelia", "JarvanIV", "Jayce", "Jhin", "Jinx", "KaiSa",
             "Karma", "Kassadin", "Kayle", "KhaZix", "Leona", "Lucian", "Lulu",
             "Lux", "Malphite", "MasterYi", "MissFortune", "Mordekaiser", "Neeko",
             "Poppy", "Rakan", "Rumble", "Shaco", "Shen", "Sona", "Soraka", "Syndra",
             "Thresh", "TwistedFate", "VelKoz", "Vi", "WuKong", "Xayah", "Xerath",
             "XinZhao", "Yasuo", "Ziggs", "Zoe"]

# Create a mapping of champion names to their indices for easy access
champions_lower_dict = {champions[i].lower(): i for i in range(len(champions))}  

comatrix_normalized = np.load(os.path.join(os.environ['ROOT_PATH'], 'backend', 'comatrix_normalized.npy'))
comatrix = np.load(os.path.join(os.environ['ROOT_PATH'], 'backend', 'comatrix.npy'))

# Tokenize method which can be passed into various methods.
def tokenize(text):
    """Returns a list of words that make up the text.    

    Parameters
    ----------
    text : str
        The input text string

    Returns
    -------
    list
        A list of tokens corresponding to the input string.
    """
    return [x for x in re.findall(r"[a-z]+", text.lower())]


def recommend_next_champion(user_comp_csv, comatrix_normalized, champions, champions_lower_dict):
    """
    Given a comma-separated list of champion names, returns the champion
    with the highest row-normalized co-occurrence sum that is not already
    in the user's comp.

    user_comp_csv: str, e.g. "Ahri, Annie, Ashe"
    comatrix_normalized: np.array (N x N), row-normalized co-occurrence matrix
    champions: list of str, e.g. ["Ahri", "Annie", "Ashe", ...]
    champions_lower_dict: dict, e.g. {"ahri": 0, "annie": 1, "ashe": 2, ...}

    Return: str, name of the recommended champion
    """

    # Parse the user's champions into a list of lowercase names
    user_champ_list = [champ.strip().lower() for champ in user_comp_csv.split(',') if champ.strip()]

    # Convert each champion to its index (skip any name not in the dictionary)
    user_indices = [champions_lower_dict[c] for c in user_champ_list if c in champions_lower_dict]

    # Accumulate row-normalized co-occurrence scores across all champions in the comp
    # This gives us a "likelihood" score for every other champion
    accum_scores = np.zeros(comatrix_normalized.shape[0])
    for idx in user_indices:
        accum_scores += comatrix_normalized[idx]

    # Exclude champions already in the user's comp by setting their scores to a negative number
    for idx in user_indices:
        accum_scores[idx] = -1_000_000  # any large negative value to ensure they're not chosen

    # Get the index of the champion with the highest score
    recommended_idx = np.argmax(accum_scores)

    # Return the champion name
    return champions[recommended_idx]

def recommend_k_next_champions(user_comp_csv, champions, k=1):
    """
    Given a comma-separated list of champion names, returns the top-k champions
    with the highest row-normalized co-occurrence sum that are not already
    in the user's comp.

    :param user_comp_csv: str, e.g. "Ahri, Annie, Ashe"
    :param comatrix_normalized: np.array (N x N), row-normalized co-occurrence matrix
    :param champions: list of str, e.g. ["Ahri", "Annie", "Ashe", ...]
    :param champions_lower_dict: dict, e.g. {"ahri": 0, "annie": 1, "ashe": 2, ...}
    :param k: int, number of champions to return

    :return: list of str (length <= k), champion names in priority order
    """

    # 1) Parse the user's champions into a list of lowercase names
    user_champ_list = [champ.strip().lower() for champ in user_comp_csv.split(',') if champ.strip()]

    # 2) Convert each champion to its index (skip any name not in the dictionary)
    user_indices = [champions_lower_dict[c] for c in user_champ_list if c in champions_lower_dict]

    # 3) Accumulate row-normalized co-occurrence scores across all champions in the comp
    accum_scores = np.zeros(comatrix_normalized.shape[0])
    for idx in user_indices:
        accum_scores += comatrix_normalized[idx]

    # 4) Exclude champions already in the user's comp by setting their scores to negative
    for idx in user_indices:
        accum_scores[idx] = -1_000_000  # ensure they're not chosen

    # 5) Sort all champions by descending score
    sorted_indices = np.argsort(accum_scores)[::-1]

    # 6) Slice the top-k indices
    top_k_indices = sorted_indices[:k]

    # 7) Return the corresponding champion names in priority order
    return [champions[i] for i in top_k_indices]

# Example usage:
# recommended = recommend_next_champions("Ahri, Annie, Ashe", comatrix_normalized, champions, champions_lower_dict, k=3)
# print("Recommended champions:", recommended)
