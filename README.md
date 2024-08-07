
# Ton-Tector

![Ton-Tector Device](./img/ton-tector1.jpeg)

Ton-Tector is a revolutionary device combining blockchain technology with environmental monitoring. Designed to function as a lightweight node in The Open Network (TON) blockchain, Ton-Tector also serves as an early detection system for natural disasters. Equipped with sensors for temperature and seismic activity, it provides real-time alerts to users via a Telegram mini-app. This open-source project aims to provide accessible and reliable technology for safety and blockchain integration.

## Quick Links
- [Hardware Specifications](./SPECS/HardwareSpecs.md)
- [Software Specifications](./SPECS/SoftwareSpecs.md)

## Who I Am

My name is Patrick Skinner, and I'm the Lead DevRel for Forward Research | Arweave. I bring my experience as a former Paratrooper Medic to my work, driven by a passion for building blockchain technology that provides tangible benefits in real-world situations. I am dedicated to developing solutions that can truly help those in need, especially in critical scenarios. You can follow my work and updates on [GitHub](https://github.com/PSkinnerTech), [X](https://x.com/PSkinnerTech).

## Use Case

### Problem Statement
Natural disasters such as earthquakes and extreme temperature fluctuations can cause significant harm to communities, often with little to no warning. There is a need for a reliable, real-time monitoring system that can alert individuals and authorities promptly, allowing for quicker response times and potentially saving lives.

### Solution
Ton-Tector addresses this problem by combining advanced sensor technology with the reliability of blockchain. It continuously monitors environmental conditions and immediately alerts users to any anomalies via a Telegram mini-app. Additionally, by functioning as a lightweight node on the TON blockchain, it ensures data integrity and leverages the decentralized nature of the network for robustness and security.

### How It Works
1. **Sensor Monitoring:** Ton-Tector uses DHT22 sensors for temperature detection and ADXL345 accelerometers for seismic activity monitoring.
2. **Data Processing:** The Raspberry Pi 4 processes the sensor data and determines if the readings indicate a potential natural disaster.
3. **Blockchain Integration:** The processed data is then logged on the TON blockchain, ensuring immutability and transparency.
4. **Real-Time Alerts:** If a potential natural disaster is detected, the device sends an immediate alert to users via a Telegram mini-app.
5. **User Interaction:** Users can subscribe to the Telegram bot to receive real-time updates and alerts directly on their mobile devices.

Absolutely, here’s the continuation and completion of the README file:

---

## System Architecture

### Hardware Components
- **Raspberry Pi 4 Model B**: Acts as the central processing unit.
- **DHT22 Temperature Sensor**: Measures environmental temperature.
- **ADXL345 Accelerometer**: Detects seismic activity.
- **1TB SSD**: Provides ample storage for data logging and blockchain interaction.
- **Active Cooling Solution**: Ensures optimal performance of the Raspberry Pi.

### Software Components
- **Raspberry Pi OS**: The operating system for the Raspberry Pi.
- **Python Scripts**: Handle sensor data collection and processing.
- **Flask Framework**: Hosts the backend for the Telegram bot.
- **TON Blockchain Node Software**: Enables the Raspberry Pi to function as a lightweight node.
- **Telegram Bot API**: Facilitates communication with users via the Telegram mini-app.

### Folder Structure
```
/Ton-Tector
    /img
    /SPECS
    /Ton-Tector # Raspberry Pi
        /config
        /data
        /logs
        /src
    /TT-TG-App # Telegram App
        /venv
        app.py
        config.py
        requirements.txt
        set_webhook.py
```

### Detailed Workflow
1. **Sensor Data Collection**:
    - The `DHT22` sensor measures temperature and the `ADXL345` sensor detects seismic activity.
    - Sensor data is read by Python scripts running on the Raspberry Pi.

2. **Data Processing**:
    - The collected data is analyzed to identify significant deviations indicating potential natural disasters.
    - Processed data is logged locally and prepared for blockchain entry.

3. **Blockchain Integration**:
    - Data is sent to the TON blockchain node software on the Raspberry Pi.
    - The node validates and logs the data, ensuring immutability and transparency.

4. **Real-Time Alerts**:
    - The Flask application interacts with the Telegram Bot API.
    - When abnormal sensor data is detected, an alert is sent through the Telegram bot to all subscribed users.

5. **User Interaction**:
    - Users subscribe to the bot via Telegram to receive updates.
    - The bot provides real-time alerts and status updates on environmental conditions.

## Open Source

Ton-Tector is an open-source project designed to encourage community collaboration and innovation. We welcome contributions from developers and enthusiasts alike to help improve and expand the capabilities of this project. By leveraging the collective expertise of the community, we aim to create a robust and reliable system for monitoring environmental conditions and issuing timely alerts. Your contributions can make a real difference in advancing this technology.

## License

This project is licensed under the MIT License, allowing for open use, modification, and distribution. This permissive license ensures that Ton-Tector remains accessible to everyone, fostering a spirit of collaboration and continuous improvement. For more details, please refer to the LICENSE file in the project's repository.