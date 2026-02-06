# Chimera Agent: Runtime Skills

This directory contains the capability packages used by the Chimera Agent Swarm. Each skill follows a strict Input/Output contract to ensure interoperability.

## 1. Skill: trend_analyzer
- **Description**: Ingests raw data from news and social MCP resources to identify viral clusters.
- **Input Contract**: `{ "source_data": string[], "threshold": float }`
- **Output Contract**: `{ "detected_trends": [ { "topic": string, "score": float } ] }`

## 2. Skill: multimodal_generator
- **Description**: Orchestrates specialized MCP tools (Ideogram/Runway) to create character-consistent assets.
- **Input Contract**: `{ "prompt": string, "lora_id": string, "asset_type": "image" | "video" }`
- **Output Contract**: `{ "asset_url": string, "generation_metadata": JSON }`

## 3. Skill: financial_governor (CFO)
- **Description**: Validates transaction requests against the $50 USDC daily budget before calling Coinbase AgentKit.
- **Input Contract**: `{ "proposed_tx": { "to": string, "amount": float } }`
- **Output Contract**: `{ "status": "approved" | "rejected", "remaining_budget": float }`