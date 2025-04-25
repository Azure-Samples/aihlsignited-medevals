import json

class SearchRecallEvaluator:
    def __init__(self, k: int):
        self.k = k

    def __call__(self, *, ranking: str, ground_truth: str, **kwargs):
        # Parse inputs
        run_map   = json.loads(ranking)           # {doc_id: score, ...}
        qrels_map = json.loads(ground_truth)       # {doc_id: relevance, ...}

        # Identify relevant docs (rel > 0)
        relevant_docs = {doc for doc, rel in qrels_map.items() if int(rel) > 0}
        if not relevant_docs:
            # no relevant docs => define recall as 0.0
            return {f"Recall@{self.k}": 0.0}

        # Sort by score descending, take top-k
        topk = sorted(run_map, key=lambda d: run_map[d], reverse=True)[: self.k]

        # Count hits
        hits = sum(1 for doc in topk if doc in relevant_docs)
        recall = hits / len(relevant_docs)
        return {f"Recall@{self.k}": recall}