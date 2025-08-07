import matplotlib.pyplot as plt
import time

# Predefined intersection coordinates (X, Y)
intersections = {
    "A": (1, 1), "B": (3, 1), "C": (5, 1),
    "D": (1, 3), "E": (3, 3), "F": (5, 3),
    "G": (1, 5), "H": (3, 5), "I": (5, 5),
}

# Define road connections
roads = [
    ("A", "B"), ("B", "C"),
    ("D", "E"), ("E", "F"),
    ("G", "H"), ("H", "I"),
    ("A", "D"), ("D", "G"),
    ("B", "E"), ("E", "H"),
    ("C", "F"), ("F", "I")
]

# Predefined ambulance path
default_ambulance_path = ["G", "H", "E", "B", "C"]

def draw_map(active_path, save=False, step=0):
    """
    Draws the map with current active ambulance path.

    Parameters:
    - active_path (list): List of intersection names (e.g., ['G', 'H']).
    - save (bool): If True, saves the plot as an image.
    - step (int): Step index (used in filename if save=True).
    """
    plt.clf()  # Clear previous plot
    fig, ax = plt.subplots()
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)
    ax.set_aspect('equal')
    ax.set_title("Ambulance Route Clearance Map")

    # Plot intersections
    for name, (x, y) in intersections.items():
        color = 'green' if name in active_path else 'red'
        circle = plt.Circle((x, y), 0.2, color=color)
        ax.add_patch(circle)
        ax.text(x, y + 0.3, name, ha='center', fontsize=10)

    # Plot roads
    for start, end in roads:
        x1, y1 = intersections[start]
        x2, y2 = intersections[end]
        ax.plot([x1, x2], [y1, y2], color='gray')

    plt.grid(True)
    plt.pause(0.001)  # Allow GUI event loop to process

    if save:
        plt.savefig(f"step_{step:02d}.png")

def simulate_route(path=None, delay=1.0, save_images=False):
    """
    Simulates the ambulance moving along a path.

    Parameters:
    - path (list): Custom path or use default.
    - delay (float): Delay between steps (in seconds).
    - save_images (bool): If True, saves each step as an image.
    """
    if path is None:
        path = default_ambulance_path

    print("[INFO] Simulating ambulance route...")
    plt.ion()  # Turn on interactive mode
    for i in range(1, len(path) + 1):
        draw_map(path[:i], save=save_images, step=i)
        time.sleep(delay)
    plt.ioff()  # Turn off interactive mode
    plt.show()

if __name__ == "__main__":
    simulate_route()
