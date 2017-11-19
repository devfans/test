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
