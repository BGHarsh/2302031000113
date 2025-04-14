import matplotlib.pyplot as plt

# Days of the week
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Sample temperature data (°C)
temperatures = [34, 40, 39, 42, 37, 35, 41]

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(days, temperatures, marker='o', color='royalblue', linestyle='-', linewidth=2)

# Add titles and labels
plt.title("🌤 Weekly Temperature Overview", fontsize=14)
plt.xlabel("Day", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
