from jup_ag_sdk.clients.jupiter_client import JupiterClient
from jup_ag_sdk.models.swap_api.quote_request_model import QuoteRequest
from jup_ag_sdk.models.swap_api.swap_request_model import SwapRequest


class SwapApiClient(JupiterClient):
    """
    A client for interacting with the Jupiter Swap API. Inherits from JupiterClient.
    """

    def __init__(
        self, api_key=None, rpc_url="https://api.mainnet-beta.solana.com", private_key_env_var="PRIVATE_KEY", timeout=10
    ):
        super().__init__(
            api_key=api_key,
            rpc_url=rpc_url,
            private_key_env_var=private_key_env_var,
            timeout=timeout,
        )

    def quote(self, request: QuoteRequest) -> dict:
        """
        Get a swap quote from the Jupiter API.

        Args:
            request (QuoteRequest): The request parameters for the quote.

        Returns:
            dict: The dict api response.
        """
        params = request.to_dict()

        url = f"{self.base_url}/swap/v1/quote"
        response = self.client.get(url, params=params, headers=self._get_headers())
        response.raise_for_status()

        return response.json()

    def swap(self, request: SwapRequest) -> dict:
        """
        Submit a swap request to the Jupiter API.

        Args:
            request (SwapRequest): The swap request parameters.

        Returns:
            dict: The parsed response containing transaction details and metadata.
        """
        payload = request.to_dict()

        url = f"{self.base_url}/swap/v1/swap"
        response = self.client.post(url, json=payload, headers=self._get_headers())
        response.raise_for_status()

        return response.json()

    def swap_and_execute(self, request: SwapRequest) -> dict:
        """
        Submit a swap request to the Jupiter API and execute it immediately.

        Args:
            request (SwapRequest): The swap request parameters.

        Returns:
            dict: The raw RPC response containing the result of the transaction execution.
        """
        swap_response = self.swap(request)
        signed_transaction = self._sign_base64_transaction(
            swap_response["swapTransaction"]
        )
        return self._send_transaction(signed_transaction)
