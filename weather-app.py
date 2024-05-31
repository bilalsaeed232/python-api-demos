import tkinter as tk
from weatherapi import get_weather_forecasts

# Create the main window
root = tk.Tk()
root.title("Hello World App")

# Set the size of the window
root.geometry("800x600")

# Configure the grid
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

api_key = "3683120ad1mshed60f81472ffd44p1c4a52jsn4b64d7d61d0e"
location = "aachen"
forecasts = get_weather_forecasts(location, api_key)

detailed_weather = ""
for forecast in forecasts:
    detailed_weather = f"{detailed_weather}\n{forecast["day"]} : \t (High: {forecast["high"]}, Low: {forecast["low"]}) {forecast["text"]}"

print(detailed_weather)
# Create a label widget with the text "Hello, World!"
label = tk.Label(root, text=str(detailed_weather), font=("Helvetica", 16))

# Position the label in the center of the grid
label.grid(row=0, column=0, sticky="nsew")

# Run the application
root.mainloop()

