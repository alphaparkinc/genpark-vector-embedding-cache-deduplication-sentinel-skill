"""Example usage for Vector Embedding Cache Deduplication Sentinel."""
from client import VectorEmbeddingCacheDeduplicationSentinel

if __name__ == "__main__":
    sentinel = VectorEmbeddingCacheDeduplicationSentinel()
    res1 = sentinel.check_or_store("Semantic retrieval prompt query")
    res2 = sentinel.check_or_store("Semantic retrieval prompt query")
    print("First call:", res1)
    print("Second call (cached):", res2)
