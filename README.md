# Ton-Tector

Early-detection IoT system for natural disasters — a Raspberry Pi 4 sensor node that monitors temperature and seismic activity, processes readings on-device, and pushes real-time alerts to subscribers through a Telegram bot.

Built to give individuals and authorities earlier warning of earthquakes, dangerous temperature swings, and similar environmental anomalies, with an immutable on-chain audit log for the alert history.

![Ton-Tector Device](./img/ton-tector1.jpeg)

## Quick links

- [Hardware Specifications](./SPECS/HardwareSpecs.md)
- [Software Specifications](./SPECS/SoftwareSpecs.md)

## Why this exists

Natural disasters — earthquakes, extreme heat events, wildfire-driving heat waves — often arrive with little warning. Communities, schools, and businesses near fault lines or in vulnerable climates need real-time monitoring that is cheap to deploy, simple to operate, and trustworthy after the fact.

Ton-Tector combines off-the-shelf sensors with a Raspberry Pi 4 to produce a self-contained early-detection node. Alerts are pushed instantly to a Telegram mini-app, and a tamper-evident log of every alert is written to a public ledger for after-the-fact analysis and accountability.

## How it works

1. **Sensor monitoring** — DHT22 for temperature, ADXL345 accelerometer for seismic activity, sampled continuously by the Pi.
2. **On-device processing** — Python scripts analyze the readings, smooth them, and flag anomalies that exceed configured thresholds.
3. **Real-time alerts** — A Flask backend triggers the Telegram Bot API, pushing alerts to every subscribed user within seconds.
4. **Immutable audit log** — Each alert is recorded on the TON blockchain (used as a tamper-evident append-only log), so the alert history can be independently verified after an incident.
5. **User interaction** — Anyone can subscribe to the Telegram bot to receive alerts and live status updates.

> The on-chain log is the *audit layer*, not the alerting path. Alerts reach users via Telegram in real time and do not depend on chain finality.

## System architecture

### Hardware

- **Raspberry Pi 4 Model B** — central processing unit
- **DHT22 temperature sensor** — environmental temperature
- **ADXL345 accelerometer** — seismic activity
- **1 TB SSD** — local data storage and node state
- **Active cooling** — sustained-load reliability

### Software

- **Raspberry Pi OS** — host operating system
- **Python sensor pipeline** — reads, smooths, and classifies readings
- **Flask backend** — hosts the Telegram bot webhook
- **Telegram Bot API** — alert delivery to subscribed users
- **TON node software** — append-only audit log for alerts

### Folder layout

```
/Ton-Tector
    /img
    /SPECS
    /Ton-Tector        # Raspberry Pi services
        /config
        /data
        /logs
        /src
    /TT-TG-App         # Telegram bot
        /venv
        app.py
        config.py
        requirements.txt
        set_webhook.py
```

## Detailed workflow

**1. Sensor collection**
DHT22 measures temperature; ADXL345 measures three-axis acceleration. Python services on the Pi sample both at a configurable cadence.

**2. Data processing**
Readings are smoothed and compared against configured thresholds. Significant deviations are classified as candidate events.

**3. Alerting**
For any candidate event, the Flask app invokes the Telegram Bot API to push an alert to all subscribed users immediately.

**4. Audit log**
The same event is written to the TON node so the alert history is tamper-evident.

**5. User interaction**
Users subscribe through the Telegram mini-app and receive both alerts and periodic status pings.

## Where to take it next

- **Multi-sensor fusion** — add CO2, particulate (SDS011), gas (MQ-series), and barometric pressure for broader hazard coverage
- **Edge ML** — train a small classifier on accelerometer windows to separate real seismic events from foot traffic, doors, and vehicles
- **Mesh of nodes** — correlate detections across nearby Pis to filter false positives
- **Alternative log backends** — swap the audit log for S3 + object-lock, IPFS, or any append-only store

## Open source

Ton-Tector is open source and welcomes contributions — sensor adapters, edge-ML models, alternate alert transports, and better thresholds for specific climates and geographies are all wanted.

## License

MIT — see `LICENSE`.
