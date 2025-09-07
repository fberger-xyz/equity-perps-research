# Estimate Fees API Documentation

## Overview

The Estimate Fees API provides real-time fee estimates and processing times for deposits and withdrawals across all supported blockchain networks. This endpoint helps users and applications make informed decisions about transaction timing and costs.

## Endpoint

### Request
`GET /v2/estimate-fees`

### Base URLs
- **Production**: `https://api.hyperunit.xyz/v2/estimate-fees`
- **Testnet**: `https://api.hyperunit-testnet.xyz/v2/estimate-fees`

## Response Format

The API returns a comprehensive fee structure for all supported networks:

```json
{
  "bitcoin": {
    "deposit-fee-rate-sats-per-vb": 8,
    "deposit-size-v-bytes": 113,
    "depositEta": "21m",
    "depositFee": 1404,
    "withdrawal-fee-rate-sats-per-vb": 5,
    "withdrawal-size-v-bytes": 143,
    "withdrawalEta": "44m",
    "withdrawalFee": 715
  },
  "ethereum": {
    "base-fee": 4180642406,
    "depositEta": "3m",
    "depositFee": 542339092071454,
    "eth-deposit-gas": 21000,
    "eth-withdrawal-gas": 50000,
    "priority-fee": 7000,
    "withdrawalEta": "7m",
    "withdrawalFee": 209032470300000
  },
  "solana": {
    "depositEta": "1m",
    "depositFee": 8711125,
    "withdrawalEta": "4m",
    "withdrawalFee": 8000
  },
  "spl": {
    "depositEta": "1m",
    "depositFee": 7857245,
    "withdrawalEta": "4m",
    "withdrawalFee": 2815836
  }
}
```

## Network-Specific Fields

### Bitcoin
| Field | Type | Description | Unit |
|-------|------|-------------|------|
| `deposit-fee-rate-sats-per-vb` | Integer | Fee rate for deposits | satoshis/vByte |
| `deposit-size-v-bytes` | Integer | Typical deposit transaction size | vBytes |
| `depositFee` | Integer | Total deposit fee | satoshis |
| `depositEta` | String | Estimated deposit confirmation time | minutes |
| `withdrawal-fee-rate-sats-per-vb` | Integer | Fee rate for withdrawals | satoshis/vByte |
| `withdrawal-size-v-bytes` | Integer | Typical withdrawal transaction size | vBytes |
| `withdrawalFee` | Integer | Total withdrawal fee | satoshis |
| `withdrawalEta` | String | Estimated withdrawal processing time | minutes |

### Ethereum
| Field | Type | Description | Unit |
|-------|------|-------------|------|
| `base-fee` | Integer | Current base fee per gas | wei |
| `priority-fee` | Integer | Priority fee (tip) per gas | wei |
| `eth-deposit-gas` | Integer | Gas required for deposits | gas units |
| `eth-withdrawal-gas` | Integer | Gas required for withdrawals | gas units |
| `depositFee` | Integer | Total deposit fee | wei |
| `withdrawalFee` | Integer | Total withdrawal fee | wei |
| `depositEta` | String | Estimated deposit confirmation time | minutes |
| `withdrawalEta` | String | Estimated withdrawal processing time | minutes |

### Solana
| Field | Type | Description | Unit |
|-------|------|-------------|------|
| `depositFee` | Integer | Total deposit fee | lamports |
| `withdrawalFee` | Integer | Total withdrawal fee | lamports |
| `depositEta` | String | Estimated deposit confirmation time | minutes |
| `withdrawalEta` | String | Estimated withdrawal processing time | minutes |

### SPL Tokens
| Field | Type | Description | Unit |
|-------|------|-------------|------|
| `depositFee` | Integer | Total deposit fee | lamports |
| `withdrawalFee` | Integer | Total withdrawal fee | lamports |
| `depositEta` | String | Estimated deposit confirmation time | minutes |
| `withdrawalEta` | String | Estimated withdrawal processing time | minutes |

## Fee Calculation

### Bitcoin
```javascript
// Calculate total fee in satoshis
const totalFee = feeRatePerVByte * transactionSizeVBytes;

// Convert to BTC
const feeBTC = totalFee / 100000000;
```

### Ethereum
```javascript
// Calculate total fee in wei
const gasPrice = baseFee + priorityFee;
const totalFee = gasPrice * gasUnits;

// Convert to ETH
const feeETH = totalFee / 1e18;
```

### Solana
```javascript
// Fee is already calculated in lamports
const feeSOL = fee / 1e9;
```

## Usage Examples

### JavaScript/TypeScript

