import requests
import time
import hashlib
import hmac


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
    print(t, sign)
    return {'KEY': key, 'Timestamp': str(t), 'SIGN': sign}


host = "https://api.gateio.ws"
prefix = "/api/v4"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

url = '/spot/orders'
query_param = ''
body = '{"text":"t-123456","currency_pair":"ETH_BTC","type":"limit","account":"spot","side":"buy","iceberg":"0","amount":"1","price":"5.00032","time_in_force":"gtc","auto_borrow":false}'
# for `gen_sign` implementation, refer to section `Authentication` above
sign_headers = gen_sign('POST', prefix + url, query_param, body)
headers.update(sign_headers)
print('POST', host + prefix + url, headers, body)
r = requests.request('POST', host + prefix + url, headers=headers, data=body)
print(r.json())
