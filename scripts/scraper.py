#!/usr/bin/env python3
"""
Equity Perpetuals Research Scraper
Fetches and organizes articles about blockchain equity perpetuals
"""

import json
import os
import re
import time
import hashlib
from datetime import datetime
from typing import Dict, List, Optional
from urllib.parse import urlparse
import requests
from pathlib import Path

class EquityPerpsResearchScraper:
    def __init__(self, base_dir: str = ".."):
        self.base_dir = Path(base_dir)
        self.articles_dir = self.base_dir / "articles"
        self.data_dir = self.base_dir / "data"
        self.raw_dir = self.articles_dir / "raw"
        
        # Create directories if needed
        for dir_path in [self.articles_dir, self.data_dir, self.raw_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
        
        self.articles_index = []
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Research Bot'
        })
    
    def load_articles_metadata(self) -> List[Dict]:
        """Load article metadata from INDEX.md or predefined list"""
        articles = [
            {
                "id": "aster-etf-2025",
                "title": "Aster Launches 24/7 Stock Perpetual Contracts Trading",
                "url": "https://www.etf.com/sections/news/aster-launches-247-stock-perpetual-contracts-trading-exposure-us-equities",
                "category": "defi-dex",
                "date": "2025-07-16",
                "platform": "Aster",
                "key_topics": ["stock perps", "24/7 trading", "50x leverage", "Pyth Network"]
            },
            {
                "id": "pancakeswap-stocks-2025",
                "title": "PancakeSwap On-Chain Stock Perpetuals",
                "url": "https://www.cryptopolitan.com/pancakeswap-tokenized-stocks-perp-contracts/",
                "category": "defi-dex",
                "date": "2025-08-06",
                "platform": "PancakeSwap",
                "key_topics": ["BNB Chain", "synthetic stocks", "25x leverage", "US market hours"]
            },
            {
                "id": "hyperliquid-craze-2025",
                "title": "Understanding Hyperliquid Craze",
                "url": "https://medium.com/@nefture/understanding-crypto-perpetual-futures-and-the-hyperliquid-craze-7d1c8b413444",
                "category": "defi-dex",
                "date": "2025-01-01",
                "platform": "Hyperliquid",
                "key_topics": ["80% market share", "CEX-like performance", "L1 chain"]
            },
            {
                "id": "hyperliquid-tokenmetrics-2025",
                "title": "Hyperliquid Redefining Decentralized Perpetuals",
                "url": "https://www.tokenmetrics.com/blog/how-hyperliquid-is-redefining-decentralized-perpetuals-in-2025",
                "category": "defi-dex",
                "date": "2025-01-01",
                "platform": "Hyperliquid",
                "key_topics": ["reverse auction", "sustainable revenue", "L1 development"]
            },
            {
                "id": "build-hyperliquid-2025",
                "title": "Building Hyperliquid-like Platform Guide",
                "url": "https://www.antiersolutions.com/blogs/how-to-build-your-perpetual-futures-trading-platform-like-hyperliquid-in-2025/",
                "category": "technical",
                "date": "2025-08-01",
                "platform": "Guide",
                "key_topics": ["architecture", "order book", "matching engine", "implementation"]
            },
            {
                "id": "bitget-rwa-2025",
                "title": "Bitget RWA Index Perpetuals",
                "url": "https://www.financemagnates.com/cryptocurrency/bitget-rwa-index-perpetuals",
                "category": "cefi",
                "date": "2025-08-20",
                "platform": "Bitget",
                "key_topics": ["RWA index", "Tesla/Nvidia", "24/5 trading", "10x leverage"]
            },
            {
                "id": "pdlp-arxiv-2025",
                "title": "Perpetual Demand Lending Pools",
                "url": "https://arxiv.org/abs/2502.06028",
                "category": "academic",
                "date": "2025-02-01",
                "platform": "Academic",
                "key_topics": ["capital efficiency", "arbitrage", "theoretical models"]
            },
            {
                "id": "funding-rates-arxiv-2025",
                "title": "Designing Funding Rates for Perpetual Futures",
                "url": "https://arxiv.org/abs/2506.08573",
                "category": "academic",
                "date": "2025-06-01",
                "platform": "Academic",
                "key_topics": ["funding rates", "price stability", "replication"]
            },
            {
                "id": "perps-primer-arxiv-2022",
                "title": "A Primer on Perpetuals",
                "url": "https://arxiv.org/abs/2209.03307",
                "category": "academic",
                "date": "2022-09-01",
                "platform": "Academic",
                "key_topics": ["continuous models", "derivatives theory", "foundations"]
            }
        ]
        return articles
    
    def fetch_article(self, article: Dict) -> Optional[str]:
        """Fetch article content with error handling"""
        try:
            print(f"Fetching: {article['title'][:50]}...")
            
            # Rate limiting
            time.sleep(1)
            
            # Special handling for different domains
            domain = urlparse(article['url']).netloc
            
            if 'arxiv.org' in domain:
                # For arXiv, we'd typically fetch the PDF
                # For now, just fetch the abstract page
                response = self.session.get(article['url'], timeout=10)
            else:
                response = self.session.get(article['url'], timeout=10)
            
            if response.status_code == 200:
                return response.text
            else:
                print(f"  Failed with status {response.status_code}")
                return None
                
        except Exception as e:
            print(f"  Error: {str(e)}")
            return None
    
    def extract_text_content(self, html: str, url: str) -> str:
        """Extract readable text from HTML (basic extraction)"""
        # Remove script and style elements
        html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
        html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL)
        
        # Extract title
        title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE)
        title = title_match.group(1) if title_match else ""
        
        # Extract meta description
        desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']+)["\']', html, re.IGNORECASE)
        description = desc_match.group(1) if desc_match else ""
        
        # Extract article body (common patterns)
        body = ""
        for pattern in [
            r'<article[^>]*>(.*?)</article>',
            r'<main[^>]*>(.*?)</main>',
            r'<div[^>]*class=["\'][^"\']*content[^"\']*["\'][^>]*>(.*?)</div>',
        ]:
            match = re.search(pattern, html, re.DOTALL | re.IGNORECASE)
            if match:
                body = match.group(1)
                break
        
        # Clean HTML tags
        text = re.sub(r'<[^>]+>', ' ', body if body else html)
        text = re.sub(r'\s+', ' ', text)
        
        return f"Title: {title}\n\nDescription: {description}\n\nContent Extract:\n{text[:5000]}"
    
    def save_article(self, article: Dict, content: Optional[str]):
        """Save article content and metadata"""
        if not content:
            article['status'] = 'failed'
            article['fetched_at'] = None
            return
        
        # Generate filename
        file_hash = hashlib.md5(article['url'].encode()).hexdigest()[:8]
        filename = f"{article['id']}_{file_hash}.txt"
        
        # Save raw HTML
        raw_path = self.raw_dir / f"{article['id']}.html"
        with open(raw_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Extract and save text
        text_content = self.extract_text_content(content, article['url'])
        category_dir = self.articles_dir / article['category']
        category_dir.mkdir(exist_ok=True)
        
        text_path = category_dir / filename
        with open(text_path, 'w', encoding='utf-8') as f:
            f.write(f"# {article['title']}\n\n")
            f.write(f"URL: {article['url']}\n")
            f.write(f"Date: {article['date']}\n")
            f.write(f"Platform: {article['platform']}\n")
            f.write(f"Topics: {', '.join(article['key_topics'])}\n\n")
            f.write("---\n\n")
            f.write(text_content)
        
        # Update metadata
        article['status'] = 'success'
        article['fetched_at'] = datetime.now().isoformat()
        article['local_path'] = str(text_path.relative_to(self.base_dir))
        article['raw_path'] = str(raw_path.relative_to(self.base_dir))
    
    def scrape_all(self):
        """Main scraping function"""
        print("Starting Equity Perps Research Scraper")
        print("=" * 50)
        
        # Load articles
        articles = self.load_articles_metadata()
        print(f"Found {len(articles)} articles to process\n")
        
        # Process each article
        for i, article in enumerate(articles, 1):
            print(f"[{i}/{len(articles)}] Processing {article['id']}")
            
            # Fetch content
            content = self.fetch_article(article)
            
            # Save article
            self.save_article(article, content)
            
            # Add to index
            self.articles_index.append(article)
            
            print(f"  Status: {article['status']}\n")
        
        # Save index
        self.save_index()
        
        # Generate summary
        self.generate_summary()
        
        print("=" * 50)
        print("Scraping complete!")
        print(f"Success: {sum(1 for a in self.articles_index if a['status'] == 'success')}")
        print(f"Failed: {sum(1 for a in self.articles_index if a['status'] == 'failed')}")
    
    def save_index(self):
        """Save the articles index as JSON"""
        index_path = self.data_dir / "index.json"
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(self.articles_index, f, indent=2)
        print(f"Index saved to {index_path}")
    
    def generate_summary(self):
        """Generate a summary document"""
        summary_path = self.base_dir / "docs" / "SUMMARY.md"
        
        content = ["# Equity Perpetuals Research Summary\n"]
        content.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        
        # Statistics
        content.append("## Statistics\n")
        content.append(f"- Total Articles: {len(self.articles_index)}\n")
        content.append(f"- Successfully Fetched: {sum(1 for a in self.articles_index if a.get('status') == 'success')}\n")
        
        # By category
        categories = {}
        for article in self.articles_index:
            cat = article['category']
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(article)
        
        content.append(f"- Categories: {', '.join(categories.keys())}\n\n")
        
        # By platform
        platforms = {}
        for article in self.articles_index:
            plat = article['platform']
            if plat not in platforms:
                platforms[plat] = []
            platforms[plat].append(article)
        
        content.append("## Articles by Platform\n")
        for platform, arts in sorted(platforms.items()):
            content.append(f"\n### {platform} ({len(arts)} articles)\n")
            for art in arts:
                status = "✓" if art.get('status') == 'success' else "✗"
                content.append(f"- [{status}] {art['title']}\n")
        
        # Key topics frequency
        topic_count = {}
        for article in self.articles_index:
            for topic in article['key_topics']:
                topic_count[topic] = topic_count.get(topic, 0) + 1
        
        content.append("\n## Top Topics\n")
        for topic, count in sorted(topic_count.items(), key=lambda x: x[1], reverse=True)[:10]:
            content.append(f"- {topic}: {count} articles\n")
        
        # Write summary
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.writelines(content)
        
        print(f"Summary saved to {summary_path}")

if __name__ == "__main__":
    scraper = EquityPerpsResearchScraper()
    scraper.scrape_all()