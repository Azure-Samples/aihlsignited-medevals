import json

class SearchRecallEvaluator:
    def __init__(self, k: int):
        self.k = k

    def __call__(self, *, context: dict, ground_truth: dict, **kwargs):
        # extract ranking from context
        run_map = context.get("ranking", {})
        qrels_map = ground_truth

        relevant = {doc for doc, rel in qrels_map.items() if rel > 0}
        if not relevant:
            return {f"Recall@{self.k}": 0.0}

        topk = sorted(run_map, key=lambda d: run_map[d], reverse=True)[: self.k]
        hits = sum(1 for doc in topk if doc in relevant)
        return {f"Recall@{self.k}": hits / len(relevant)}