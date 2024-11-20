# M-ATTEMPT: Energy-Efficient Routing Protocol for WBASNs

This project implements the **M-ATTEMPT (Mobility-supporting Adaptive Threshold-based Thermal-aware Energy-efficient Multi-hop Protocol)**, designed for **Wireless Body Area Sensor Networks (WBASNs)**. M-ATTEMPT combines Single-hop and Multi-hop communication to optimize energy consumption, handle node mobility, and ensure reliable data transmission for applications like patient monitoring and real-time feedback.

---

## Features

- **Hybrid Communication**:
  - Single-hop for real-time and emergency data.
  - Multi-hop for normal data delivery.
- **Thermal Awareness**:
  - Detects and avoids "hot spots" caused by overheating sensor nodes.
- **Mobility Support**:
  - Dynamically reconnects nodes when links break due to body movement.
- **Energy Optimization**:
  - Calculates energy consumption for both Single-hop and Multi-hop routing.
- **Performance Metrics**:
  - Tracks network stability, total energy, and throughput over simulation rounds.

---

## Visualizations

The simulation provides real-time graphs to monitor the protocol's performance:

1. **Network Stability**: Number of active nodes over time.
2. **Energy Consumption**: Total energy remaining in the network.
3. **Throughput**: Successfully delivered packets to the sink.

---

## Installation and Usage

### Prerequisites

- Python 3.7 or higher
- Required Python libraries:
  - `matplotlib`

Install dependencies using:
```bash
pip install matplotlib
