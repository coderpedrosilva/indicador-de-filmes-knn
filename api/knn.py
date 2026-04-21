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
        match = df[df["filme"]==filme]
        if match.empty:
            continue
        vectors.append(match.iloc[0][FEATURES].values * nota)
        weights.append(nota)

    total_weight = np.sum(weights)
    if not vectors or total_weight == 0:
        return None

    return np.sum(vectors, axis=0) / total_weight

def recommend_knn(ratings, df, k=5):
    profile = build_user_profile(ratings, df)
    if profile is None:
        return []

    norm_df, mins, maxs = normalize_dataset(df, FEATURES)
    profile_norm = normalize_user(profile, mins.values, maxs.values)

    candidates=[]

    for i,row in df.iterrows():
        if row["filme"] in ratings:
            continue

        movie_norm = norm_df.loc[i].values
        d = euclidean(profile_norm, movie_norm)
        candidates.append((row["filme"],row["classe"],float(d)))

    candidates.sort(key=lambda x:x[2])

    top = candidates[:15]
    main = top[:3]
    explore = random.sample(top[3:], min(2, len(top[3:])))

    final=[]
    used_classes=set()

    for f in main+explore:
        if f[1] not in used_classes:
            final.append(f)
            used_classes.add(f[1])
        if len(final)==k:
            break

    return final
