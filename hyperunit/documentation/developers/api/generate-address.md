# Generate Address API Documentation

## Overview

The Generate Address API allows you to create unique deposit addresses for transferring assets between different blockchains and Hyperliquid. Each generated address is permanently tied to the destination address and secured by Guardian signatures.

## Endpoint

### Request
`GET /gen/:src_chain/:dst_chain/:asset/:dst_addr`

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `src_chain` | String | Yes | Source blockchain identifier |
| `dst_chain` | String | Yes | Destination blockchain identifier |
| `asset` | String | Yes | Asset symbol to transfer |
| `dst_addr` | String | Yes | Destination address on target chain |

### Supported Values

#### Chains
- `bitcoin` - Bitcoin network
- `ethereum` - Ethereum network
- `solana` - Solana network
- `hyperliquid` - Hyperliquid L1

#### Assets
- `btc` - Bitcoin
- `eth` - Ethereum
- `sol` - Solana
- Additional SPL tokens on Solana

## Example Request

### Generating a Bitcoin deposit address for Hyperliquid

```bash
curl -X GET https://api.hyperunit.xyz/gen/bitcoin/hyperliquid/btc/0x99a5F7202c4983a6f0Ca9d8F0526Fcd9d2be9e1D
```

### Testnet Example

```bash
curl -X GET https://api.hyperunit-testnet.xyz/gen/bitcoin/hyperliquid/btc/0x99a5F7202c4983a6f0Ca9d8F0526Fcd9d2be9e1D
```

## Response Format

### Success Response (200 OK)

```json
{
  "address": "bc1qxyz...",
  "signatures": {
    "field-node": "0x3045022100...",
    "hl-node": "0x3044022100...",
    "node-1": "0x3045022100..."
  },
  "status": "OK"
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `address` | String | The generated deposit address |
| `signatures` | Object | Guardian signatures for verification |
| `status` | String | Operation status ("OK" for success) |

## Guardian Signatures

Each generated address comes with signatures from multiple Guardian nodes for verification:

- **Minimum Required**: 2 Guardian signatures
- **Signature Type**: ECDSA with SHA-256
- **Verification**: Always verify signatures before using addresses

See [Guardian Signatures](/developers/api/generate-address/guardian-signatures) for detailed verification instructions.

## Minimum Deposit Amounts

Deposits below these minimums will not be processed:

| Asset | Minimum Amount | Notes |
|-------|----------------|-------|
| BTC | 0.002 BTC | 200,000 satoshis |
| ETH | 0.05 ETH | 5e16 wei |
| SOL | 0.1 SOL | 100,000,000 lamports |

## Important Notes

### Address Permanence
- Generated addresses are **permanent** and tied to the destination address
- The same parameters will always generate the same deposit address
- Addresses can be reused for multiple deposits

### Security Considerations
1. **Always verify Guardian signatures** before sending funds
2. **Use HTTPS** for all API calls
3. **Store addresses securely** in your application
4. **Monitor the blockchain** for transaction confirmations

### Rate Limits
- Standard rate limits apply as per your API tier
- Consider caching addresses as they are deterministic

## Error Responses

### 400 Bad Request
```json
{
  "error": "Invalid chain combination",
  "status": "ERROR"
}
```

### 404 Not Found
```json
{
  "error": "Unsupported asset",
  "status": "ERROR"
}
```

### 500 Internal Server Error
```json
{
  "error": "Guardian consensus failure",
  "status": "ERROR"
}
```

## Integration Examples

### JavaScript/TypeScript

```javascript
const axios = require('axios');

async function generateDepositAddress(dstAddress) {
  const response = await axios.get(
    `https://api.hyperunit.xyz/gen/bitcoin/hyperliquid/btc/${dstAddress}`
  );
  
  if (response.data.status === 'OK') {
    // Verify signatures before using address
    const isValid = await verifySignatures(
      response.data.signatures,
      response.data.address
    );
    
    if (isValid) {
      return response.data.address;
    }
  }
  
  throw new Error('Failed to generate valid address');
}
```

### Python

```python
import requests
from verify_signatures import verify_guardian_signatures

def generate_deposit_address(dst_address):
    url = f"https://api.hyperunit.xyz/gen/bitcoin/hyperliquid/btc/{dst_address}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            # Verify signatures
            if verify_guardian_signatures(data['signatures'], data['address']):
                return data['address']
    
    raise Exception('Failed to generate valid address')
```

## Next Steps

1. [Verify Guardian Signatures](/developers/api/generate-address/guardian-signatures)
2. [Estimate Transaction Fees](/developers/api/estimate-fees)
3. [Monitor Deposit Lifecycle](/developers/api/operations/deposit-lifecycle)

## Support

For additional help with address generation:
- Review our [FAQ](/faq)
- Contact support at developers@hyperunit.xyz
- Join our [Discord](https://discord.gg/hyperunit)