import type { NextApiRequest, NextApiResponse } from 'next';
import crypto from 'crypto';

/**
 * Default HTTP handler
 */
export default function handler(req: NextApiRequest, res: NextApiResponse) {
  try {
    const method = req.query.method as string;
    const host = 'https://api.gateio.ws';
    const prefix = '/api/v4';
    const headers = {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    };
    const url = req.query.url;
    const body = (req.query.body as string) || '';
    const query_param = (req.query.query_param as string) || '';

    const sign = genSign(method, prefix + url, query_param, body);
    res.status(200).json({
      ...sign,
      ...headers,
      method,
      prefix,
      url,
      query_param,
      body,
    });
  } catch (err) {
    res.status(500).end();
  }
}

/**
 * Return a signature object to be used in the header of a request to Gate.io
 */
function genSign(
  method: string,
  url: string,
  queryString?: string,
  payloadString?: string
) {
  const key = process.env.KEY;
  const secret = process.env.SECRET as string;
  const t = new Date().getTime() / 1000;
  const m = crypto.createHash('sha512');
  m.update(payloadString || '').setEncoding('utf-8');
  const hashedPayload = m.digest('hex');
  const s = `${method}\n${url}\n${queryString || ''}\n${hashedPayload}\n${t}`;
  const sign = crypto
    .createHmac('sha512', secret)
    .update(s)
    .setEncoding('utf-8')
    .digest('hex');
  return {
    KEY: key,
    Timestamp: t,
    SIGN: sign,
  };
}
