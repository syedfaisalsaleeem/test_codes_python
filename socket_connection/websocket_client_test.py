import websocket
import json
try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    print("opened")
    auth_data = {
    "action": "authenticate",
    "data": {"key_id": "PKYGXZDBD43YGTLWOYRD", 
    "secret_key": "KRuuE0FmSt9IHc3YZEUUky6GuJtl1W8vtCTM6s8V"}}
    ws.send(json.dumps(auth_data))
    listen_message = {
    "action":"listen",
    "data":{"streams":["T.SPY"]}
    }
    # def run(*args):
    #     for i in range(3):
    #         time.sleep(1)
    #         ws.send("Hello %d" % i)
    #     time.sleep(1)
    #     ws.close()
    #     print("thread terminating...")
    # thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://data.alpaca.markets/stream",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()