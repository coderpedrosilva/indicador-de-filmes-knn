import numpy as np
import random
from .normalizer import normalize_dataset, normalize_user

FEATURES = ["violencia","romance","acao","comedia"]

def euclidean(a,b):
    return np.sqrt(np.sum((a-b)**2))

def build_user_profile(ratings, df):
    vectors=[]
    weights=[]

    for filme,nota in ratings.items():
        row = df[df["filme"]==filme].iloc[0]
        vectors.append(row[FEATURES].values * nota)
        weights.append(nota)

    return np.sum(vectors, axis=0) / np.sum(weights)

def recommend_knn(ratings, df, k=5):
    profile = build_user_profile(ratings, df)

    norm_df, mins, maxs = normalize_dataset(df, FEATURES)
    profile_norm = normalize_user(profile, mins.values, maxs.values)

    candidates=[]

    for i,row in df.iterrows():
        if row["filme"] in ratings:
            continue

        movie_norm = norm_df.iloc[i].values
        d = euclidean(profile_norm, movie_norm)
        candidates.append((row["filme"],row["classe"],float(d)))

    candidates.sort(key=lambda x:x[2])

    top = candidates[:15]
    main = top[:3]
    explore = random.sample(top[3:],2)

    final=[]
    used_classes=set()

    for f in main+explore:
        if f[1] not in used_classes:
            final.append(f)
            used_classes.add(f[1])
        if len(final)==k:
            break

    return final
