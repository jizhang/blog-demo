import time
import os.path
import asyncio
import logging
import argparse
from collections import deque
from urllib.parse import urlparse, parse_qs

import websockets
from ansi2html import Ansi2HTMLConverter

NUM_LINES = 1000
HEARTBEAT_INTERVAL = 15 # seconds

# init
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)
allowed_prefixes = []
conv = Ansi2HTMLConverter(inline=True)


async def view_log(websocket, path):

    logging.info('Connected, remote={}, path={}'.format(websocket.remote_address, path))

    try:
        try:
            parse_result = urlparse(path)
        except Exception:
            raise ValueError('Fail to parse URL')

        file_path = os.path.abspath(parse_result.path)
        allowed = False
        for prefix in allowed_prefixes:
            if file_path.startswith(prefix):
                allowed = True
                break
        if not allowed:
            raise ValueError('Forbidden')

        if not os.path.isfile(file_path):
            raise ValueError('Not found')

        query = parse_qs(parse_result.query)
        tail = query and query['tail'] and query['tail'][0] == '1'

        with open(file_path) as f:

            content = ''.join(deque(f, NUM_LINES))
            content = conv.convert(content, full=False)
            await websocket.send(content)

            if tail:
                last_heartbeat = time.time()
                while True:
                    content = f.read()
                    if content:
                        content = conv.convert(content, full=False)
                        await websocket.send(content)
                    else:
                        await asyncio.sleep(1)

                    # heartbeat
                    if time.time() - last_heartbeat > HEARTBEAT_INTERVAL:
                        try:
                            await websocket.send('ping')
                            pong = await asyncio.wait_for(websocket.recv(), 5)
                            if pong != 'pong':
                                raise Exception()
                        except Exception:
                            raise Exception('Ping error')
                        else:
                            last_heartbeat = time.time()

            else:
                await websocket.close()

    except ValueError as e:
        try:
            await websocket.send('<font color="red"><strong>{}</strong></font>'.format(e))
            await websocket.close()
        except Exception:
            pass

        log_close(websocket, path, e)

    except Exception as e:
        log_close(websocket, path, e)

    else:
        log_close(websocket, path)


def log_close(websocket, path, exception=None):
    message = 'Closed, remote={}, path={}'.format(websocket.remote_address, path)
    if exception is not None:
        message += ', exception={}'.format(exception)
    logging.info(message)


async def serve(host: str, port: int):
    async with websockets.serve(view_log, host, port):
        await asyncio.Future()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8765)
    parser.add_argument('--prefix', required=True, action='append', help='Allowed directories')
    args = parser.parse_args()

    allowed_prefixes.extend(args.prefix)
    asyncio.run(serve(args.host, args.port))


if __name__ == '__main__':
    main()
