# Hyperunit Documentation

Welcome to the complete Hyperunit (Unit Protocol) documentation. This repository contains all documentation scraped and indexed from https://docs.hyperunit.xyz/.

## 📚 Documentation Structure

### Getting Started
- **[About Unit](./index.md)** - Introduction to Unit Protocol and its capabilities
- **[FAQ](./faq.md)** - Frequently asked questions and quick answers

### Unit Organization
- **[Team](./unit/about-unit/team.md)** - Meet the team behind Unit Protocol

### How-To Guides
- **[How to Deposit](./how-to/deposit.md)** - Step-by-step guide for depositing assets
- **[How to Withdraw](./how-to/withdraw.md)** - Complete withdrawal instructions

### Architecture
- **[Overview/Quickstart](./architecture/quickstart.md)** - High-level architecture overview
- **[Components](./architecture/components.md)** - Detailed component descriptions
- **[Security](./architecture/security.md)** - Security architecture and measures

### Developer Resources

#### API Documentation
- **[API Overview](./developers/api/index.md)** - Complete API reference
- **[Generate Address](./developers/api/generate-address.md)** - Address generation endpoints
  - **[Guardian Signatures](./developers/api/generate-address/guardian-signatures.md)** - Signature verification
- **[Estimate Fees](./developers/api/estimate-fees.md)** - Fee calculation API
- **Operations**
  - **[Deposit Lifecycle](./developers/api/operations/deposit-lifecycle.md)** - Deposit process stages
  - **[Withdrawal Lifecycle](./developers/api/operations/withdrawal-lifecycle.md)** - Withdrawal process stages
- **[Withdraw Queue](./developers/api/withdraw-queue.md)** - Queue management API

#### Key Addresses
- **[Overview](./developers/key-addresses/index.md)** - Address documentation overview
- **Mainnet**
  - **[Mainnet Addresses](./developers/key-addresses/mainnet.md)** - Production addresses
  - **[Token Metadata](./developers/key-addresses/mainnet/token-metadata.md)** - Mainnet token details
- **Testnet**
  - **[Testnet Addresses](./developers/key-addresses/testnet.md)** - Test environment addresses
  - **[Token Metadata](./developers/key-addresses/testnet/token-metadata-testnet.md)** - Testnet token details

### Legal Documentation
- **[Regulatory Compliance](./legal/regulatory-compliance.md)** - Compliance measures and policies
- **[Terms of Service](./legal/terms-of-service.md)** - Service terms and conditions
- **[Privacy Policy](./legal/privacy-policy.md)** - Data handling and privacy

## 🚀 Quick Links

### Essential Resources
- **Website**: https://hyperunit.xyz
- **App**: https://app.hyperunit.xyz
- **API (Production)**: https://api.hyperunit.xyz
- **API (Testnet)**: https://api.hyperunit-testnet.xyz
- **Hyperliquid**: https://app.hyperliquid.xyz

### For Developers
- [API Documentation](./developers/api/index.md)
- [Generate Deposit Address](./developers/api/generate-address.md)
- [Guardian Signatures Verification](./developers/api/generate-address/guardian-signatures.md)
- [Mainnet Integration](./developers/key-addresses/mainnet.md)
- [Testnet Integration](./developers/key-addresses/testnet.md)

### For Users
- [How to Deposit](./how-to/deposit.md)
- [How to Withdraw](./how-to/withdraw.md)
- [FAQ](./faq.md)
- [Security Information](./architecture/security.md)

## 📖 Documentation Overview

### What is Unit?

Unit is the asset tokenization layer on Hyperliquid, enabling seamless deposits and withdrawals for various crypto assets. It allows users to:

- Deposit BTC, ETH, or SOL from personal wallets directly to Hyperliquid
- Trade these assets on Hyperliquid's spot order book
- Withdraw assets to preferred addresses on their native blockchains

### Key Features

- **Multi-Chain Support**: Bitcoin, Ethereum, Solana, and Hyperliquid L1
- **Guardian Network**: Decentralized security through MPC threshold signatures
- **Unified Trading**: Spot and derivatives markets in one platform
- **Regulatory Compliance**: OFAC screening and geographic restrictions
- **Developer-Friendly**: Comprehensive APIs and documentation

### Supported Assets

#### Mainnet
- **UBTC** (Unit Bitcoin)
- **UETH** (Unit Ethereum)
- **USOL** (Unit Solana)
- **UPUMP** (Unit Pump Fun)
- **UFART** (Unit Fartcoin)
- **USPX** (Unit SPX6900)

#### Testnet
- Test versions of all supported assets
- Additional experimental tokens

## 🛠️ Technical Architecture

### Core Components
1. **Guardian Network** - Distributed consensus and security
2. **MPC Threshold Signatures** - 2-of-3 multi-party computation
3. **Chain Services** - Native blockchain integration
4. **Flow Manager** - State machine for operations
5. **Consensus Service** - Guardian agreement protocol

### Security Features
- End-to-end encryption
- Distributed key management
- Transaction verification
- Compliance screening
- Circuit breaker mechanisms

## 📱 Integration Guide

### Quick Start

1. **Generate Deposit Address**
```bash
curl -X GET https://api.hyperunit.xyz/gen/bitcoin/hyperliquid/btc/YOUR_HL_ADDRESS
```

2. **Estimate Fees**
```bash
curl -X GET https://api.hyperunit.xyz/v2/estimate-fees
```

3. **Check Withdrawal Queue**
```bash
curl -X GET https://api.hyperunit.xyz/withdrawal-queue
```

### Minimum Deposits
- **BTC**: 0.002 BTC
- **ETH**: 0.05 ETH
- **SOL**: 0.1 SOL

## 📞 Support & Contact

### Developer Support
- **Email**: developers@hyperunit.xyz
- **Discord**: Join the developer community
- **Documentation**: https://docs.hyperunit.xyz

### Security
- **Security Issues**: security@hyperunit.xyz
- **Bug Bounty**: https://hyperunit.xyz/bug-bounty

### Legal & Compliance
- **Legal Inquiries**: legal@hyperunit.xyz
- **Compliance**: compliance@hyperunit.xyz

## 📝 License & Legal

- [Terms of Service](./legal/terms-of-service.md)
- [Privacy Policy](./legal/privacy-policy.md)
- [Regulatory Compliance](./legal/regulatory-compliance.md)

## 🔄 Updates

This documentation was last indexed on: **September 2025**

For the most up-to-date information, always refer to:
- Official website: https://hyperunit.xyz
- Live documentation: https://docs.hyperunit.xyz

## 📊 Documentation Statistics

- **Total Pages**: 24
- **Sections**: 8 main sections
- **API Endpoints**: Multiple REST and WebSocket endpoints
- **Supported Chains**: 4 (Bitcoin, Ethereum, Solana, Hyperliquid)
- **Supported Assets**: 6+ tokens

---

> **Note**: This documentation is a snapshot of the Hyperunit documentation. For real-time updates and the latest information, please visit the official documentation at https://docs.hyperunit.xyz/