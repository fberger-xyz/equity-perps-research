# Unit Protocol Architecture Overview

## Core Components

### Guardian Network
The Guardian Network forms the backbone of Unit's security and operations:

- **Distributed Architecture**: A network of independent Guardians running the Unit protocol agent
- **Verification**: Guardians independently verify blockchain data for all supported assets
- **Consensus Mechanism**: Participate in consensus and Multi-Party Computation (MPC) Threshold Signature Scheme (TSS)
- **Security**: No single point of failure through distributed key management

### Infrastructure
Unit operates as a neutral infrastructure component within the Hyperliquid ecosystem, enabling:

- Direct deposits to Hyperliquid spot balance
- Asset withdrawals across major cryptocurrencies (BTC, ETH, SOL)
- Seamless integration with Hyperliquid's trading infrastructure

## Key Architecture Layers

### 1. Core Protocol Layer
The foundation of Unit's operations:

- **Decentralized Network**: Leader-verifier network architecture
- **Guardian Nodes**: Independent nodes running protocol implementation
- **Blockchain Integration**: Native blockchain node and indexer operations for supported assets
- **Consensus Protocol**: Byzantine fault-tolerant consensus mechanism

### 2. Application/UI Layer
User interaction points:

- **Web Interface**: Centralized interface at [app.hyperunit.xyz](https://app.hyperunit.xyz)
- **Optional Access**: Users can interact through multiple channels
- **Alternative Access**: 
  - Hyperliquid app integration
  - Direct Guardian Network API requests
  - Third-party integrations

### 3. Compliance Layer
Ensuring regulatory compliance:

- **OFAC Screening**: Transaction screening against sanctioned addresses
- **Geographical Restrictions**: IP-based geoblocking for restricted jurisdictions
- **Security Measures**: VPN detection and prevention mechanisms
- **KYC/AML**: Compliance with applicable regulations

## System Architecture

The Unit protocol architecture consists of interconnected components:

```
User Interface Layer
    ├── Unit Web App (app.hyperunit.xyz)
    ├── Hyperliquid Integration
    └── API Access

Guardian Network Layer
    ├── Guardian Nodes
    ├── MPC/TSS Key Management
    └── Consensus Protocol

Blockchain Layer
    ├── Bitcoin Network
    ├── Ethereum Network
    ├── Solana Network
    └── Hyperliquid L1
```

## Access Points

### Primary Interfaces
- **Web Interface**: [app.hyperunit.xyz](https://app.hyperunit.xyz)
- **Hyperliquid Integration**: [app.hyperliquid.xyz](https://app.hyperliquid.xyz)
- **Direct API**: Guardian Network API endpoints

### Developer Access
- RESTful API for programmatic access
- WebSocket connections for real-time updates
- SDK support for major programming languages

## Security Model

### Multi-Party Computation (MPC)
- Distributed key generation and management
- No single party controls private keys
- Threshold signatures for transaction authorization

### Guardian Requirements
- Stake-based participation
- Performance monitoring and slashing conditions
- Regular security audits and updates

## Next Steps

- Learn about [Components](/architecture/components) in detail
- Review [Security](/architecture/security) measures
- Explore [Developer API](/developers/api) documentation
- Understand [Key Addresses](/developers/key-addresses) for integration