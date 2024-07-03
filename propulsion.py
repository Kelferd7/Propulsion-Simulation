import numpy as np
import matplotlib.pyplot as plt

# Constants/Inputs
massFlowRate = 100  # kg/s
exitVelocity = 300  # m/s
initialVelocity = 100  # m/s
exitArea = 0.1  # m^2
exitPressure = 100000  # Pa
ambientPressure = 101325  # Pa

# Time parameters
time = np.linspace(0, 100, 500)  # 100 seconds, 500 intervals

# Thrust Calculation
thrust = massFlowRate * (exitVelocity - initialVelocity) + exitArea * (exitPressure - ambientPressure)

# Simplified Fuel Consumption
fuelConsumptionRate = 0.5  # kg/s
fuelConsumption = fuelConsumptionRate * time

# Plotting the results
plt.figure(figsize=(10, 5))

# Thrust vs Time plot
plt.subplot(1, 2, 1)
plt.plot(time, thrust * np.ones_like(time), label='Thrust')
plt.xlabel('Time (s)')
plt.ylabel('Thrust (N)')
plt.title('Thrust vs Time')
plt.legend()

#Fuel Consumption vs Time plot
plt.subplot(1, 2, 2)
plt.plot(time, fuelConsumption, label='Fuel Consumption', color='orange')
plt.xlabel('Time (s)')
plt.ylabel('Fuel Consumed (kg)')
plt.title('Fuel Consumption vs Time')
plt.legend()

plt.tight_layout()
plt.show()

