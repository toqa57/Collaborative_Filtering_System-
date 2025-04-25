import pandas as pd
from surprise import Dataset, Reader

def load_movielens_data(file_path='data/u.data'):
    reader = Reader(line_format='user item rating timestamp', sep='\t')
    data = Dataset.load_from_file(file_path, reader=reader)
    return data