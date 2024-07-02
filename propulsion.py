import numpy as np
import matplotlib.pyplot as plt

# Constants/Inputs
mass_flow_rate = 100  # kg/s
exit_velocity = 300  # m/s
initial_velocity = 100  # m/s
exit_area = 0.1  # m^2
exit_pressure = 100000  # Pa
ambient_pressure = 101325  # Pa

# Time parameters
time = np.linspace(0, 100, 500)  # 100 seconds, 500 intervals

# Thrust Calculation
thrust = mass_flow_rate * (exit_velocity - initial_velocity) + exit_area * (exit_pressure - ambient_pressure)

# Simplified Fuel Consumption
fuel_consumption_rate = 0.5  # kg/s
fuel_consumption = fuel_consumption_rate * time

# Plotting the results
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(time, thrust * np.ones_like(time), label='Thrust')
plt.xlabel('Time (s)')
plt.ylabel('Thrust (N)')
plt.title('Thrust vs Time')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(time, fuel_consumption, label='Fuel Consumption', color='orange')
plt.xlabel('Time (s)')
plt.ylabel('Fuel Consumed (kg)')
plt.title('Fuel Consumption vs Time')
plt.legend()

plt.tight_layout()
plt.show()

