# route_clearance_map/map_simulator.py

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time

# Simulated intersections on a 2D map
intersections = {
    "A": (1, 1),
    "B": (3, 1),
    "C": (5, 1),
    "D": (1, 3),
    "E": (3, 3),
    "F": (5, 3),
    "G": (1, 5),
    "H": (3, 5),
    "I": (5, 5),
}

# Predefined ambulance path
ambulance_path = ["G", "H", "E", "B", "C"]

def draw_map(active_path):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)
    ax.set_aspect('equal')
    ax.set_title("Ambulance Route Clearance Map")

    # Draw intersections
    for name, (x, y) in intersections.items():
        color = 'green' if name in active_path else 'red'
        circle = plt.Circle((x, y), 0.2, color=color)
        ax.add_patch(circle)
        ax.text(x, y + 0.3, name, ha='center', fontsize=10)

    # Draw roads
    roads = [
        ("A", "B"), ("B", "C"),
        ("D", "E"), ("E", "F"),
        ("G", "H"), ("H", "I"),
        ("A", "D"), ("D", "G"),
        ("B", "E"), ("E", "H"),
        ("C", "F"), ("F", "I")
    ]
    for start, end in roads:
        x1, y1 = intersections[start]
        x2, y2 = intersections[end]
        ax.plot([x1, x2], [y1, y2], 'gray')

    plt.grid(True)
    plt.pause(0.5)
    plt.show()

if __name__ == "__main__":
    print("[INFO] Simulating ambulance route...")
    for i in range(1, len(ambulance_path)+1):
        draw_map(ambulance_path[:i])
        time.sleep(1)
