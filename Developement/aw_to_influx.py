# File: aw_to_influx.py
import requests
from influxdb import InfluxDBClient
import socket

INFLUX_HOST = "13.13.1.65"     # your server IP
INFLUX_PORT = 8086
INFLUX_DB = "activitywatch"
AW_SERVER = "http://localhost:5600/api/0"

hostname = socket.gethostname()
client = InfluxDBClient(host=INFLUX_HOST, port=INFLUX_PORT)
client.switch_database(INFLUX_DB)

buckets = requests.get(f"{AW_SERVER}/buckets").json()

for bucket in buckets:
    bid = bucket["id"]
    try:
        events = requests.get(f"{AW_SERVER}/buckets/{bid}/events").json()["events"]
        for e in events[-50:]:  # Only last 50 events
            json_body = [{
                "measurement": "aw_usage",
                "tags": {
                    "bucket": bid,
                    "machine": hostname
                },
                "time": e["timestamp"],
                "fields": {
                    "duration": e["duration"],
                    "event_data": str(e["data"])
                }
            }]
            client.write_points(json_body)
    except Exception as ex:
        print(f"Failed to export {bid}: {ex}")
