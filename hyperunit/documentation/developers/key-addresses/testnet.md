# Unit Testnet Key Addresses

## Overview

The testnet environment provides a safe space for developers to test integrations with Unit Protocol before deploying to mainnet. All testnet operations use test tokens with no real value.

## Treasury Addresses

Unit Protocol maintains testnet treasury addresses for managing test assets and protocol operations.

### Bitcoin Signet
| Type | Address |
|------|---------|
| Native Chain Treasury | `tb1phrd66lrhm7rtjh5a6jzkcum8ru4yyxsssrzhpdgez52hasjngc5q58gffn` |
| HyperCore Treasury | `0x5B6Fce52630f5f11FC9b77DfA5cFa8970f944Ec2` |

### Ethereum Sepolia
| Type | Address |
|------|---------|
| Native Chain Treasury | `0x762420d851318c47F256E22AF95E861DB9A77b94` |
| HyperCore Treasury | `0xdC78799911e46bacA335e6c5BA50dA89e9885520` |

### Solana Devnet
| Type | Address |
|------|---------|
| Native Chain Treasury | `F2yH7AU1S3ef37m2MJ4RvEfjHNpum1KQwsjK74krtQAS` |
| HyperCore Treasury | `0x8ac07902383196B25a8A48eFEB5A59E317da789e` |

## Guardian Information

Testnet Guardians operate similarly to mainnet but with different keys and configurations for testing purposes.

### Guardian Public Keys

#### Unit Node (Testnet)
```
Guardian ID: unit-node
Public Key: 04bab844e8620c4a1ec304df6284cd6fdffcde79b3330a7bffb1e4cecfee72d02a7c1f3a4415b253dc8d6ca2146db170e1617605cc8a4160f539890b8a24712152
```

#### Hyperliquid Node (Testnet)
```
Guardian ID: hl-node-testnet
Public Key: 04502d20a0d8d8aaea9395eb46d50ad2d8278c1b3a3bcdc200d531253612be23f5f2e9709bf3a3a50d1447281fa81aca0bf2ac2a6a3cb8a12978381a088bc3e0e0
```

#### Field Node (Testnet)
```
Guardian ID: field-node-testnet
Public Key: [To be updated]
```

## Test Networks

### Supported Test Networks

