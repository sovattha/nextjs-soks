import requests
import time
import hashlib
import hmac
import time
import hashlib
import hmac
import json


def gen_sign(method, url, query_string=None, payload_string=None):
    key = ''        # api_key
    secret = ''     # api_secret

    t = time.time()
    m = hashlib.sha512()
    m.update((payload_string or "").encode('utf-8'))
    hashed_payload = m.hexdigest()
    s = '%s\n%s\n%s\n%s\n%s' % (
        method, url, query_string or "", hashed_payload, t)
    sign = hmac.new(secret.encode('utf-8'), s.encode('utf-8'),
                    hashlib.sha512).hexdigest()
    return {'KEY': key, 'Timestamp': str(t), 'SIGN': sign}


host = "https://api.gateio.ws"
prefix = "/api/v4"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

url = '/spot/orders'
query_param = 'currency_pair=BTC_USDT&status=open'
# for `gen_sign` implementation, refer to section `Authentication` above
sign_headers = gen_sign('GET', prefix + url, query_param)
headers.update(sign_headers)
print(sign_headers)
print('GET', host + prefix + url +
      "?" + query_param, headers)
r = requests.request('GET', host + prefix + url +
                     "?" + query_param, headers=headers)
print(r.json())
