from surprise import accuracy
from collections import defaultdict

def evaluate_rmse(predictions):
    return accuracy.rmse(predictions)

def get_precision_recall_at_k(predictions, k=10, threshold=3.5):
    user_est_true = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        user_est_true[uid].append((est, true_r))
    
    precisions, recalls = {}, {}
    for uid, user_ratings in user_est_true.items():
        user_ratings.sort(key=lambda x: x[0], reverse=True)
        top_k = user_ratings[:k]
        
        tp = sum((true_r >= threshold) for (_, true_r) in top_k)
        total_pred = len(top_k)
        total_rel = sum((true_r >= threshold) for (_, true_r) in user_ratings)
        
        precisions[uid] = tp / total_pred if total_pred else 0
        recalls[uid] = tp / total_rel if total_rel else 0
    
    avg_precision = sum(prec for prec in precisions.values()) / len(precisions)
    avg_recall = sum(rec for rec in recalls.values()) / len(recalls)
    
    return avg_precision, avg_recall
