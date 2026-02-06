All inter-agent communication must follow a strictly typed JSON schema.
```json
{
  "type": "TrendAlert",
  "payload": {
    "topic": "string",
    "relevance_score": "float (0.0-1.0)",
    "source_mcp": "string (resource_uri)",
    "timestamp": "ISO8601"
  }
}