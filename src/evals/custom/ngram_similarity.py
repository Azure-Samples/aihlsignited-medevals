from typing import TypedDict, List, Set
import re
from src.evals.custom.custom_evaluator import CustomEvaluator

class NgramSimilarityScore(TypedDict):
    ngram_similarity: float

class NgramSimilarityEvaluator(CustomEvaluator):
    def __init__(self, n: int = 2, lowercase: bool = True, **kwargs):
        super().__init__(**kwargs)
        self.n = n
        self.lowercase = lowercase
        for key, value in kwargs.items():
            setattr(self, key, value)

    def _clean_text(self, text: str) -> str:
        if self.lowercase:
            text = text.lower()
        # Remove punctuation and collapse multiple spaces.
        text = re.sub(r"[^\w\s]", "", text)
        return " ".join(text.split())

    def _tokenize(self, text: str) -> List[str]:
        return text.split()

    def _get_ngrams(self, tokens: List[str]) -> Set[str]:
        ngrams = set()
        if len(tokens) < self.n:
            return ngrams
        for i in range(len(tokens) - self.n + 1):
            ngram = " ".join(tokens[i : i + self.n])
            ngrams.add(ngram)
        return ngrams

    def __call__(self, *, response: str, ground_truth: str, **kwargs) -> NgramSimilarityScore:
        try:
            clean_gt = self._clean_text(ground_truth)
            clean_resp = self._clean_text(response)
            tokens_gt = self._tokenize(clean_gt)
            tokens_resp = self._tokenize(clean_resp)
            ngrams_gt = self._get_ngrams(tokens_gt)
            ngrams_resp = self._get_ngrams(tokens_resp)
            if not ngrams_gt and not ngrams_resp:
                score = 1.0
            else:
                intersection = ngrams_gt.intersection(ngrams_resp)
                union = ngrams_gt.union(ngrams_resp)
                score = len(intersection) / len(union) if union else 0.0
        except Exception:
            score = 0.0
        return {"ngram_similarity": score}