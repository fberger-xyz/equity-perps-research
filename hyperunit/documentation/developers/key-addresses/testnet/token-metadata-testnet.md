# Testnet Token Metadata for Unit

## Important Notice

> **Disclaimer**: Testnet deployments do not necessarily indicate future mainnet deployment. Tokens available on testnet are for testing purposes only and may not be available on mainnet.

## Overview

The testnet environment provides test versions of Unit Protocol tokens for development and integration testing. All testnet tokens have no real value and are solely for testing purposes.

## Testnet Tokens

### Supported Test Tokens

| Native Token | L1 Symbol | Full Name | Native Chain | Hyperliquid Testnet Token ID |
|--------------|-----------|-----------|--------------|------------------------------|
| **BTC** | UNIT | Test UNIT | Bitcoin Signet | [`0x5314ecc85ee6059955409e0da8d2bd31`](https://app.hyperliquid-testnet.xyz/explorer/token/0x5314ecc85ee6059955409e0da8d2bd31) |
| **ETH** | UETH | Unit Ethereum | Sepolia Testnet | [`0xe4371d8166f362d6578725f11e0a14f3`](https://app.hyperliquid-testnet.xyz/explorer/token/0xe4371d8166f362d6578725f11e0a14f3) |
| **SOL** | USOL | Unit Solana | Solana Devnet | [`0x57ead23624b114018cc0e49d01cc7b6b`](https://app.hyperliquid-testnet.xyz/explorer/token/0x57ead23624b114018cc0e49d01cc7b6b) |
| **PUMP** | UPUMP | Unit Pumpfun | Solana Devnet | [`0xdc348378290f167692e50bfb49c60696`](https://app.hyperliquid-testnet.xyz/explorer/token/0xdc348378290f167692e50bfb49c60696) |
| **FARTCOIN** | UFART | Unit Fartcoin | Solana Devnet | [`0x5c1a98b4df03401e19acb16bcf2ffabf`](https://app.hyperliquid-testnet.xyz/explorer/token/0x5c1a98b4df03401e19acb16bcf2ffabf) |
| **SPX** | USPXS | Unit SPX6900 | Solana Devnet | [`0x[token_id_pending]`](https://app.hyperliquid-testnet.xyz/explorer) |

## Token Configuration

### Test Bitcoin (BTC → UNIT)

**Network**: Bitcoin Signet
**Symbol**: UNIT (Note: Different from mainnet UBTC)
**Decimals**: 8
**Minimum Deposit**: 0.001 BTC (testnet)
**Faucet**: Available at signet faucets

```javascript
// Testnet BTC configuration
const TESTNET_BTC = {
  symbol: 'UNIT',
  tokenId: '0x5314ecc85ee6059955409e0da8d2bd31',
  decimals: 8,
  minDeposit: 0.001,
  network: 'signet'
};
```

### Test Ethereum (ETH → UETH)

**Network**: Sepolia Testnet
**Symbol**: UETH
**Decimals**: 18
**Minimum Deposit**: 0.01 ETH (testnet)
**Faucet**: Sepolia faucets

```javascript
// Testnet ETH configuration
const TESTNET_ETH = {
  symbol: 'UETH',
  tokenId: '0xe4371d8166f362d6578725f11e0a14f3',
  decimals: 18,
  minDeposit: 0.01,
  network: 'sepolia'
};
```

### Test Solana (SOL → USOL)

**Network**: Solana Devnet
**Symbol**: USOL
**Decimals**: 9
**Minimum Deposit**: 0.05 SOL (testnet)
**Faucet**: `solana airdrop` command

```javascript
// Testnet SOL configuration
const TESTNET_SOL = {
  symbol: 'USOL',
  tokenId: '0x57ead23624b114018cc0e49d01cc7b6b',
  decimals: 9,
  minDeposit: 0.05,
  network: 'devnet'
};
```

### Test SPL Tokens

#### Test Pump (PUMP → UPUMP)
**Network**: Solana Devnet
**Symbol**: UPUMP
**Decimals**: 6
**Token Contract**: `[Devnet SPL Address]`
**Hyperliquid Token ID**: `0xdc348378290f167692e50bfb49c60696`

#### Test Fartcoin (FARTCOIN → UFART)
**Network**: Solana Devnet
**Symbol**: UFART
**Decimals**: 6
**Token Contract**: `[Devnet SPL Address]`
**Hyperliquid Token ID**: `0x5c1a98b4df03401e19acb16bcf2ffabf`

## Obtaining Test Tokens

### 1. Native Test Tokens

```javascript
// Example: Get test ETH from Sepolia faucet
async function getTestETH(address) {
  // Visit https://sepoliafaucet.com
  // Or use API if available
  const response = await fetch('https://api.sepoliafaucet.com/claim', {
    method: 'POST',
    body: JSON.stringify({ address }),
    headers: { 'Content-Type': 'application/json' }
  });
  
  return response.json();
}
```

### 2. Bridge to Hyperliquid Testnet

```javascript
// Generate testnet deposit address
async function bridgeToTestnet(asset, amount, destinationAddress) {
  // Generate deposit address
  const depositAddr = await fetch(
    `https://api.hyperunit-testnet.xyz/gen/${asset}/hyperliquid/${asset}/${destinationAddress}`
  );
  
  const { address } = await depositAddr.json();
  
  // Send test tokens to generated address
  console.log(`Send ${amount} test ${asset} to: ${address}`);
  
  return address;
}
```

## Testing Token Operations

### Balance Queries

```javascript
// Query testnet token balance
async function getTestnetBalance(userAddress, tokenSymbol) {
  const testnetTokens = {
    'UNIT': '0x5314ecc85ee6059955409e0da8d2bd31',
    'UETH': '0xe4371d8166f362d6578725f11e0a14f3',
    'USOL': '0x57ead23624b114018cc0e49d01cc7b6b',
    'UPUMP': '0xdc348378290f167692e50bfb49c60696',
    'UFART': '0x5c1a98b4df03401e19acb16bcf2ffabf'
  };
  
  const tokenId = testnetTokens[tokenSymbol];
  
  // Query Hyperliquid testnet
  const response = await fetch(
    `https://api.hyperliquid-testnet.xyz/balance/${userAddress}/${tokenId}`
  );
  
  return response.json();
}
```

### Transfer Testing

```javascript
// Test token transfer on Hyperliquid testnet
async function testTransfer(fromAddress, toAddress, tokenSymbol, amount) {
  const tx = {
    from: fromAddress,
    to: toAddress,
    token: getTestnetTokenId(tokenSymbol),
    amount: amount,
    network: 'hyperliquid-testnet'
  };
  
  // Sign and broadcast transaction
  const result = await broadcastTestnetTx(tx);
  
  console.log(`Test transfer: ${result.txHash}`);
  return result;
}
```

## Integration Testing

### Test Scenarios

1. **Deposit Flow Testing**
```javascript
async function testDepositFlow() {
  // 1. Generate deposit address
  const depositAddr = await generateTestnetDepositAddress();
  
  // 2. Send test tokens
  await sendTestTokens(depositAddr, '0.01');
  
  // 3. Monitor deposit status
  const status = await monitorDeposit(depositAddr);
  
  // 4. Verify balance on Hyperliquid
  const balance = await getHyperliquidBalance();
  
  return { depositAddr, status, balance };
}
```

2. **Withdrawal Flow Testing**
```javascript
async function testWithdrawalFlow() {
  // 1. Initiate withdrawal
  const withdrawal = await initiateTestnetWithdrawal({
    asset: 'UETH',
    amount: '0.01',
    destination: '0x...'
  });
  
  // 2. Monitor withdrawal queue
  const queueStatus = await checkWithdrawalQueue();
  
  // 3. Verify completion
  const completed = await waitForWithdrawal(withdrawal.id);
  
  return { withdrawal, queueStatus, completed };
}
```

## Testnet Limitations

### Important Differences from Mainnet

| Feature | Testnet | Mainnet |
|---------|---------|---------|
| Token Symbol (BTC) | UNIT | UBTC |
| Minimum Deposits | Lower | Higher |
| Processing Speed | Variable | Consistent |
| Token Availability | Limited | Full |
| Network Resets | Possible | Never |

### Known Limitations

1. **Token Availability**: Some tokens may not always be available
2. **Faucet Limits**: Test token faucets have rate limits
3. **Network Instability**: Test networks may experience downtime
4. **Data Persistence**: Testnet data may be reset periodically

## Monitoring and Debugging

### Testnet Explorer

Monitor your test tokens:
- [Hyperliquid Testnet Explorer](https://app.hyperliquid-testnet.xyz/explorer)
- [Sepolia Etherscan](https://sepolia.etherscan.io)
- [Solana Devnet Explorer](https://explorer.solana.com?cluster=devnet)

### Debug Utilities

```javascript
// Enable testnet debug mode
const DEBUG = true;

function logTestnetOperation(operation, data) {
  if (DEBUG) {
    console.log(`[TESTNET] ${operation}:`, data);
    console.log(`Timestamp: ${new Date().toISOString()}`);
    console.log(`Network: ${data.network || 'hyperliquid-testnet'}`);
  }
}

// Usage
logTestnetOperation('DEPOSIT', {
  token: 'UETH',
  amount: '0.01',
  address: '0x...'
});
```

## Migration Considerations

### Preparing for Mainnet

When migrating from testnet to mainnet:

1. **Update Token IDs**
```javascript
// Testnet
const TESTNET_TOKENS = {
  'UNIT': '0x5314ecc85ee6059955409e0da8d2bd31',
  // ...
};

// Mainnet
const MAINNET_TOKENS = {
  'UBTC': '0x8f254b963e8468305d409b33aa137c67',
  // ...
};
```

2. **Adjust Minimum Amounts**
```javascript
// Increase minimum amounts for mainnet
const MIN_DEPOSITS = {
  testnet: { BTC: 0.001, ETH: 0.01, SOL: 0.05 },
  mainnet: { BTC: 0.002, ETH: 0.05, SOL: 0.1 }
};
```

3. **Update API Endpoints**
```javascript
const API_ENDPOINTS = {
  testnet: 'https://api.hyperunit-testnet.xyz',
  mainnet: 'https://api.hyperunit.xyz'
};
```

## Support and Resources

### Getting Help

- **Discord**: #testnet-tokens channel
- **Documentation**: https://docs.hyperunit.xyz
- **Email**: testnet-support@hyperunit.xyz

### Useful Links

- [Testnet Faucets List](https://docs.hyperunit.xyz/testnet/faucets)
- [API Documentation](/developers/api)
- [Mainnet Token Metadata](/developers/key-addresses/mainnet/token-metadata)
- [Testing Guide](/developers/testing-guide)

## Changelog

Track testnet token updates:
- Subscribe to testnet announcements
- Monitor [changelog](https://docs.hyperunit.xyz/changelog)
- Follow [@hyperunit_dev](https://twitter.com/hyperunit_dev)

---

> **Remember**: Testnet tokens have no value. Never send real assets to testnet addresses.