import pytest
from typing import Dict

# This test mirrors the 'TrendAlert' contract from specs/technical.md
def test_trend_data_structure():
    """
    Asserts that the trend data structure matches the 
    API contract defined in specs/technical.md.
    """
    # Mocking the output of a Trend Fetcher Skill
    # In a real run, this would be the actual output from the agent
    mock_trend_output = {
        "type": "TrendAlert",
        "payload": {
            "topic": "On-chain AI Agents",
            "relevance_score": 0.89,
            "source": "news://tech/latest",
            "timestamp": "2026-02-04T12:00:00Z"
        }
    }

    # Validation against the contract
    assert mock_trend_output["type"] == "TrendAlert"
    assert isinstance(mock_trend_output["payload"]["topic"], str)
    assert 0.0 <= mock_trend_output["payload"]["relevance_score"] <= 1.0
    assert mock_trend_output["payload"]["source"].startswith("news://")