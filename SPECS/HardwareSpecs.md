# Ton-Tector Hardware Specifications

Ton-Tector is built using reliable hardware components designed for optimal performance and durability. Below are the detailed specifications:

## Core Components

- **Raspberry Pi 4 Model B**
  - **CPU:** Quad-core Cortex-A72 (ARM v8) 64-bit SoC @ 1.5GHz
  - **RAM:** 8GB LPDDR4-3200 SDRAM
  - **Storage:** 1TB SSD (connected via USB 3.0)
  - **OS:** Ubuntu Server or Raspberry Pi OS (Lite)
  - **Power Supply:** 5V/3A USB-C power supply
  - **Cooling:** Active cooling solution (fan or heatsink)

## Temperature Detection

- **DHT22 (AM2302) Temperature Sensor**
  - **Accuracy:** ±0.5°C
  - **Temperature Range:** -40°C to +80°C
  - **Interface:** Digital signal
  - **Power Supply:** 3.3V or 5V
  - **Additional Components:** 10kΩ pull-up resistor for data line

## Seismic Activity Detection

- **ADXL345 Accelerometer**
  - **Type:** 3-axis digital accelerometer
  - **Sensitivity:** 3.9 mg/LSB
  - **Range:** ±2g, ±4g, ±8g, ±16g (selectable)
  - **Interface:** I2C or SPI
  - **Power Supply:** 3.3V
  - **Additional Components:** Logic level converter if necessary

## Additional Components

- **MicroSD Card:** At least 32GB (for OS and initial setup)
- **USB to SATA Adapter:** For connecting SSD to Raspberry Pi
- **Enclosure:** Custom or commercial case for housing the device
- **GPIO Breakout Board:** For easy connection of multiple sensors
- **Connecting Cables and Jumpers:** For sensor connections and power supply
- **UPS or Battery Backup:** Optional, for continuous operation during power outages