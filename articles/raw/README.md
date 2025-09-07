# Raw Articles Folder

This folder was intended to store raw HTML/PDF content from scraped articles.

## Why It's Empty

1. **Access Restrictions**: Most websites (ETF.com, Medium, Bloomberg, etc.) block automated scraping with 403 Forbidden errors

2. **Missing Dependencies**: The `scraper.py` script requires the `requests` library which isn't installed

3. **Limited WebFetch Access**: The WebFetch tool successfully retrieved only:
   - Academic papers from arXiv (open access)
   - Some content from TokenMetrics
   
4. **Paywall/Login Requirements**: Many articles are behind paywalls or require authentication

## What You Can Do

To populate this folder with raw content:

1. **Manual Download**: Visit each URL in your browser and save the page
   - Use "Save As" → "Webpage, Complete" to get HTML + assets
   - Or use browser extensions to save clean HTML

2. **PDF Downloads**: For arXiv papers, download PDFs directly:
   - https://arxiv.org/pdf/2209.03307 (Primer on Perpetuals)
   - https://arxiv.org/pdf/2502.06028 (PDLPs)
   - https://arxiv.org/pdf/2506.08573 (Funding Rates)

3. **Archive Services**: Use archive.org or archive.is to access cached versions

4. **Browser Extensions**: Tools like SingleFile or Save Page WE can capture full pages

## Alternative Approach

Since automated scraping is limited, the project focuses on:
- Organizing all URLs for manual access
- Extracting and documenting key insights
- Creating structured metadata for research purposes

The INDEX.md file contains all URLs for direct browser access.