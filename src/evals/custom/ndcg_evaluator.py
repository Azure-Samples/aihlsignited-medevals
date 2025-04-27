from beir.retrieval.evaluation import EvaluateRetrieval

class NDCGEvaluator:
    def __init__(self, k: int):
        self.k = k

    def __call__(self, *, response: dict, ground_truth: dict, query_id: str, **kwargs):
        ranking = response.get("ranking", {})
        qrels = {query_id: ground_truth}
        results = EvaluateRetrieval().evaluate(qrels, {query_id: ranking}, k_values=[self.k])
        return {f"NDCG@{self.k}": results[0].get(f"NDCG@{self.k}", 0.0)}