from pymavlink import mavutil

master = mavutil.mavlink_connection("udp:127.0.0.1:14550")
master.wait_heartbeat()
print("Connected. Listening for STATUSTEXT...\n")

while True:
    msg = master.recv_match(type="STATUSTEXT", blocking=True)
    if msg:
        text = msg.text.decode(errors="ignore") if isinstance(msg.text, bytes) else msg.text
        print(text)