```javascript
const axios = require('axios');

async function getEstimatedFees() {
  try {
    const response = await axios.get('https://api.hyperunit.xyz/v2/estimate-fees');
    const fees = response.data;
    
    // Bitcoin fees
    console.log(`BTC Deposit: ${fees.bitcoin.depositFee} sats (ETA: ${fees.bitcoin.depositEta})`);
    console.log(`BTC Withdrawal: ${fees.bitcoin.withdrawalFee} sats (ETA: ${fees.bitcoin.withdrawalEta})`);
    
    // Ethereum fees
    const ethDepositFee = fees.ethereum.depositFee / 1e18;
    console.log(`ETH Deposit: ${ethDepositFee} ETH (ETA: ${fees.ethereum.depositEta})`);
    
    // Solana fees
    const solDepositFee = fees.solana.depositFee / 1e9;
    console.log(`SOL Deposit: ${solDepositFee} SOL (ETA: ${fees.solana.depositEta})`);
    
    return fees;
  } catch (error) {
    console.error('Failed to fetch fees:', error);
    throw error;
  }
}

// Calculate if fee is acceptable
function isFeeAcceptable(network, operation, maxFeeInUSD, priceInUSD) {
  const fees = await getEstimatedFees();
  const feeAmount = operation === 'deposit' 
    ? fees[network].depositFee 
    : fees[network].withdrawalFee;
  
  // Convert to USD based on network
  let feeInUSD;
  switch(network) {
    case 'bitcoin':
      feeInUSD = (feeAmount / 1e8) * priceInUSD.btc;
      break;
    case 'ethereum':
      feeInUSD = (feeAmount / 1e18) * priceInUSD.eth;
      break;
    case 'solana':
      feeInUSD = (feeAmount / 1e9) * priceInUSD.sol;
      break;
  }
  
  return feeInUSD <= maxFeeInUSD;
}
```

### Python

```python
import requests

def get_estimated_fees():
    """Fetch current fee estimates from Unit API"""
    response = requests.get('https://api.hyperunit.xyz/v2/estimate-fees')
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch fees: {response.status_code}")

def format_fees(fees):
    """Format fees for display"""
    # Bitcoin
    btc_deposit = fees['bitcoin']['depositFee'] / 1e8
    btc_withdraw = fees['bitcoin']['withdrawalFee'] / 1e8
    
    # Ethereum
    eth_deposit = fees['ethereum']['depositFee'] / 1e18
    eth_withdraw = fees['ethereum']['withdrawalFee'] / 1e18
    
    # Solana
    sol_deposit = fees['solana']['depositFee'] / 1e9
    sol_withdraw = fees['solana']['withdrawalFee'] / 1e9
    
    return {
        'bitcoin': {
            'deposit': f"{btc_deposit:.8f} BTC ({fees['bitcoin']['depositEta']})",
            'withdraw': f"{btc_withdraw:.8f} BTC ({fees['bitcoin']['withdrawalEta']})"
        },
        'ethereum': {
            'deposit': f"{eth_deposit:.6f} ETH ({fees['ethereum']['depositEta']})",
            'withdraw': f"{eth_withdraw:.6f} ETH ({fees['ethereum']['withdrawalEta']})"
        },
        'solana': {
            'deposit': f"{sol_deposit:.6f} SOL ({fees['solana']['depositEta']})",
            'withdraw': f"{sol_withdraw:.6f} SOL ({fees['solana']['withdrawalEta']})"
        }
    }

# Example usage
fees = get_estimated_fees()
formatted = format_fees(fees)
print(formatted)
```

## Fee Optimization Strategies

### 1. Time-Based Optimization
Monitor fee trends and execute transactions during low-congestion periods:

```javascript
async function waitForLowerFees(network, maxFee) {
  while (true) {
    const fees = await getEstimatedFees();
    if (fees[network].depositFee <= maxFee) {
      return fees[network];
    }
    // Wait 60 seconds before checking again
    await new Promise(resolve => setTimeout(resolve, 60000));
  }
}
```

### 2. Batch Operations
Combine multiple operations when fees are favorable to optimize costs.

### 3. Network Selection
Choose the most cost-effective network for your needs:

```javascript
function getCheapestNetwork(fees, amount) {
  const networks = ['bitcoin', 'ethereum', 'solana'];
  let cheapest = null;
  let lowestFee = Infinity;
  
  for (const network of networks) {
    const fee = fees[network].depositFee;
    if (fee < lowestFee) {
      lowestFee = fee;
      cheapest = network;
    }
  }
  
  return cheapest;
}
```

## Important Considerations

### Fee Volatility
- Fees can change rapidly based on network congestion
- Always fetch current fees before initiating transactions
- Consider implementing fee caps to protect against spikes

### Processing Times
- ETAs are estimates based on current network conditions
- Actual confirmation times may vary
- Priority fees can reduce processing times

### Minimum Amounts
Remember that deposits have minimum amounts regardless of fees:
- BTC: 0.002 BTC
- ETH: 0.05 ETH
- SOL: 0.1 SOL

## Error Handling

### Common Response Codes

| Code | Description | Action |
|------|-------------|--------|
| 200 | Success | Process fee data |
| 429 | Rate limited | Implement backoff |
| 500 | Server error | Retry with exponential backoff |
| 503 | Service unavailable | Check status page |

### Example Error Handling

```javascript
async function getFeesWithRetry(maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      const response = await axios.get('https://api.hyperunit.xyz/v2/estimate-fees');
      return response.data;
    } catch (error) {
      if (error.response?.status === 429) {
        // Rate limited - wait longer
        await new Promise(resolve => setTimeout(resolve, 5000 * (i + 1)));
      } else if (i === maxRetries - 1) {
        throw error;
      } else {
        // Exponential backoff for other errors
        await new Promise(resolve => setTimeout(resolve, 1000 * Math.pow(2, i)));
      }
    }
  }
}
```

## Related Resources

- [Generate Address](/developers/api/generate-address)
- [Deposit Lifecycle](/developers/api/operations/deposit-lifecycle)
- [Withdrawal Lifecycle](/developers/api/operations/withdrawal-lifecycle)
- [API Overview](/developers/api)

## Support

For assistance with fee estimation:
- API Documentation: https://docs.hyperunit.xyz
- Developer Support: developers@hyperunit.xyz
- Status Page: https://status.hyperunit.xyz