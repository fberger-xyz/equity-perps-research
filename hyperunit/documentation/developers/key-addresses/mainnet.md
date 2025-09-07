# Unit Mainnet Key Addresses

## Treasury Addresses

Unit Protocol maintains treasury addresses on each supported blockchain for managing protocol assets and operations.

### Bitcoin
| Type | Address |
|------|---------|
| Native Chain Treasury | `bc1pdwu79dady576y3fupmm82m3g7p2p9f6hgyeqy0tdg7ztxg7xrayqlkl8j9` |
| HyperCore Treasury | `0x574bAFCe69d9411f662a433896e74e4F153096FA` |

### Ethereum
| Type | Address |
|------|---------|
| Native Chain Treasury | `0xBEa9f7FD27f4EE20066F18DEF0bc586eC221055A` |
| HyperCore Treasury | `0x8DAfBe89302656a7Df43c470e9EbCB4c540835c0` |

### Solana
| Type | Address |
|------|---------|
| Native Chain Treasury | `9SLPTL41SPsYkgdsMzdfJsxymEANKr5bYoBsQzJyKpKS` |
| HyperCore Treasury | `0xA822a9cEB6D6CB5b565bD10098AbCFA9Cf18D748` |

## Guardian Information

Guardians are essential participants in the Unit Protocol, helping generate protocol addresses through consensus. Their public keys enable verification of address integrity and protocol operations.

### Guardian Public Keys

#### Unit Node
```
Guardian ID: unit-node
Public Key: 04dc6f89f921dc816aa69b687be1fcc3cc1d48912629abc2c9964e807422e1047e0435cb5ba0fa53cb9a57a9c610b4e872a0a2caedda78c4f85ebafcca93524061
```

#### Hyperliquid Node
```
Guardian ID: hl-node
Public Key: 048633ea6ab7e40cdacf37d1340057e84bb9810de0687af78d031e9b07b65ad4ab379180ab55075f5c2ebb96dab30d2c2fab49d5635845327b6a3c27d20ba4755b
```

#### Field Node
```
Guardian ID: field-node
Public Key: 04ae2ab20787f816ea5d13f36c4c4f7c9e4e88bef2af6bbbb3e088faf088d0cec7c7dd28a5e14b7a4e2dfa1cf31e5a5e951e82f37fcea2c1fa8bc3c0fccd1e2ee8
```

## Address Verification

### How to Verify Treasury Addresses

1. **Blockchain Explorer Verification**
   - Bitcoin: Check on [mempool.space](https://mempool.space)
   - Ethereum: Verify on [Etherscan](https://etherscan.io)
   - Solana: Confirm on [Solscan](https://solscan.io)

2. **Guardian Signature Verification**
   - Use Guardian public keys to verify signatures
   - Ensure at least 2-of-3 Guardian consensus
   - See [Guardian Signatures](/developers/api/generate-address/guardian-signatures) for implementation

3. **Cross-Reference Sources**
   - Official documentation
   - Protocol smart contracts
   - Community announcements

## Smart Contract Addresses

### Token Contracts
For token-specific contract addresses, see [Token Metadata](/developers/key-addresses/mainnet/token-metadata)

### Protocol Contracts
Protocol-specific contracts are deployed on Hyperliquid L1:
- Bridge Contract: `[To be updated]`
- Registry Contract: `[To be updated]`
- Guardian Manager: `[To be updated]`

## Integration Guidelines

### For Developers

1. **Address Format Validation**
   ```javascript
   // Bitcoin address validation
   function isValidBitcoinAddress(address) {
     // Native SegWit (Bech32) format
     return /^bc1[a-z0-9]{39,87}$/.test(address);
   }
   
   // Ethereum address validation
   function isValidEthereumAddress(address) {
     return /^0x[a-fA-F0-9]{40}$/.test(address);
   }
   
   // Solana address validation
   function isValidSolanaAddress(address) {
     return /^[1-9A-HJ-NP-Za-km-z]{32,44}$/.test(address);
   }
   ```

2. **Treasury Monitoring**
   ```javascript
   // Monitor treasury balance
   async function getTreasuryBalance(chain, address) {
     // Implementation depends on chain
     switch(chain) {
       case 'bitcoin':
         return await getBitcoinBalance(address);
       case 'ethereum':
         return await getEthereumBalance(address);
       case 'solana':
         return await getSolanaBalance(address);
     }
   }
   ```

## Security Notices

### Important Warnings
- **Never send funds directly to treasury addresses** unless explicitly instructed
- **Always verify addresses** before any transaction
- **Use testnet first** for integration testing
- **Monitor official channels** for address updates

### Reporting Issues
If you discover any discrepancies or security concerns:
1. Do not publicly disclose the issue
2. Contact security@hyperunit.xyz immediately
3. Provide detailed information about the discovery

## Change Management

### Address Updates
Treasury addresses may change due to:
- Security upgrades
- Protocol improvements
- Guardian rotations
- Multi-sig updates

### Notification Process
Updates will be announced through:
- Official documentation updates
- Developer mailing list
- Discord announcements
- Twitter/X updates

## Monitoring Tools

### Recommended Services
- **DeBank**: Portfolio tracking across chains
- **Zerion**: Multi-chain wallet monitoring
- **Nansen**: On-chain analytics
- **Dune Analytics**: Custom dashboards

### API Endpoints
```javascript
// Get current treasury addresses
GET https://api.hyperunit.xyz/treasuries/mainnet

// Verify address ownership
POST https://api.hyperunit.xyz/verify-address
{
  "address": "0x...",
  "chain": "ethereum"
}
```

## Related Resources

- [Testnet Addresses](/developers/key-addresses/testnet)
- [Token Metadata](/developers/key-addresses/mainnet/token-metadata)
- [Guardian Signatures](/developers/api/generate-address/guardian-signatures)
- [API Documentation](/developers/api)

## Support

For questions about mainnet addresses:
- Technical Support: developers@hyperunit.xyz
- Security Concerns: security@hyperunit.xyz
- General Inquiries: info@hyperunit.xyz