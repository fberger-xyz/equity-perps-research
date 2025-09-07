# Equity Perpetuals Research Collection

A comprehensive research collection on blockchain-based equity perpetual futures, covering DeFi platforms, CeFi exchanges, and academic papers.

## 📁 Repository Structure

```
equity-perps-research/
├── articles/              # Article content (to be populated)
│   ├── defi-dex/         # DeFi & DEX articles
│   ├── cefi/             # Centralized exchange articles
│   ├── academic/         # Research papers
│   └── raw/              # Original downloads
├── data/                 # Structured data
│   ├── articles_metadata.json   # Complete article database
│   └── quick_reference.md       # Platform comparison table
├── docs/                 # Documentation
│   ├── INDEX.md          # Master index with all URLs
│   ├── SUMMARY.md        # Executive summary
│   └── KEY_INSIGHTS.md   # Extracted insights
└── scripts/              # Tools
    ├── organize.py       # Organization tool
    └── scraper.py        # Web scraper (requires requests)
```

## 🚀 Quick Start

### View the Research

1. **Start here**: [docs/INDEX.md](docs/INDEX.md) - Complete list of 16 articles with direct URLs
2. **Key insights**: [docs/KEY_INSIGHTS.md](docs/KEY_INSIGHTS.md) - Extracted insights and trends
3. **Executive summary**: [docs/SUMMARY.md](docs/SUMMARY.md) - Overview and statistics
4. **Quick reference**: [data/quick_reference.md](data/quick_reference.md) - Platform comparison

### Access Articles

All article URLs are available in:
- **Markdown format**: [docs/INDEX.md](docs/INDEX.md)
- **JSON format**: [data/articles_metadata.json](data/articles_metadata.json)

## 📊 Coverage Overview

- **16 Articles** spanning 2022-2025
- **Platforms**: Hyperliquid, Aster, PancakeSwap, Bitget, and more
- **Topics**: Stock perps, leverage models, regulatory approaches, technical architecture
- **Sources**: ETF.com, Bloomberg, Medium, arXiv, TokenMetrics, and others

## 🔑 Key Findings

### Platform Leaders
- **Hyperliquid**: ~80% of decentralized perps market ($357B monthly volume)
- **Aster**: Pioneer in 24/7 US stock perps with 50× leverage
- **PancakeSwap**: BNB Chain stock perps with regulatory-conscious design

### Market Impact
- **$2.6T** in decentralized perps volume in 2025
- **$25-70B** potential annual revenue shift from TradFi to DeFi
- **$120T** global equity market tokenization potential

### Innovation Trends
- 24/7 trading breaking traditional market hours
- Synthetic derivatives avoiding securities regulations
- Pyth Network emerging as standard oracle for equity pricing
- L1 chains optimized for perpetual trading

## 🛠️ Tools

### organize.py
Generates summary documents from metadata:
```bash
cd scripts
python3 organize.py
```

### scraper.py
Fetches article content (requires `requests` library):
```bash
pip install requests
cd scripts
python3 scraper.py
```

## 📚 Research Categories

| Category | Count | Focus |
|----------|-------|-------|
| DeFi/DEX | 10 | Decentralized platforms and protocols |
| CeFi | 2 | Centralized exchange implementations |
| Academic | 3 | Theoretical models and research papers |
| Technical | 1 | Implementation guides |
| Analysis | 1 | Market disruption studies |

## 🔗 Quick Links to Key Articles

### Must-Read Articles
1. [Aster Launches 24/7 Stock Perps](https://www.etf.com/sections/news/aster-launches-247-stock-perpetual-contracts-trading-exposure-us-equities)
2. [PancakeSwap Stock Perpetuals](https://www.cryptopolitan.com/pancakeswap-tokenized-stocks-perp-contracts/)
3. [Understanding Hyperliquid](https://medium.com/@nefture/understanding-crypto-perpetual-futures-and-the-hyperliquid-craze-7d1c8b413444)
4. [Building Perps Platform Guide](https://www.antiersolutions.com/blogs/how-to-build-your-perpetual-futures-trading-platform-like-hyperliquid-in-2025/)

### Academic Papers
1. [Perpetual Demand Lending Pools](https://arxiv.org/abs/2502.06028)
2. [Designing Funding Rates](https://arxiv.org/abs/2506.08573)
3. [A Primer on Perpetuals](https://arxiv.org/abs/2209.03307)

## 📈 Platform Comparison

| Platform | Leverage | Assets | Trading Hours | Special Features |
|----------|----------|--------|---------------|------------------|
| Aster | 50× | US Stocks | 24/7 | Pyth oracles, non-custodial |
| PancakeSwap | 25× | AAPL, AMZN, TSLA | US hours | Synthetic, BNB Chain |
| Hyperliquid | 50× | Crypto | 24/7 | 80% market share, L1 |
| Bitget | 10× | RWA Indexes | 24/5 | Tesla/Nvidia indexes |
| Ostium | 100-200× | RWAs | 24/7 | Extreme leverage |

## 📅 Last Updated

September 7, 2025

---

*This collection provides a comprehensive overview of the rapidly evolving equity perpetuals landscape on blockchain. For the latest developments, check the original article sources.*