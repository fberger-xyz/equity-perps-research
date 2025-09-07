# Key Addresses

## Overview

The Key Addresses section provides comprehensive documentation for developers looking to understand and integrate with Unit's blockchain infrastructure across different networks and environments.

## Environments

Unit operates on two primary environments, each with its own set of addresses and configurations:

### 1. [Mainnet](/developers/key-addresses/mainnet)
Production environment for live operations:
- Real asset transfers
- Production Guardian nodes
- Live treasury addresses
- Official token deployments

### 2. [Testnet](/developers/key-addresses/testnet)
Testing environment for development:
- Test asset transfers
- Testnet Guardian nodes
- Test treasury addresses
- Experimental token deployments

## Contents

Each environment documentation includes:

### Treasury Addresses
- Native chain treasury addresses for each supported blockchain
- HyperCore treasury addresses for cross-chain operations
- Protocol-controlled addresses for asset management

### Guardian Information
- Public keys for address verification
- Guardian node identifiers
- Signature verification data

### Token Metadata
- Token contract addresses
- Token symbols and names
- Native chain mappings
- Token specifications

## Quick Reference

### Supported Chains
- **Bitcoin**: Native BTC transfers
- **Ethereum**: ETH and ERC-20 tokens
- **Solana**: SOL and SPL tokens
- **Hyperliquid**: L1 native assets

### Integration Points
Developers can use these addresses for:
- Verifying protocol transactions
- Monitoring treasury operations
- Validating Guardian signatures
- Integrating token contracts

## Navigation

- **Mainnet Resources**
  - [Mainnet Addresses](/developers/key-addresses/mainnet)
  - [Mainnet Token Metadata](/developers/key-addresses/mainnet/token-metadata)

- **Testnet Resources**
  - [Testnet Addresses](/developers/key-addresses/testnet)
  - [Testnet Token Metadata](/developers/key-addresses/testnet/token-metadata-testnet)

## Security Considerations

### Address Verification
Always verify addresses through multiple sources:
1. Check Guardian signatures
2. Confirm with official documentation
3. Validate on blockchain explorers

### Guardian Verification
Use Guardian public keys to verify:
- Generated deposit addresses
- Protocol transactions
- Treasury operations

## Best Practices

### For Integration
1. Always use addresses from official documentation
2. Implement address validation in your code
3. Monitor for address updates or changes
4. Test thoroughly on testnet before mainnet

### For Security
1. Never trust addresses from unofficial sources
2. Verify Guardian signatures for critical operations
3. Cross-reference addresses with blockchain explorers
4. Implement checksums and validation

## Updates and Changes

Address information may be updated due to:
- Protocol upgrades
- Security enhancements
- New chain integrations
- Guardian rotations

Stay informed:
- Subscribe to developer updates
- Monitor the changelog
- Follow official announcements

## Support

For assistance with key addresses:
- Technical Documentation: https://docs.hyperunit.xyz
- Developer Support: developers@hyperunit.xyz
- Security Concerns: security@hyperunit.xyz

## Related Resources

- [API Documentation](/developers/api)
- [Guardian Signatures](/developers/api/generate-address/guardian-signatures)
- [Architecture Overview](/architecture/quickstart)
- [Security](/architecture/security)