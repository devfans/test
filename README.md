# API Documentation

## API common parameters
- key: ApiKey
- nonce: Any integer larger than last request.
- sig: Signature generated with ApiKey, nonce and ApiSecret
##### Signature generation sample
```
message = userid + api_key + nonce
signature = hmac.new(API_SECRET, msg=message, digestmod=hashlib.sha256).hexdigest().upper()
```
#### Notes
- Every ApiKey can only send 60 requests within one minute for protection of the system.
- Some results will be cached and cache may survive for 2 to 3 minutes depending on which kind of data you are requesting.
## API Endpoints
### Get pool stats
```https://api.dcexploration.com/api/v1/poolStats```
##### Result:
```
{
  "status": 0,
  "poolHashrateLast10m": 0,
  "poolHashrateLast30m": 0,
  "poolHashrateLast1h": 0,
  "poolRejectrateLast10m": 0,
  "poolRejectrateLast30m": 0,
  "poolRejectrateLast1h": 0,
  "currentRound": 18,
  "currentLuck": 154.385,
  "currentWorkers": 0
}
```
### Get account info
```https://api.dcexploration.com/api/v1/account```
##### Result:
```
{
  "status": 0,
  "region": "cn",
  "coin": "btc",
  "miner": "miner-test",
  "fee": 0,
  "txfee": 0,
  "pay_min": 0.01,
  "address": "xxxxxx",
  "balance": 831908,
  "pay_mode": "PPS",
  "mining_mode": "BTC"
}
```
### Get miner hashrate
```https://api.dcexploration.com/api/v1/hashrate```
##### Result:
```
{
  "status": 0,
  "region": "cn",
  "coin": "btc",
  "miner": "miner-test",
  "hashrateLast10m": 0,
  "hashrateLast30m": 0,
  "hashrateLast1h": 0,
  "rejectrateLast10m": 0,
  "rejectrateLast30m": 0,
  "rejectrateLast1h": 0
}
```
### Get workers status
```https://api.dcexploration.com/api/v1/workers```
##### Result:
```
{
  "status": 0,
  "totalActive": 0,
  "totalDead": 1,
  "totalHashrate": 0,
  "region": "cn",
  "coin": "btc",
  "miner": "miner-test",
  "totalRecords": 1,
  "totalPages": 1,
  "pageSize": 10,
  "page": 1,
  "data": [
    {
      "workername": "4X61",
      "hashrate": 0,
      "rejectrate": 0,
      "active": false,
      "last_submit": "2017-11-06 07:52:24"
    }
  ]
}
```
### Get payment history
```https://api.dcexploration.com/api/v1/payments```
##### Result:
```
{
  "status": 0,
  "paid": 46865389,
  "paying": 0,
  "region": "cn",
  "coin": "btc",
  "miner": "miner-test",
  "totalRecords": 1,
  "totalPages": 1,
  "pageSize": 10,
  "page": 1,
  "data": [
    {
      "txid": "xxxxxxxxxx",
      "amount": 46865389,
      "timestamp": "2017-10-26 00:00:22",
      "address": "xxxxxxxxxxxx",
      "pay_mode": "PPS",
      "paid": true
    }
  ]
}
```
