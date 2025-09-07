# Unit Protocol API Documentation

## Overview

The Unit Protocol provides comprehensive public APIs for developers to interact directly with the protocol. These APIs enable programmatic access to all protocol functionality including address generation, fee estimation, and transaction lifecycle management.

## API Endpoints

### Production
- **Base URL**: `https://api.hyperunit.xyz`
- **Status**: Live and operational
- **Supported Assets**: BTC, ETH, SOL

### Testnet
- **Base URL**: `https://api.hyperunit-testnet.xyz`
- **Status**: Available for testing
- **Test Assets**: Test BTC, ETH, SOL tokens

## Required Confirmations

The protocol requires blockchain-specific confirmation times to ensure transaction finality:

| Chain       | Confirmations | Approximate Time | Notes |
|-------------|---------------|------------------|-------|
| Bitcoin     | 2             | ~20 minutes      | May vary based on network congestion |
| Hyperliquid | 2000          | ~3.5 minutes     | Fast finality on L1 |
| Ethereum    | 14            | ~3 minutes       | Based on average block time |
| Solana      | 32            | ~13 seconds      | Near-instant finality |

## Core API Features

### 1. Address Generation
Generate unique deposit addresses for users:
- Deterministic address derivation
- Guardian signature verification
- Support for all asset types
- [Learn more →](/developers/api/generate-address)

### 2. Fee Estimation
Calculate transaction fees before operations:
- Real-time fee updates
- Network congestion consideration
- Optimal fee recommendations
- [Learn more →](/developers/api/estimate-fees)

### 3. Operation Management
Track deposit and withdrawal lifecycles:
- Real-time status updates
- Transaction monitoring
- Error handling and recovery
- [Learn more →](/developers/api/operations)

### 4. Queue Management
Monitor and manage withdrawal queues:
- Queue position tracking
- Estimated processing times
- Priority management
- [Learn more →](/developers/api/withdraw-queue)

## Authentication

### API Key Management
```http
Authorization: Bearer YOUR_API_KEY
```

- API keys are issued per application
- Rate limits apply based on tier
- Keys can be managed via dashboard

### Request Signing
For sensitive operations, requests must be signed:
```javascript
const signature = sign(payload, privateKey);
headers['X-Signature'] = signature;
```

## Rate Limits

| Tier | Requests/Second | Requests/Day | Use Case |
|------|-----------------|--------------|----------|
| Free | 10 | 10,000 | Development |
| Basic | 100 | 100,000 | Small applications |
| Pro | 1,000 | 1,000,000 | Production apps |
| Enterprise | Custom | Custom | High-volume |

## Response Format

### Success Response
```json
{
  "success": true,
  "data": {
    // Response data
  },
  "timestamp": "2024-01-01T00:00:00Z"
}
```

### Error Response
```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": {}
  },
  "timestamp": "2024-01-01T00:00:00Z"
}
```

## Common Error Codes

| Code | Description | Resolution |
|------|-------------|------------|
| `RATE_LIMIT_EXCEEDED` | Too many requests | Implement backoff strategy |
| `INVALID_ADDRESS` | Invalid blockchain address | Validate address format |
| `INSUFFICIENT_BALANCE` | Not enough funds | Check balance before operation |
| `GUARDIAN_CONSENSUS_FAILED` | Guardian agreement not reached | Retry after delay |
| `NETWORK_CONGESTION` | Blockchain network busy | Wait or increase fees |

## WebSocket Support

Real-time updates via WebSocket connections:

```javascript
const ws = new WebSocket('wss://api.hyperunit.xyz/ws');

ws.on('message', (data) => {
  const update = JSON.parse(data);
  // Handle real-time updates
});
```

### Subscription Topics
- `deposits`: Monitor incoming deposits
- `withdrawals`: Track withdrawal status
- `addresses`: Address generation events
- `fees`: Real-time fee updates

## SDK Libraries

Official SDKs for popular languages:

### JavaScript/TypeScript
```bash
npm install @hyperunit/sdk
```

### Python
```bash
pip install hyperunit-sdk
```

### Go
```bash
go get github.com/hyperunit/go-sdk
```

## Integration Examples

### Generate Deposit Address
```javascript
const { Unit } = require('@hyperunit/sdk');
const unit = new Unit({ apiKey: 'YOUR_API_KEY' });

const address = await unit.generateAddress({
  asset: 'BTC',
  hyperliquidAddress: '0x...'
});
```

### Monitor Deposit
```javascript
const deposit = await unit.trackDeposit({
  txHash: '...',
  asset: 'BTC'
});

console.log(deposit.status); // 'pending' | 'confirmed' | 'completed'
```

## Best Practices

### Security
1. Never expose API keys in client-side code
2. Implement request signing for sensitive operations
3. Use HTTPS for all API calls
4. Validate all responses

### Performance
1. Implement caching where appropriate
2. Use WebSocket for real-time updates
3. Batch requests when possible
4. Handle rate limits gracefully

### Error Handling
1. Implement exponential backoff for retries
2. Log all errors for debugging
3. Provide user-friendly error messages
4. Monitor API health endpoints

## API Sections

Explore detailed documentation for each API section:

- [Generate Address](/developers/api/generate-address) - Create deposit addresses
- [Estimate Fees](/developers/api/estimate-fees) - Calculate transaction costs
- [Operations](/developers/api/operations) - Manage deposits and withdrawals
- [Withdraw Queue](/developers/api/withdraw-queue) - Monitor withdrawal processing

## Support Resources

- **Documentation**: https://docs.hyperunit.xyz
- **API Status**: https://status.hyperunit.xyz
- **Developer Discord**: https://discord.gg/hyperunit
- **Email Support**: developers@hyperunit.xyz

## Changelog

Stay updated with API changes:
- Subscribe to developer newsletter
- Follow [@hyperunit_dev](https://twitter.com/hyperunit_dev) on Twitter
- Check [changelog](https://docs.hyperunit.xyz/changelog) regularly