| Network | Name | Faucet | Explorer |
|---------|------|--------|----------|
| Bitcoin | Signet | [Signet Faucet](https://signetfaucet.com) | [Mempool Signet](https://mempool.space/signet) |
| Ethereum | Sepolia | [Sepolia Faucet](https://sepoliafaucet.com) | [Sepolia Etherscan](https://sepolia.etherscan.io) |
| Solana | Devnet | `solana airdrop` CLI | [Solana Explorer](https://explorer.solana.com?cluster=devnet) |
| Hyperliquid | Testnet | [HL Testnet Faucet](https://faucet.hyperliquid-testnet.xyz) | [HL Testnet Explorer](https://app.hyperliquid-testnet.xyz/explorer) |

## Getting Test Tokens

### Bitcoin Signet
```bash
# Request from faucet
curl -X POST https://signetfaucet.com/claim \
  -d "address=tb1phrd66lrhm7rtjh5a6jzkcum8ru4yyxsssrzhpdgez52hasjngc5q58gffn"
```

### Ethereum Sepolia
```javascript
// Use web3.js or ethers.js
const faucetUrl = 'https://sepoliafaucet.com';
// Visit faucet website and enter your address
```

### Solana Devnet
```bash
# Using Solana CLI
solana airdrop 2 YOUR_ADDRESS --url devnet

# Or via curl
curl -X POST https://api.devnet.solana.com -H "Content-Type: application/json" -d '
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "requestAirdrop",
  "params": ["YOUR_ADDRESS", 1000000000]
}'
```

### Hyperliquid Testnet
Visit the [Hyperliquid Testnet Faucet](https://faucet.hyperliquid-testnet.xyz) and connect your wallet.

## API Endpoints

### Testnet API Base URL
```
https://api.hyperunit-testnet.xyz
```

### Testnet WebSocket
```
wss://api.hyperunit-testnet.xyz/ws
```

## Integration Testing Guide

### 1. Environment Setup

```javascript
// Configure for testnet
const config = {
  network: 'testnet',
  apiUrl: 'https://api.hyperunit-testnet.xyz',
  wsUrl: 'wss://api.hyperunit-testnet.xyz/ws',
  guardianNodes: {
    'unit-node': '04bab844e8620c4a1ec304df6284cd6fdffcde79b3330a7bffb1e4cecfee72d02a7c1f3a4415b253dc8d6ca2146db170e1617605cc8a4160f539890b8a24712152',
    'hl-node-testnet': '04502d20a0d8d8aaea9395eb46d50ad2d8278c1b3a3bcdc200d531253612be23f5f2e9709bf3a3a50d1447281fa81aca0bf2ac2a6a3cb8a12978381a088bc3e0e0'
  }
};
```

### 2. Generate Test Deposit Address

```javascript
async function generateTestDepositAddress(destinationAddress) {
  const response = await fetch(
    `https://api.hyperunit-testnet.xyz/gen/bitcoin/hyperliquid/btc/${destinationAddress}`
  );
  
  const data = await response.json();
  console.log('Test deposit address:', data.address);
  
  // Verify signatures with testnet Guardian keys
  const isValid = await verifyTestnetSignatures(data.signatures);
  console.log('Signature valid:', isValid);
  
  return data.address;
}
```

### 3. Monitor Test Transactions

```javascript
class TestnetMonitor {
  constructor() {
    this.ws = new WebSocket('wss://api.hyperunit-testnet.xyz/ws');
  }
  
  watchDeposit(txHash) {
    this.ws.send(JSON.stringify({
      action: 'subscribe',
      topic: 'deposit',
      txHash: txHash,
      network: 'testnet'
    }));
  }
  
  watchWithdrawal(withdrawalId) {
    this.ws.send(JSON.stringify({
      action: 'subscribe',
      topic: 'withdrawal',
      withdrawalId: withdrawalId,
      network: 'testnet'
    }));
  }
}
```

## Testing Checklist

### Pre-Deployment Testing

- [ ] **Address Generation**
  - Generate deposit addresses for all supported chains
  - Verify Guardian signatures
  - Test address persistence

- [ ] **Deposits**
  - Test minimum deposit amounts
  - Verify confirmation requirements
  - Monitor deposit lifecycle

- [ ] **Withdrawals**
  - Test withdrawal queue
  - Verify processing times
  - Check fee calculations

- [ ] **Error Handling**
  - Test with invalid addresses
  - Handle network timeouts
  - Verify error messages

- [ ] **Integration**
  - Test API authentication
  - Verify WebSocket connections
  - Check rate limiting

## Differences from Mainnet

### Key Differences

| Aspect | Testnet | Mainnet |
|--------|---------|---------|
| Token Value | No real value | Real value |
| Confirmation Times | May be faster | Standard times |
| Network Stability | May have resets | Stable |
| Guardian Set | Test guardians | Production guardians |
| Rate Limits | More lenient | Strict limits |

### Testnet Limitations

1. **Periodic Resets**: Testnet may be reset periodically
2. **Limited Liquidity**: Test tokens have limited availability
3. **Network Instability**: Test networks may experience downtime
4. **Feature Differences**: Some features may be experimental

## Troubleshooting

### Common Testnet Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Faucet not working | Rate limited | Wait or try different faucet |
| Transaction stuck | Low fees | Increase fee or wait |
| Address not found | Wrong network | Verify testnet configuration |
| Signature verification fails | Wrong Guardian keys | Use testnet Guardian keys |

### Debug Mode

Enable debug logging for testnet:

```javascript
// Enable verbose logging
const debug = true;

async function testnetRequest(endpoint, options = {}) {
  if (debug) {
    console.log(`[TESTNET] Request to ${endpoint}`, options);
  }
  
  const response = await fetch(
    `https://api.hyperunit-testnet.xyz${endpoint}`,
    options
  );
  
  if (debug) {
    console.log(`[TESTNET] Response:`, response.status);
  }
  
  return response;
}
```

## Migration to Mainnet

### Checklist for Mainnet Migration

1. **Update Configuration**
   ```javascript
   // Change from testnet to mainnet
   const config = {
     network: 'mainnet',
     apiUrl: 'https://api.hyperunit.xyz',
     // Update Guardian keys
     // Update treasury addresses
   };
   ```

2. **Security Review**
   - Audit error handling
   - Review key management
   - Test failover scenarios

3. **Performance Testing**
   - Load test your integration
   - Verify timeout handling
   - Check retry logic

4. **Documentation**
   - Update API endpoints
   - Document configuration changes
   - Review security practices

## Support Resources

### Testnet Support

- **Discord**: Join #testnet-support channel
- **Documentation**: https://docs.hyperunit.xyz
- **Status Page**: https://status.hyperunit-testnet.xyz
- **Email**: testnet@hyperunit.xyz

### Testnet Tools

- **Transaction Monitor**: https://testnet.hyperunit.xyz/monitor
- **Address Validator**: https://testnet.hyperunit.xyz/validate
- **Fee Calculator**: https://testnet.hyperunit.xyz/fees

## Related Resources

- [Mainnet Addresses](/developers/key-addresses/mainnet)
- [Testnet Token Metadata](/developers/key-addresses/testnet/token-metadata-testnet)
- [API Documentation](/developers/api)
- [Integration Guide](/developers/api/generate-address)

## Notes

> **Important**: Testnet configurations and addresses are subject to change. Always refer to the latest documentation before testing.