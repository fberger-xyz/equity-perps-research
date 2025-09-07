# Unit Protocol Components

## Guardian Network

The Guardian Network is the core infrastructure layer of the Unit Protocol, providing decentralized security and operation management.

### Core Principles

- **Independent Operation**: Operated by independent "Guardians" who maintain protocol integrity
- **Blockchain Integration**: Uses dedicated blockchain indexers for each supported chain
- **Transaction Verification**: Verifies on-chain activity and ensures transaction finality
- **MPC Security**: Implements a 2-of-3 Multi-Party Computation (MPC) threshold signature scheme

### Key Features

- **Distributed Control**: Prevents unilateral operations by any single Guardian
- **Key Management**: Maintains distributed key shares across the network
- **Leadership Model**: Uses a predetermined leader to coordinate proposals
- **Message Relay**: Employs a relay server for message passing with no key material storage

## Agent Components

The Agent is the core software that enforces protocol rules through four primary components:

### 1. Chain Services
Responsible for blockchain interactions:
- Track incoming deposits across supported chains
- Confirm transaction finality based on chain-specific requirements
- Build and broadcast transaction payloads
- Monitor blockchain state changes

### 2. Flow Manager
Orchestrates protocol operations:
- Manages multi-step state machine for complex operations
- Enforces strict sequencing of protocol steps
- Ensures all protocol requirements are met before proceeding
- Handles error recovery and rollback scenarios

### 3. Consensus Service
Implements distributed agreement:
- Enforces t-of-n quorum rules (typically 2-of-3)
- Requires Guardian agreement on all critical operations
- Manages proposal submission and voting
- Ensures Byzantine fault tolerance

### 4. Wallet Manager
Handles cryptographic operations:
- Manages MPC-based key operations
- Operates within secure enclaves (e.g., AWS Nitro)
- Stores encrypted secret shares
- Coordinates threshold signatures for transactions
- Generates deterministic addresses

## Network Architecture

### Guardian Roles

Each Guardian in the network has specific responsibilities:

1. **Leader Guardian**
   - Proposes new operations
   - Coordinates consensus rounds
   - Manages operation sequencing

2. **Verifier Guardians**
   - Independently validate proposals
   - Participate in consensus voting
   - Monitor for protocol violations

### Communication Protocol

The Guardian Network uses a sophisticated communication system:

- **Encrypted Channels**: All inter-Guardian communication is encrypted
- **Relay Infrastructure**: Messages pass through relay servers that cannot read content
- **Fault Tolerance**: System continues operating even if relay servers fail
- **Latency Optimization**: Geographic distribution for optimal performance

## Initial Guardian Network Participants

The protocol launched with three trusted entities as initial Guardians:

1. **Unit**: The protocol development team
2. **Hyperliquid**: The underlying L1 blockchain team
3. **Infinite Field**: Independent security and infrastructure provider

## Scalability and Future Expansion

The architecture is designed for future growth:

- **Additional Guardians**: Protocol supports adding new Guardian participants
- **Chain Support**: Modular design allows adding new blockchain integrations
- **Performance Scaling**: Can increase throughput through protocol upgrades
- **Geographic Distribution**: Supports global Guardian distribution for resilience

## Technical Specifications

### MPC Implementation
- **Threshold**: 2-of-3 signature scheme
- **Key Generation**: Distributed key generation protocol
- **Resharing**: Support for key resharing when Guardian set changes
- **Recovery**: Mechanisms for recovering from Guardian failures

### State Management
- **Deterministic State Machine**: All Guardians maintain identical state
- **Checkpointing**: Regular state checkpoints for recovery
- **Audit Logs**: Comprehensive logging of all state transitions
- **Rollback Protection**: Prevents state regression attacks

## Integration Points

### For Developers
- RESTful API endpoints for protocol interaction
- WebSocket connections for real-time updates
- SDK libraries for common programming languages
- Example implementations and best practices

### For Users
- Web interface at app.hyperunit.xyz
- Integration with Hyperliquid platform
- Mobile-responsive design
- Multi-language support

## Related Resources

- [Security Architecture](/architecture/security)
- [API Documentation](/developers/api)
- [Guardian Signatures](/developers/api/generate-address/guardian-signatures)