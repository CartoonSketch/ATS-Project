# traffic_signal_gui.py

import tkinter as tk
from tkinter import messagebox
import requests

SERVER_URL = "http://127.0.0.1:5000"

class TrafficSignalGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Smart Traffic Signal Controller")
        self.master.geometry("400x300")

        self.signal_status = tk.StringVar()
        self.signal_status.set("NORMAL TRAFFIC MODE")

        self.status_label = tk.Label(master, textvariable=self.signal_status, font=("Helvetica", 14), fg="green")
        self.status_label.pack(pady=20)

        self.ambulance_button = tk.Button(master, text="🚑 Ambulance Detected", command=self.ambulance_detected, bg="red", fg="white", height=2, width=20)
        self.ambulance_button.pack(pady=10)

        self.reset_button = tk.Button(master, text="🔄 Reset to Normal", command=self.reset_signal, bg="blue", fg="white", height=2, width=20)
        self.reset_button.pack(pady=10)

    def ambulance_detected(self):
        self.signal_status.set("AMBULANCE DETECTED - CLEAR PATH")
        self.status_label.config(fg="red")
        try:
            requests.post(f"{SERVER_URL}/update_detection", json={"detected": True})
            requests.post(f"{SERVER_URL}/update_signal", json={"signal": "RED"})
            messagebox.showinfo("Signal Update", "All signals turned RED except ambulance path.")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to update server:\n{e}")

    def reset_signal(self):
        self.signal_status.set("NORMAL TRAFFIC MODE")
        self.status_label.config(fg="green")
        try:
            requests.post(f"{SERVER_URL}/update_detection", json={"detected": False})
            requests.post(f"{SERVER_URL}/update_signal", json={"signal": "GREEN"})
            messagebox.showinfo("Signal Update", "Traffic signals reset to normal mode.")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to update server:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficSignalGUI(root)
    root.mainloop()
