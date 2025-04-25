import os
import re
from dataclasses import dataclass
from difflib import SequenceMatcher

@dataclass
class SequenceSimilarity:
    sequence_similarity: float


class SequenceEvaluator():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def _clean_text(self, text: str) -> str:
        # Remove newlines/tabs and collapse whitespace
        return " ".join(text.replace("\n", " ").replace("\t", " ").split())

    def _ratio(self, a: str, b: str) -> float:
        # SequenceMatcher.ratio() returns a float in [0,1]
        return SequenceMatcher(None, a, b).ratio() * 100

    def _sliding_window_fuzzy_match(
        self, ground_truth: str, response: str, step: int = 1
    ) -> tuple[float, str, int]:
        window_size = len(ground_truth)
        best_score = 0.0
        best_window = ""
        best_index = -1

        for i in range(0, len(response) - window_size + 1, step):
            window = response[i : i + window_size]
            score = self._ratio(ground_truth, window)
            if score > best_score:
                best_score = score
                best_window = window
                best_index = i
                if best_score == 100.0:
                    break

        return best_score, best_window, best_index

    def __call__(
        self, *, response: str, ground_truth: str, **kwargs
    ) -> SequenceSimilarity:
        try:
            clean_gt = self._clean_text(ground_truth)
            step = int(kwargs.get("step", 10))
            score, window, idx = self._sliding_window_fuzzy_match(
                clean_gt, response, step=step
            )
            self.logger.info(f"Best score {score:.2f}% at index {idx}.")
        except Exception as e:
            self.logger.error(f"Error computing similarity: {e}")
            score = 0.0

        return SequenceSimilarity(sequence_similarity=score)