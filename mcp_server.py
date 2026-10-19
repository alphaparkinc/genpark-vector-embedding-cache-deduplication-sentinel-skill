"""MCP Server wrapper for Vector Embedding Cache Deduplication Sentinel."""
import json
import sys
from client import VectorEmbeddingCacheDeduplicationSentinel

sentinel = VectorEmbeddingCacheDeduplicationSentinel()

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [
                {
                    "name": "check_embedding_cache",
                    "description": "Check SimHash cache to eliminate redundant embedding API calls",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "text": {"type": "string"},
                            "embedding_dim": {"type": "integer", "default": 1536}
                        },
                        "required": ["text"]
                    }
                }
            ]
        }
    elif method == "tools/call":
        args = req.get("params", {}).get("arguments", {})
        res = sentinel.check_or_store(args.get("text", ""), args.get("embedding_dim", 1536))
        return {
            "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
        }
    return {}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            try:
                r = json.loads(line)
                out = handle_request(r)
                print(json.dumps(out), flush=True)
            except Exception as e:
                print(json.dumps({"error": str(e)}), flush=True)
