# A Primer on Perpetuals

**Source**: arXiv  
**URL**: https://arxiv.org/abs/2209.03307  
**Date**: September 2022  
**Authors**: Guillermo Angeris, Tarun Chitra, Alex Evans, Matthew Lorig  

## Abstract

This foundational academic paper introduces theoretical models for perpetual contracts in continuous-time financial markets with no arbitrage or transaction costs.

## Key Theoretical Contributions

### Two Types of Perpetual Contracts

1. **First Contract Type**
   - Payoff to long side is a fixed function of underlying assets
   - Long side pays a funding rate to the short side
   - Requires continuous funding payments

2. **Second Contract Type**
   - Payoff to long side is a fixed function of underlying assets multiplied by a time-varying discount factor
   - No funding payments required
   - Uses discount factor mechanism instead

### Mathematical Modeling Approach

The paper provides:
- Model-free expressions for funding and discount rates
- Complete replication strategies for the short side
- Analysis covering multiple scenarios:
  - Continuous, strictly positive asset prices
  - Asset prices with potential jumps
  - Volatility processes independent of risky assets

### Connection to Traditional Finance

The authors demonstrate how perpetual contracts relate to:
- Variance swaps
- Leveraged exchange-traded funds (ETFs)
- Traditional derivatives pricing models

## Significance for Equity Perpetuals

This theoretical foundation is crucial for understanding:
- How funding rates should be designed to maintain price alignment
- The mathematical relationship between perpetual contracts and spot prices
- Risk management strategies for market makers and traders
- The theoretical basis for implementing perpetuals on blockchain

## Key Concepts

- **Funding Rate**: The periodic payment between long and short positions to maintain price parity
- **Replication Strategy**: How to synthetically create the payoff of a perpetual contract
- **No-Arbitrage Conditions**: Mathematical constraints ensuring fair pricing
- **Continuous-Time Models**: Framework for analyzing perpetual contracts in real-time markets

This paper provides the theoretical underpinning for many of the perpetual futures implementations seen in DeFi platforms like Hyperliquid, dYdX, and the emerging equity perpetuals on Aster and PancakeSwap.