# Unit Mainnet Token Metadata

## Overview

This document provides comprehensive metadata for all Unit-supported tokens on mainnet, including their native chain origins, Hyperliquid L1 representations, and associated contract addresses.

## HyperCore Tokens

Unit Protocol enables bridging of major cryptocurrencies and select tokens to Hyperliquid. Each bridged asset is represented as a Unit token (prefixed with 'U') on the Hyperliquid L1.

### Supported Tokens

| Token | L1 Symbol | Full Name | Native Chain | Hyperliquid Token ID |
|-------|-----------|-----------|--------------|---------------------|
| **BTC** | UBTC | Unit Bitcoin | Bitcoin | [`0x8f254b963e8468305d409b33aa137c67`](https://app.hyperliquid.xyz/explorer/token/0x8f254b963e8468305d409b33aa137c67) |
| **ETH** | UETH | Unit Ethereum | Ethereum Mainnet | [`0xe1edd30daaf5caac3fe63569e24748da`](https://app.hyperliquid.xyz/explorer/token/0xe1edd30daaf5caac3fe63569e24748da) |
| **SOL** | USOL | Unit Solana | Solana Mainnet | [`0x49b67c39f5566535de22b29b0e51e685`](https://app.hyperliquid.xyz/explorer/token/0x49b67c39f5566535de22b29b0e51e685) |
| **PUMP** | UPUMP | Unit Pump Fun | Solana Mainnet | [`0x544e60f98a36d7b22c0fb5824b84f795`](https://app.hyperliquid.xyz/explorer/token/0x544e60f98a36d7b22c0fb5824b84f795) |
| **FARTCOIN** | UFART | Unit Fartcoin | Solana Mainnet | [`0x7650808198966e4285687d3deb556ccc`](https://app.hyperliquid.xyz/explorer/token/0x7650808198966e4285687d3deb556ccc) |
| **SPX** | USPX | Unit SPX6900 | Solana Mainnet | [`0x2ff71b802a6788a052c7f1a58ec863af`](https://app.hyperliquid.xyz/explorer/token/0x2ff71b802a6788a052c7f1a58ec863af) |

## Token Details

### Bitcoin (BTC → UBTC)

**Native Chain**: Bitcoin Mainnet
**Unit Token**: UBTC (Unit Bitcoin)
**Decimals**: 8
**Minimum Deposit**: 0.002 BTC
**Contract Type**: Native BTC (no smart contract)

**Integration**:
```javascript
const UBTC_TOKEN_ID = "0x8f254b963e8468305d409b33aa137c67";
const UBTC_DECIMALS = 8;
const MIN_DEPOSIT_BTC = 0.002;
```

### Ethereum (ETH → UETH)

**Native Chain**: Ethereum Mainnet
**Unit Token**: UETH (Unit Ethereum)
**Decimals**: 18
**Minimum Deposit**: 0.05 ETH
**Contract Type**: Native ETH

**Integration**:
```javascript
const UETH_TOKEN_ID = "0xe1edd30daaf5caac3fe63569e24748da";
const UETH_DECIMALS = 18;
const MIN_DEPOSIT_ETH = 0.05;
```

### Solana (SOL → USOL)

**Native Chain**: Solana Mainnet Beta
**Unit Token**: USOL (Unit Solana)
**Decimals**: 9
**Minimum Deposit**: 0.1 SOL
**Contract Type**: Native SOL

**Integration**:
```javascript
const USOL_TOKEN_ID = "0x49b67c39f5566535de22b29b0e51e685";
const USOL_DECIMALS = 9;
const MIN_DEPOSIT_SOL = 0.1;
```

### SPL Tokens

#### Pump Fun (PUMP → UPUMP)

**Native Chain**: Solana Mainnet Beta
**Native Contract**: `[SPL Token Address]`
**Unit Token**: UPUMP (Unit Pump Fun)
**Decimals**: 6
**Hyperliquid Token ID**: `0x544e60f98a36d7b22c0fb5824b84f795`

#### Fartcoin (FARTCOIN → UFART)

**Native Chain**: Solana Mainnet Beta
**Native Contract**: `[SPL Token Address]`
**Unit Token**: UFART (Unit Fartcoin)
**Decimals**: 6
**Hyperliquid Token ID**: `0x7650808198966e4285687d3deb556ccc`

#### SPX6900 (SPX → USPX)

**Native Chain**: Solana Mainnet Beta
**Native Contract**: `[SPL Token Address]`
**Unit Token**: USPX (Unit SPX6900)
**Decimals**: 6
**Hyperliquid Token ID**: `0x2ff71b802a6788a052c7f1a58ec863af`

## Token Verification

### How to Verify Token Authenticity

1. **Check Hyperliquid Explorer**
   - Visit the token page using the provided explorer links
   - Verify token name and symbol match
   - Check total supply and holders

2. **Verify Native Chain Contract** (for SPL tokens)
   - Confirm contract address on Solscan
   - Check token metadata on-chain
   - Verify creator and authority

3. **Cross-Reference with API**
   ```javascript
   // Verify token metadata via API
   const response = await fetch('https://api.hyperunit.xyz/tokens/mainnet');
   const tokens = await response.json();
   
   // Validate token exists and matches metadata
   const token = tokens.find(t => t.symbol === 'UBTC');
   console.assert(token.tokenId === '0x8f254b963e8468305d409b33aa137c67');
   ```

## Integration Examples

### Fetching Token Balances

```javascript
async function getUnitTokenBalance(userAddress, tokenSymbol) {
  const tokenMap = {
    'UBTC': '0x8f254b963e8468305d409b33aa137c67',
    'UETH': '0xe1edd30daaf5caac3fe63569e24748da',
    'USOL': '0x49b67c39f5566535de22b29b0e51e685',
    'UPUMP': '0x544e60f98a36d7b22c0fb5824b84f795',
    'UFART': '0x7650808198966e4285687d3deb556ccc',
    'USPX': '0x2ff71b802a6788a052c7f1a58ec863af'
  };
  
  const tokenId = tokenMap[tokenSymbol];
  if (!tokenId) throw new Error(`Unknown token: ${tokenSymbol}`);
  
  // Query Hyperliquid for balance
  const balance = await queryHyperliquidBalance(userAddress, tokenId);
  return balance;
}
```

### Token Price Feeds

```javascript
async function getTokenPrice(tokenSymbol) {
  // Map Unit tokens to price identifiers
  const priceMap = {
    'UBTC': 'bitcoin',
    'UETH': 'ethereum',
    'USOL': 'solana',
    // SPL tokens may require different price sources
  };
  
  // Fetch price from oracle or exchange
  const price = await fetchPrice(priceMap[tokenSymbol]);
  return price;
}
```

## Token Standards

### Naming Convention
- All Unit tokens use the prefix 'U' followed by the native token symbol
- Example: BTC → UBTC, ETH → UETH

### Decimal Handling
- Preserve native chain decimal precision
- BTC: 8 decimals
- ETH: 18 decimals
- SOL: 9 decimals
- SPL Tokens: Typically 6-9 decimals

### Minimum Amounts
Respect minimum deposit/withdrawal amounts:
```javascript
const MIN_AMOUNTS = {
  'UBTC': 0.002,
  'UETH': 0.05,
  'USOL': 0.1,
  // SPL tokens have dynamic minimums
};
```

## Future Tokens

> **Note**: Additional tokens may be added to the Unit Protocol. Always check the latest documentation for updates.

### Planned Additions
- Additional SPL tokens
- ERC-20 tokens
- Other L1 native assets

### Integration Preparation
Design your integration to handle dynamic token lists:
```javascript
async function refreshSupportedTokens() {
  const response = await fetch('https://api.hyperunit.xyz/tokens/mainnet');
  const tokens = await response.json();
  
  // Update local token registry
  tokens.forEach(token => {
    tokenRegistry.set(token.symbol, {
      tokenId: token.tokenId,
      decimals: token.decimals,
      minDeposit: token.minDeposit,
      nativeChain: token.nativeChain
    });
  });
}
```

## Monitoring and Analytics

### Token Metrics
Track key metrics for Unit tokens:
- Total Value Locked (TVL)
- Daily volume
- Number of holders
- Bridge activity

### Dashboard Resources
- Hyperliquid Explorer: Token-specific pages
- Dune Analytics: Custom dashboards
- DefiLlama: TVL tracking

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Token not appearing | Not yet indexed | Wait for confirmation |
| Incorrect balance | Decimal mismatch | Check decimal conversion |
| Transfer failed | Below minimum | Ensure amount > minimum |

## Related Resources

- [Testnet Token Metadata](/developers/key-addresses/testnet/token-metadata-testnet)
- [Generate Address API](/developers/api/generate-address)
- [Deposit Guide](/how-to/deposit)
- [Withdrawal Guide](/how-to/withdraw)

## Support

For token-related inquiries:
- Technical Support: developers@hyperunit.xyz
- Token Listings: listings@hyperunit.xyz
- General Support: support@hyperunit.xyz