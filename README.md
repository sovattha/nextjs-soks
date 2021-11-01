# Gate.io API authenticator for Next.js

This is an alternative to the Gate.io API for NodeJS https://github.com/gateio/gateapi-nodejs

## Setup

1. Rename `env.example` to `.env` and fill in your key and secret
2. `yarn`
3. `yarn dev`

## How to use

### 1. Call the endpoint /api/gate

For example:
http://localhost:3000/api/gate?method=GET&url=/wallet/deposits

You will get a response like:

```
{
    "KEY": "<your key>",
    "Timestamp": 1635807198.638,
    "SIGN": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "method": "GET",
    "prefix": "/api/v4",
    "url": "/wallet/deposits",
    "query_param": "",
    "body": ""
}
```

### 2. Use the values in a separate request to Gate.io API

For example:
https://api.gateio.ws/api/v4/wallet/deposits

with the header values filled in from the previous request:

- `KEY`
- `Timestamp`
- `SIGN`

```
GET /api/v4/wallet/deposits HTTP/1.1
Host: api.gateio.ws
KEY: <your key>
Timestamp: 1635807198.638
SIGN: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Cookie: login_notice_check=%2F
```

### 3. For POST requests

Pass the body as a string, like so:

http://localhost:3000/api/gate?method=POST&url=/spot/orders&body={"text":"t-123456","currency_pair":"ETH_BTC","type":"limit","account":"spot","side":"buy","iceberg":"0","amount":"1","price":"5.00032","time_in_force":"gtc","auto_borrow":false}
