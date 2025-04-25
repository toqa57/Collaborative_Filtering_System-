from surprise import KNNBasic

def train_knn_model(trainset, user_based=True):
    sim_options = {
        'name': 'cosine',
        'user_based': user_based
    }
    model = KNNBasic(sim_options=sim_options)
    model.fit(trainset)
    return model

def get_top_n(predictions, n=10):
    from collections import defaultdict
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]
    return top_n
