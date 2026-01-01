import numpy as np
from collections import Counter
from normalizer import normalize_dataset, normalize_user

def euclidean(a,b):
    return np.sqrt(np.sum((a-b)**2))

def knn(user_vector, df, k=5):
    cols = ["violencia","romance","acao","comedia"]
    norm_df, mins, maxs = normalize_dataset(df, cols)
    user_norm = normalize_user(np.array(user_vector), mins.values, maxs.values)

    distances=[]
    for i,row in df.iterrows():
        movie_norm = norm_df.iloc[i].values
        d = euclidean(user_norm, movie_norm)
        distances.append((row["filme"],row["classe"],float(d)))

    distances.sort(key=lambda x:x[2])
    return distances[:k]
