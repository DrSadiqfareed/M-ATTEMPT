# -*- coding: utf-8 -*-
"""M-ATTEMPT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FTw5-j47ruWDHShAMkEU_N9bHbur_uK4
"""

import random
import math
import matplotlib.pyplot as plt

class Node:
    def __init__(self, node_id, x, y, energy, data_rate):
        self.node_id = node_id
        self.x = x
        self.y = y
        self.energy = energy
        self.data_rate = data_rate
        self.is_sink = False
        self.parent = None
        self.children = []
        self.temperature = 25  # Initial temperature in degrees Celsius

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Network:
    def __init__(self, num_nodes, field_size):
        self.nodes = []
        self.sink = Node("Sink", field_size // 2, field_size // 2, float('inf'), float('inf'))
        self.sink.is_sink = True
        self.field_size = field_size
        self.num_nodes = num_nodes
        self.create_nodes()
        self.routes = []
        self.active_nodes = []
        self.total_energy = []
        self.throughput = []

    def create_nodes(self):
        for i in range(self.num_nodes):
            x, y = random.randint(0, self.field_size), random.randint(0, self.field_size)
            energy = random.uniform(1, 10)  # Random energy between 1 and 10J
            data_rate = random.randint(50, 1000)  # Data rate in Kbps
            node = Node(f"Node-{i}", x, y, energy, data_rate)
            self.nodes.append(node)

    def initialize_routes(self):
        for node in self.nodes:
            if node.distance_to(self.sink) <= 10:
                node.parent = self.sink
                self.sink.children.append(node)
            else:
                nearest = min(self.nodes, key=lambda n: n.distance_to(node) if n != node else float('inf'))
                node.parent = nearest
                nearest.children.append(node)

    def simulate_round(self):
        packets_delivered = 0
        total_energy = sum(node.energy for node in self.nodes if node.energy > 0)

        for node in self.nodes:
            if node.energy <= 0:
                continue  # Skip dead nodes

            # Check temperature thresholds
            if node.temperature > 50:
                node.parent.children.remove(node)
                node.parent = None
                continue

            # Data transmission
            if node.parent:
                distance = node.distance_to(node.parent)
                energy_used = self.calculate_energy(distance, node.data_rate)
                if node.energy >= energy_used:
                    node.energy -= energy_used
                    node.parent.energy -= energy_used * 0.1  # Reception cost
                    packets_delivered += 1

            # Mobility simulation
            if random.random() < 0.05:  # 5% chance of moving
                node.x = random.randint(0, self.field_size)
                node.y = random.randint(0, self.field_size)
                self.reconnect_node(node)

        self.active_nodes.append(len([node for node in self.nodes if node.energy > 0]))
        self.total_energy.append(total_energy)
        self.throughput.append(packets_delivered)

    def calculate_energy(self, distance, data_rate):
        e_elec = 50e-9  # Energy for processing per bit (J/bit)
        e_amp = 100e-12  # Energy for amplification (J/bit/m^2)
        return data_rate * (e_elec + e_amp * (distance ** 2))

    def reconnect_node(self, node):
        nearest = min(self.nodes + [self.sink], key=lambda n: n.distance_to(node) if n != node else float('inf'))
        if node.parent:
            node.parent.children.remove(node)
        node.parent = nearest
        nearest.children.append(node)

    def simulate(self, rounds):
        for r in range(rounds):
            self.simulate_round()

    def plot_results(self):
        rounds = list(range(len(self.active_nodes)))

        # Plot Active Nodes
        plt.figure(figsize=(10, 6))
        plt.plot(rounds, self.active_nodes, label="Active Nodes", color='blue')
        plt.xlabel("Rounds")
        plt.ylabel("Number of Active Nodes")
        plt.title("Network Stability Over Time")
        plt.legend()
        plt.grid(True)
        plt.show()

        # Plot Total Energy
        plt.figure(figsize=(10, 6))
        plt.plot(rounds, self.total_energy, label="Total Energy (J)", color='green')
        plt.xlabel("Rounds")
        plt.ylabel("Energy (Joules)")
        plt.title("Total Energy Remaining in Network")
        plt.legend()
        plt.grid(True)
        plt.show()

        # Plot Throughput
        plt.figure(figsize=(10, 6))
        plt.plot(rounds, self.throughput, label="Throughput (Packets)", color='orange')
        plt.xlabel("Rounds")
        plt.ylabel("Packets Delivered")
        plt.title("Throughput Over Time")
        plt.legend()
        plt.grid(True)
        plt.show()

# Main Simulation
network = Network(num_nodes=10, field_size=50)
network.initialize_routes()
network.simulate(rounds=100)
network.plot_results()