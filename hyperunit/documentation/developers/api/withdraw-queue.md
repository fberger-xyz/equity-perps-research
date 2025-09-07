# Withdraw Queue API

## Overview

The Withdraw Queue API provides real-time information about the withdrawal processing queue for different blockchain networks. Due to network throughput constraints and security requirements, withdrawals are processed in batches at regular intervals.

## Endpoint

### Request
`GET /withdrawal-queue`

### Base URLs
- **Production**: `https://api.hyperunit.xyz/withdrawal-queue`
- **Testnet**: `https://api.hyperunit-testnet.xyz/withdrawal-queue`

## Response Format

```json
{
  "bitcoin": {
    "lastWithdrawQueueOperationTxID": "f15cf8bb590cd7d50dc9d892c9d4d5ba370887f462cd5ac5e61ad2696b19e6cd",
    "withdrawalQueueLength": 2
  },
  "ethereum": {
    "lastWithdrawQueueOperationTxID": "0x95f792c9ba7d31d33b6d631824756e74cd85e6c1cb5d677b4614c324f57c6aa7",
    "withdrawalQueueLength": 0
  },
  "solana": {
    "lastWithdrawQueueOperationTxID": "4xK9L2mN3pQ5R6sT7uV8wX9yZ1aB2cD3eF4gH5jK6mN7",
    "withdrawalQueueLength": 1
  }
}
```

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `lastWithdrawQueueOperationTxID` | String | Transaction hash of the last processed batch |
| `withdrawalQueueLength` | Integer | Number of withdrawals currently in queue |

## Batch Processing Schedule

Withdrawals are processed in batches according to network-specific schedules:

| Network | Trigger Frequency | Approximate Interval | Batch Size |
|---------|------------------|---------------------|------------|
| Bitcoin | Every 3 blocks | ~30 minutes | Variable |
| Ethereum | Every 21 slots | ~4 minutes | Up to 100 |
| Solana | Every 100 slots | ~40 seconds | Up to 50 |

## Queue Management

### Understanding Queue Position

When a withdrawal enters the queue, its position determines processing order:

- **Position 0**: Next to be processed in the upcoming batch
- **Position 1-N**: Will be processed in subsequent batches
- **New entries**: Added to the end of the queue (FIFO)

### Estimating Processing Time

```javascript
function estimateProcessingTime(queueLength, network) {
  const batchIntervals = {
    bitcoin: 30,    // minutes
    ethereum: 4,    // minutes
    solana: 0.67    // minutes
  };
  
  const batchSizes = {
    bitcoin: 50,    // typical batch size
    ethereum: 100,
    solana: 50
  };
  
  const batchesNeeded = Math.ceil(queueLength / batchSizes[network]);
  const estimatedMinutes = batchesNeeded * batchIntervals[network];
  
  return {
    batches: batchesNeeded,
    minutes: estimatedMinutes,
    estimatedTime: new Date(Date.now() + estimatedMinutes * 60000)
  };
}
```

## API Usage Examples

### Basic Queue Check

```javascript
async function checkWithdrawQueue() {
  const response = await fetch('https://api.hyperunit.xyz/withdrawal-queue');
  const data = await response.json();
  
  console.log('Bitcoin queue:', data.bitcoin.withdrawalQueueLength);
  console.log('Ethereum queue:', data.ethereum.withdrawalQueueLength);
  console.log('Solana queue:', data.solana.withdrawalQueueLength);
  
  return data;
}
```

### Monitor Queue Changes

```javascript
class QueueMonitor {
  constructor(pollInterval = 30000) { // 30 seconds
    this.pollInterval = pollInterval;
    this.previousState = null;
  }
  
  async start(callback) {
    setInterval(async () => {
      const currentState = await this.checkQueue();
      
      if (this.hasChanged(currentState)) {
        callback(currentState, this.previousState);
      }
      
      this.previousState = currentState;
    }, this.pollInterval);
  }
  
  async checkQueue() {
    const response = await fetch('https://api.hyperunit.xyz/withdrawal-queue');
    return response.json();
  }
  
  hasChanged(current) {
    if (!this.previousState) return true;
    
    return ['bitcoin', 'ethereum', 'solana'].some(network => 
      current[network].withdrawalQueueLength !== 
      this.previousState[network].withdrawalQueueLength
    );
  }
}

// Usage
const monitor = new QueueMonitor();
monitor.start((current, previous) => {
  console.log('Queue changed!', current);
});
```

### Track Batch Processing

```javascript
async function trackBatchProcessing(network) {
  let lastTxId = null;
  
  while (true) {
    const response = await fetch('https://api.hyperunit.xyz/withdrawal-queue');
    const data = await response.json();
    
    const currentTxId = data[network].lastWithdrawQueueOperationTxID;
    
    if (lastTxId && currentTxId !== lastTxId) {
      console.log(`New batch processed on ${network}:`, currentTxId);
      
      // Fetch transaction details
      const txDetails = await getTransactionDetails(currentTxId, network);
      console.log('Batch details:', txDetails);
    }
    
    lastTxId = currentTxId;
    
    // Wait for next check
    await sleep(60000); // 1 minute
  }
}
```

## WebSocket Integration

For real-time queue updates:

```javascript
const ws = new WebSocket('wss://api.hyperunit.xyz/ws');

ws.on('open', () => {
  ws.send(JSON.stringify({
    action: 'subscribe',
    topic: 'withdrawal-queue'
  }));
});

ws.on('message', (data) => {
  const update = JSON.parse(data);
  
  if (update.type === 'queue-update') {
    console.log(`${update.network} queue: ${update.queueLength}`);
  }
  
  if (update.type === 'batch-processed') {
    console.log(`Batch processed on ${update.network}: ${update.txId}`);
  }
});
```

