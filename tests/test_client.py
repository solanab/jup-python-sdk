import pytest

from jup_ag_sdk.client import JupiterClient


@pytest.fixture
def client() -> JupiterClient:
    return JupiterClient()


def test_get_quote(client: JupiterClient) -> None:
    """Test the get_quote function."""
    response = client.get_quote("SOL", "USDC", 1000000)
    assert response["inputMint"] == "SOL"
    assert response["outputMint"] == "USDC"
    assert response["amount"] == "1000000"
    assert "quote" in response
