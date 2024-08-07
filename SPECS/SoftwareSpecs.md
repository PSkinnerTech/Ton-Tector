# Ton-Tector Software Specifications

Ton-Tector integrates cutting-edge software solutions for blockchain integration and environmental monitoring. Below are the software specifications and key components:

## Operating System

- **OS Options:**
  - Ubuntu Server
  - Raspberry Pi OS (Lite)

## Node Software

- **TON Lightweight Node:**
  - Installation and configuration of the TON node software for lightweight operations
  - Synchronization with the TON blockchain network

## Sensor Drivers and Monitoring Scripts

### Temperature Monitoring

- **DHT22 Sensor Driver:**
  - Python libraries for interfacing with the DHT22 temperature sensor

- **Monitoring Script:**
  - Checks temperature readings and compares them against a defined dangerous threshold
  - Sends alerts via Telegram if dangerous temperatures are detected

### Seismic Activity Monitoring

- **ADXL345 Accelerometer Driver:**
  - Python libraries for interfacing with the ADXL345 accelerometer

- **Monitoring Script:**
  - Reads acceleration data and calculates the magnitude of seismic activity
  - Sends alerts via Telegram if dangerous seismic activity is detected

## Alert System

- **Telegram Integration:**
  - Telegram Bot API for sending alerts
  - Custom scripts to manage alert distribution based on user subscriptions

## User Subscription Management

- **Subscription Management System:**
  - Basic system for managing user subscriptions to specific locations and alert types
  - Python scripts for adding and removing subscriptions

## Security and Maintenance

- **Security Measures:**
  - SSH for secure remote access
  - Firewall configurations to protect the device and data

- **Automation:**
  - Scripts for automating node operations, including startup, monitoring, and maintenance tasks