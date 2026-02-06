import pytest

def test_multimodal_generator_interface():
    """
    Asserts that the content_generator skill accepts 
    the correct parameter contracts.
    """
    # This represents the 'Input Contract' defined in skills/README.md
    input_contract = {
        "prompt": "Cyberpunk influencer in Addis Ababa",
        "lora_id": "chimera_v1_lora",
        "asset_type": "video"
    }

    # Logic to verify that our Skill package can parse this specific JSON
    # Since the skill is not implemented yet, this test will fail upon import
    from skills.multimodal_generator import validate_input
    
    assert validate_input(input_contract) is True

def test_financial_governor_budget_limit():
    """
    Asserts the 'CFO' skill enforces the $50 USDC budget constraint.
    """
    from skills.financial_governor import check_budget
    
    # Attempting a transaction over the $50 limit defined in specs/technical.md
    high_value_tx = {"amount_usdc": 60.0}
    
    with pytest.raises(Exception) as excinfo:
        check_budget(high_value_tx)
    assert "BudgetExceededError" in str(excinfo.value)