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

How to Run
Clone the repository:

bash
Copy code
git clone [https://github.com/yourusername/m-attempt-wbasn.git](https://github.com/DrSadiqfareed/M-ATTEMPT)
cd m-attempt-wbasn
Run the Python script:

bash
Copy code
python m_attempt_simulation.py
View the performance graphs generated during the simulation.

File Structure
plaintext
Copy code
.
├── m_attempt_simulation.py  # Main simulation script
├── README.md                # Documentation
Example Outputs
1. Active Nodes Over Time
Shows the number of operational nodes as the simulation progresses.


2. Total Energy Consumption
Tracks the remaining energy of the network during the simulation.


3. Throughput
Illustrates the successful delivery of packets to the sink node.


Contributing
Feel free to fork the repository and contribute enhancements! Create a pull request for review.

License
This project is licensed under the MIT License.

References
Original Research Paper: N. Javaid et al., "M-ATTEMPT: A New Energy-Efficient Routing Protocol for Wireless Body Area Sensor Networks," Procedia Computer Science, 2013. DOI: 10.1016/j.procs.2013.06.033