## Queue Optimization Strategies

### 1. Timing Optimization

Submit withdrawals when queues are shortest:

```javascript
async function findOptimalTime(network) {
  const samples = [];
  
  // Collect hourly samples
  for (let i = 0; i < 24; i++) {
    const data = await checkWithdrawQueue();
    samples.push({
      hour: new Date().getHours(),
      queueLength: data[network].withdrawalQueueLength
    });
    
    await sleep(3600000); // 1 hour
  }
  
  // Find hours with shortest queues
  const sorted = samples.sort((a, b) => a.queueLength - b.queueLength);
  return sorted.slice(0, 3).map(s => s.hour);
}
```

### 2. Batch Coordination

Coordinate multiple withdrawals for efficiency:

```javascript
async function coordinateBatchWithdrawals(withdrawals) {
  const queueStatus = await checkWithdrawQueue();
  
  // Group by network
  const grouped = {};
  withdrawals.forEach(w => {
    grouped[w.network] = grouped[w.network] || [];
    grouped[w.network].push(w);
  });
  
  // Submit to shortest queue first
  const networks = Object.keys(grouped).sort((a, b) => 
    queueStatus[a].withdrawalQueueLength - 
    queueStatus[b].withdrawalQueueLength
  );
  
  const results = [];
  for (const network of networks) {
    const networkWithdrawals = grouped[network];
    
    // Submit all at once to be in same batch
    const submissions = await Promise.all(
      networkWithdrawals.map(w => submitWithdrawal(w))
    );
    
    results.push({
      network,
      count: submissions.length,
      estimatedBatch: Math.ceil(
        queueStatus[network].withdrawalQueueLength / getBatchSize(network)
      )
    });
  }
  
  return results;
}
```

### 3. Queue Prediction

Predict future queue states:

```javascript
class QueuePredictor {
  constructor() {
    this.history = [];
  }
  
  async recordSample() {
    const data = await checkWithdrawQueue();
    this.history.push({
      timestamp: Date.now(),
      data
    });
    
    // Keep last 7 days
    const weekAgo = Date.now() - (7 * 24 * 60 * 60 * 1000);
    this.history = this.history.filter(h => h.timestamp > weekAgo);
  }
  
  predictQueue(network, hoursAhead) {
    const targetHour = (new Date().getHours() + hoursAhead) % 24;
    const targetDay = new Date().getDay();
    
    // Find similar times in history
    const similar = this.history.filter(h => {
      const date = new Date(h.timestamp);
      return date.getHours() === targetHour && 
             date.getDay() === targetDay;
    });
    
    if (similar.length === 0) return null;
    
    // Average queue length at this time
    const avgLength = similar.reduce((sum, s) => 
      sum + s.data[network].withdrawalQueueLength, 0
    ) / similar.length;
    
    return Math.round(avgLength);
  }
}
```

## Error Handling

### Common Response Codes

| Code | Description | Action |
|------|-------------|--------|
| 200 | Success | Process queue data |
| 429 | Rate limited | Implement backoff |
| 500 | Server error | Retry with exponential backoff |
| 503 | Service unavailable | Check status page |

### Robust Queue Checking

```javascript
async function checkQueueWithRetry(maxRetries = 3) {
  let lastError;
  
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      const response = await fetch('https://api.hyperunit.xyz/withdrawal-queue', {
        timeout: 5000 // 5 second timeout
      });
      
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }
      
      return await response.json();
    } catch (error) {
      lastError = error;
      
      // Exponential backoff
      const delay = Math.pow(2, attempt) * 1000;
      await sleep(delay);
    }
  }
  
  throw new Error(`Failed after ${maxRetries} attempts: ${lastError.message}`);
}
```

## Queue Analytics

### Generate Queue Report

```javascript
async function generateQueueReport() {
  const current = await checkWithdrawQueue();
  const estimates = {};
  
  for (const network of ['bitcoin', 'ethereum', 'solana']) {
    const queueLength = current[network].withdrawalQueueLength;
    const processing = estimateProcessingTime(queueLength, network);
    
    estimates[network] = {
      currentQueue: queueLength,
      estimatedBatches: processing.batches,
      estimatedMinutes: processing.minutes,
      completionTime: processing.estimatedTime,
      lastBatchTx: current[network].lastWithdrawQueueOperationTxID
    };
  }
  
  return {
    timestamp: new Date(),
    queues: estimates,
    recommendations: generateRecommendations(estimates)
  };
}

function generateRecommendations(estimates) {
  const recommendations = [];
  
  for (const [network, data] of Object.entries(estimates)) {
    if (data.currentQueue === 0) {
      recommendations.push(`${network}: Optimal time for withdrawals (empty queue)`);
    } else if (data.estimatedMinutes > 60) {
      recommendations.push(`${network}: Long wait time (${data.estimatedMinutes}min), consider delaying`);
    }
  }
  
  return recommendations;
}
```

## Related Resources

- [Withdrawal Lifecycle](/developers/api/operations/withdrawal-lifecycle)
- [Estimate Fees](/developers/api/estimate-fees)
- [API Overview](/developers/api)
- [Architecture Overview](/architecture/quickstart)

## Support

For assistance with withdrawal queues:
- API Documentation: https://docs.hyperunit.xyz
- Developer Support: developers@hyperunit.xyz
- Status Updates: https://status.hyperunit.xyz