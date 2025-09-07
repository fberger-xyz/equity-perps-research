#!/usr/bin/env python3
"""
Organize Equity Perpetuals Research Articles
Simple organizer without external dependencies
"""

import json
import os
from pathlib import Path
from datetime import datetime

class ResearchOrganizer:
    def __init__(self, base_dir: str = ".."):
        self.base_dir = Path(base_dir)
        self.data_dir = self.base_dir / "data"
        self.docs_dir = self.base_dir / "docs"
        
    def load_metadata(self):
        """Load articles metadata"""
        with open(self.data_dir / "articles_metadata.json", 'r') as f:
            return json.load(f)
    
    def create_key_insights(self):
        """Create KEY_INSIGHTS.md document"""
        data = self.load_metadata()
        
        content = ["# Key Insights from Equity Perpetuals Research\n\n"]
        content.append(f"*Generated: {datetime.now().strftime('%Y-%m-%d')}*\n\n")
        
        # Platform Insights
        content.append("## 🏛️ Platform Landscape\n\n")
        content.append("### DeFi Leaders\n")
        content.append("- **Hyperliquid**: Dominates with ~80% of decentralized perps market ($357B monthly volume)\n")
        content.append("- **Aster**: Pioneer in 24/7 US stock perps with 50× leverage via Pyth Network\n")
        content.append("- **PancakeSwap**: BNB Chain stock perps respecting US market hours (regulatory-conscious)\n\n")
        
        content.append("### CeFi Innovations\n")
        content.append("- **Bitget**: First RWA Index perpetuals (Tesla/Nvidia indexes with 10× leverage)\n")
        content.append("- Movement toward 24/5 trading schedules (bridging crypto and TradFi)\n\n")
        
        # Technical Architecture
        content.append("## 🔧 Technical Architecture Patterns\n\n")
        content.append("### Core Components\n")
        content.append("1. **Order Book Models**: Hyperliquid's on-chain order book achieves CEX-like performance\n")
        content.append("2. **Oracle Integration**: Pyth Network emerging as standard for real-time equity pricing\n")
        content.append("3. **Hybrid Infrastructure**: L1-EVM architectures balancing speed and composability\n")
        content.append("4. **Funding Rate Mechanisms**: Path-dependent rates ensuring price alignment\n\n")
        
        # Leverage & Risk
        content.append("## ⚖️ Leverage & Risk Parameters\n\n")
        content.append("| Platform | Max Leverage | Asset Type | Trading Hours |\n")
        content.append("|----------|-------------|------------|---------------|\n")
        content.append("| Aster | 50× | US Stocks | 24/7 |\n")
        content.append("| PancakeSwap | 25× | Synthetic Stocks | US Market Hours |\n")
        content.append("| Hyperliquid | 50× | Crypto (mainly) | 24/7 |\n")
        content.append("| Bitget | 10× | RWA Indexes | 24/5 |\n")
        content.append("| Ostium | 100-200× | RWAs | 24/7 |\n\n")
        
        # Regulatory Approaches
        content.append("## 📋 Regulatory Strategies\n\n")
        content.append("- **Synthetic vs Tokenized**: PancakeSwap avoids tokenization to sidestep securities laws\n")
        content.append("- **Market Hours Compliance**: Some platforms mirror traditional hours for regulatory alignment\n")
        content.append("- **Non-Custodial Design**: DeFi platforms emphasize permissionless, self-custody models\n")
        content.append("- **US Market Entry**: Bloomberg reports growing institutional interest despite regulatory uncertainty\n\n")
        
        # Market Impact
        content.append("## 💰 Market Disruption Potential\n\n")
        content.append("### Revenue Shift Estimates\n")
        content.append("- **$25-70B annually** could shift from prime brokers to DeFi (stock lending disruption)\n")
        content.append("- **$120T global equity market** potential for tokenization\n")
        content.append("- **$2.6T** in decentralized perps volume in 2025 alone\n\n")
        
        # Innovation Trends
        content.append("## 🚀 Innovation Trends\n\n")
        content.append("1. **24/7 Trading**: Breaking traditional market hour constraints\n")
        content.append("2. **Cross-Chain Perps**: Multi-chain deployment strategies emerging\n")
        content.append("3. **RWA Integration**: Bridging traditional assets (stocks, commodities, forex)\n")
        content.append("4. **Fee Burning Models**: Hyperliquid's 97% fee burn creating deflationary pressure\n")
        content.append("5. **Reverse Auction Listings**: Novel token distribution mechanisms\n\n")
        
        # Academic Contributions
        content.append("## 📚 Academic Research Highlights\n\n")
        content.append("- **PDLPs (Perpetual Demand Lending Pools)**: Optimizing capital efficiency\n")
        content.append("- **Funding Rate Theory**: Mathematical models for price stability\n")
        content.append("- **Replication Strategies**: Connecting perps to traditional derivatives theory\n\n")
        
        # Implementation Checklist
        content.append("## ✅ Implementation Checklist (from guides)\n\n")
        content.append("For teams building equity perps platforms:\n\n")
        content.append("- [ ] Chain selection (L1 vs L2 tradeoffs)\n")
        content.append("- [ ] On-chain order book implementation\n")
        content.append("- [ ] Matching engine optimization\n")
        content.append("- [ ] Oracle integration (Pyth, Chainlink)\n")
        content.append("- [ ] Risk management systems\n")
        content.append("- [ ] Funding rate calculations\n")
        content.append("- [ ] Liquidation mechanisms\n")
        content.append("- [ ] Front-end trading interface\n")
        content.append("- [ ] Security audits\n")
        content.append("- [ ] Liquidity incentives\n\n")
        
        # Future Outlook
        content.append("## 🔮 Future Outlook\n\n")
        content.append("### Near-term (2025)\n")
        content.append("- Hyperliquid L1 launch solidifying market position\n")
        content.append("- More DEXs adding stock perps following Aster/PancakeSwap\n")
        content.append("- Potential US regulatory clarity enabling broader adoption\n\n")
        
        content.append("### Long-term\n")
        content.append("- Convergence of TradFi and DeFi through perps infrastructure\n")
        content.append("- Global 24/7 markets becoming the norm\n")
        content.append("- Tokenized equity perps potentially replacing traditional short-selling\n\n")
        
        # References
        content.append("## 📖 Key References\n\n")
        content.append("See [INDEX.md](INDEX.md) for complete article list with URLs\n")
        
        # Write the file
        with open(self.docs_dir / "KEY_INSIGHTS.md", 'w') as f:
            f.writelines(content)
        
        print(f"Created KEY_INSIGHTS.md")
    
    def create_summary(self):
        """Create SUMMARY.md document"""
        data = self.load_metadata()
        
        content = ["# Equity Perpetuals Research Summary\n\n"]
        content.append(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n")
        
        # Executive Summary
        content.append("## Executive Summary\n\n")
        content.append("This research collection covers the emerging landscape of blockchain-based equity perpetual ")
        content.append("futures, examining 16 key articles from 2022-2025. The materials span DeFi platforms ")
        content.append("(Hyperliquid, Aster, PancakeSwap), centralized exchanges (Bitget), and academic research.\n\n")
        
        # Statistics
        content.append("## Collection Statistics\n\n")
        content.append(f"- **Total Articles**: {data['metadata']['total_articles']}\n")
        content.append(f"- **Date Range**: {data['metadata']['date_range']['earliest']} to {data['metadata']['date_range']['latest']}\n")
        content.append("- **Categories**:\n")
        for cat, count in data['metadata']['categories'].items():
            content.append(f"  - {cat}: {count} articles\n")
        content.append("\n")
        
        # Platform Coverage
        content.append("## Platform Coverage\n\n")
        platforms = {}
        for article in data['articles']:
            if 'platform' in article:
                plat = article['platform']
                if plat not in platforms:
                    platforms[plat] = []
                platforms[plat].append(article['title'])
        
        for platform, articles in sorted(platforms.items()):
            if platform != "Multiple" and len(articles) > 0:
                content.append(f"### {platform}\n")
                for title in articles[:3]:  # Show first 3
                    content.append(f"- {title}\n")
                if len(articles) > 3:
                    content.append(f"- *...and {len(articles)-3} more*\n")
                content.append("\n")
        
        # Key Themes
        content.append("## Dominant Themes\n\n")
        themes = {
            "24/7 Trading": "Breaking traditional market hours with continuous trading",
            "High Leverage": "Platforms offering 25×-200× leverage on equity positions",
            "Regulatory Navigation": "Synthetic vs tokenized approaches to avoid securities laws",
            "Market Dominance": "Hyperliquid capturing 80% of decentralized perps volume",
            "Oracle Integration": "Pyth Network emerging as standard for equity price feeds",
            "TradFi Bridge": "Connecting traditional assets to DeFi infrastructure"
        }
        
        for theme, description in themes.items():
            content.append(f"**{theme}**: {description}\n\n")
        
        # Recent Developments
        content.append("## Recent Developments (2025)\n\n")
        content.append("1. **Aster Launch (July)**: First major 24/7 US stock perps platform with 50× leverage\n")
        content.append("2. **PancakeSwap Stock Perps (August)**: BNB Chain entry with regulatory-conscious design\n")
        content.append("3. **Bitget RWA Indexes (August)**: CeFi innovation with tokenized equity index perps\n")
        content.append("4. **Hyperliquid Growth**: Achieving $357B monthly volume and 80% market share\n\n")
        
        # Research Categories
        content.append("## Research by Category\n\n")
        
        categories_detail = {
            "defi-dex": "Decentralized exchange implementations and platform analyses",
            "cefi": "Centralized exchange offerings and institutional approaches",
            "academic": "Theoretical models, funding rates, and mathematical frameworks",
            "technical": "Implementation guides and architectural patterns",
            "analysis": "Market impact studies and disruption potential"
        }
        
        for cat, description in categories_detail.items():
            if cat in data['metadata']['categories']:
                count = data['metadata']['categories'][cat]
                content.append(f"### {cat.upper()} ({count} articles)\n")
                content.append(f"{description}\n\n")
        
        # Market Metrics
        content.append("## Key Market Metrics\n\n")
        content.append("| Metric | Value | Source |\n")
        content.append("|--------|-------|--------|\n")
        content.append("| Hyperliquid Market Share | ~80% | Multiple sources |\n")
        content.append("| Monthly Volume (Hyperliquid) | $357B | BlockByte |\n")
        content.append("| 2025 DeFi Perps Volume | $2.6T | 21Shares |\n")
        content.append("| Potential Revenue Shift | $25-70B/year | Sentora |\n")
        content.append("| Global Equity Market Size | $120T | Market estimates |\n\n")
        
        # Next Steps
        content.append("## Recommended Reading Order\n\n")
        content.append("1. Start with **INDEX.md** for complete article listing\n")
        content.append("2. Review **KEY_INSIGHTS.md** for extracted insights\n")
        content.append("3. Deep dive into specific platforms via category folders\n")
        content.append("4. Explore academic papers for theoretical foundations\n\n")
        
        # Footer
        content.append("---\n\n")
        content.append("*This summary is part of the Equity Perpetuals Research collection.*\n")
        content.append("*For updates or additions, see the scripts/organize.py tool.*\n")
        
        # Write the file
        with open(self.docs_dir / "SUMMARY.md", 'w') as f:
            f.writelines(content)
        
        print(f"Created SUMMARY.md")
    
    def create_quick_reference(self):
        """Create a quick reference card"""
        data = self.load_metadata()
        
        content = ["# Quick Reference: Equity Perps Platforms\n\n"]
        
        content.append("## DeFi Platforms\n\n")
        content.append("| Platform | Leverage | Assets | Chain | Special Features |\n")
        content.append("|----------|----------|--------|-------|------------------|\n")
        content.append("| Aster | 50× | US Stocks | - | 24/7, Pyth oracles |\n")
        content.append("| PancakeSwap | 25× | AAPL, AMZN, TSLA | BNB | US hours, synthetic |\n")
        content.append("| Hyperliquid | 50× | Crypto | L1 | 80% market share |\n")
        content.append("| Ostium | 100-200× | RWAs | Arbitrum | Extreme leverage |\n\n")
        
        content.append("## CeFi Platforms\n\n")
        content.append("| Platform | Type | Leverage | Trading Hours |\n")
        content.append("|----------|------|----------|---------------|\n")
        content.append("| Bitget | RWA Indexes | 10× | 24/5 |\n\n")
        
        # Write to data directory
        with open(self.data_dir / "quick_reference.md", 'w') as f:
            f.writelines(content)
        
        print(f"Created quick_reference.md")
    
    def run(self):
        """Run all organization tasks"""
        print("Organizing Equity Perpetuals Research")
        print("=" * 50)
        
        # Create documents
        self.create_key_insights()
        self.create_summary()
        self.create_quick_reference()
        
        print("=" * 50)
        print("Organization complete!")
        print("\nKey files created:")
        print("- docs/INDEX.md (master index)")
        print("- docs/KEY_INSIGHTS.md (insights)")
        print("- docs/SUMMARY.md (executive summary)")
        print("- data/quick_reference.md (platform comparison)")
        print("- data/articles_metadata.json (structured data)")

if __name__ == "__main__":
    organizer = ResearchOrganizer()
    organizer.run()