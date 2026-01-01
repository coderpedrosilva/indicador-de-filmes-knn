import numpy as np

def normalize_dataset(df, cols):
    min_vals = df[cols].min()
    max_vals = df[cols].max()
    return (df[cols] - min_vals) / (max_vals - min_vals), min_vals, max_vals

def normalize_user(user, min_vals, max_vals):
    return (user - min_vals) / (max_vals - min_vals)
