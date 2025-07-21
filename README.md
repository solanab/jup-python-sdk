# **Jup Python SDK**

A high-performance, async-first Python SDK for seamless interaction with the Jupiter Ultra API, powered by `curl_cffi` for maximum speed and flexibility.<br>
With Ultra API, you don't need to manage or connect to any RPC endpoints, or deal with complex configurations.<br>
Everything from getting quotes to transaction execution happens directly through a powerful API.<br>

Or as we like to say around here:<br>
**"RPCs are for NPCs."**

For a deeper understanding of the Ultra API, including its features and benefits, check out the [Ultra API Docs](https://dev.jup.ag/docs/ultra-api/).

## **Installation**

To install the SDK in your project, run:
```sh
pip install jup-python-sdk
```

## **Quick Start (Async)**

Below is a simple asynchronous example to fetch and execute an Ultra order.

```python
import asyncio
from dotenv import load_dotenv
from jup_python_sdk.clients.ultra_api_client import AsyncUltraApiClient
from jup_python_sdk.models.ultra_api.ultra_order_request_model import UltraOrderRequest

async def main():
   load_dotenv()
   # Note: For async client, methods are awaited.
   client = AsyncUltraApiClient()

   order_request = UltraOrderRequest(
      input_mint="So11111111111111111111111111111111111111112",  # WSOL
      output_mint="EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",  # USDC
      amount=10000000,  # 0.01 WSOL
      taker=await client.get_public_key(),
   )

   try:
      client_response = await client.order_and_execute(order_request)
      signature = str(client_response["signature"])

      print("Order and Execute API Response:")
      print(f"  - Status: {client_response.get('status')}")
      if client_response.get("status") == "Failed":
         print(f"  - Code: {client_response.get('code')}")
         print(f"  - Error: {client_response.get('error')}")

      print(f"  - Transaction Signature: {signature}")
      print(f"  - View on Solscan: https://solscan.io/tx/{signature}")

   except Exception as e:
      print("Error occurred while processing the swap:", str(e))
   finally:
      await client.close()

if __name__ == "__main__":
   asyncio.run(main())
```

> **Note**: A synchronous client (`UltraApiClient`) is also available. See the [examples](./examples) folder for both sync and async usage.

## **Setup Instructions**

Before using the SDK, please ensure you have completed the following steps:

1. **Environment Variables**:  
   Set up your required environment variables.  
   The SDK supports both base58 string and uint8 array formats for your private key.
   ```sh
   # Base58 format
   export PRIVATE_KEY=your_base58_private_key_here

   # OR as a uint8 array
   export PRIVATE_KEY=[10,229,131,132,213,96,74,22,...]
   ```
   
> **Note**: `PRIVATE_KEY` can be either a base58-encoded string (default Solana format), or a uint8 array (e.g. `[181,99,240,...]`). The SDK will automatically detect and parse the format.

2. **Optional Configuration**:  
   Depending on your credentials and setup, you have a couple of options for initializing the `UltraApiClient`:
   - **API Key**: Use an API key from [the Jupiter Portal](https://portal.jup.ag/onboard) for enhanced access. This will use the `https://api.jup.ag/` endpoint.
   - **Custom Private Key Env Var**: Specify a different environment variable name for your private key.

    ```python
    from jup_python_sdk.clients.ultra_api_client import AsyncUltraApiClient

    client = AsyncUltraApiClient(
        api_key="YOUR_API_KEY",
        private_key_env_var="YOUR_CUSTOM_ENV_VAR"
    )
    ```

## **Advanced Configuration (Proxies, Custom DNS)**

The SDK is built on `curl_cffi`, allowing you to pass any valid `curl_cffi` client parameter during initialization for advanced network control.

### Using a SOCKS5 Proxy

```python
from jup_python_sdk.clients.ultra_api_client import AsyncUltraApiClient

proxies = {"httpss": "socks5://user:pass@host:port"}
client = AsyncUltraApiClient(client_kwargs={"proxies": proxies, "impersonate": "chrome110"})
```

### Using Custom DNS Resolution

This is useful for bypassing local DNS caches or using a specialized DNS resolver.

```python
from jup_python_sdk.clients.ultra_api_client import AsyncUltraApiClient

# Tell the client to resolve jup.ag to a specific IP address
resolve_string = "jup.ag:443:1.2.3.4"
client = AsyncUltraApiClient(client_kwargs={"resolve": [resolve_string]})
```

## **Disclaimer**

🚨 **This project is actively worked on.**  
While we don't expect breaking changes as the SDK evolves, we recommend you stay updated with the latest releases.  
Any important updates will be announced in the [Discord server](https://discord.gg/jup).