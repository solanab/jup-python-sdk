from dotenv import load_dotenv

from jup_python_sdk.clients.ultra_api_client import UltraApiClient
from jup_python_sdk.models.ultra_api.ultra_order_request_model import (
    UltraOrderRequest,
)


def test_ultra_get_order_and_execute() -> None:
    """
    Test the UltraApiClient's ability to fetch an order and execute it.
    """
    load_dotenv()
    client = UltraApiClient()

    order_request = UltraOrderRequest(
        input_mint="So11111111111111111111111111111111111111112",  # WSOL
        output_mint="EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",  # USDC
        amount=10000000,  # 0.01 WSOL
        taker=client._get_public_key(),
    )

    try:
        client_response = client.order_and_execute(order_request)
        signature = str(client_response["signature"])
        assert (
            signature is not None
        ), "Transaction signature is missing or invalid."

        print()
        print("Order and Execute API Response:")
        print(f"  - Transaction Signature: {signature}")
        print(f"  - View on Solscan: https://solscan.io/tx/{signature}")

    except Exception as e:
        print("Error occurred while processing the order:", str(e))
    finally:
        client.close()
