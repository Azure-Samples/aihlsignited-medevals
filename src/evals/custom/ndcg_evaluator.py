import json
from beir.retrieval.evaluation import EvaluateRetrieval

class NDCGEvaluator:
    def __init__(self, k: int):
        self.k = k

    def __call__(self, *, ranking: str, ground_truth: str, query_id: str, **kwargs):
        run   = json.loads(ranking)
        qrels = { query_id: json.loads(ground_truth) }
        results = EvaluateRetrieval().evaluate(qrels, {query_id: run}, k_values=[self.k])
        return { f"NDCG@{self.k}": results[0].get(f"NDCG@{self.k}", 0.0) }
