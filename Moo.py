import numpy as np
import matplotlib.pyplot as plt

# Parameters (you can slightly tweak if needed)
Vth = 0.6          # Threshold voltage (V)
mu = 200e-4        # Mobility (m^2/Vs)
Cox = 1e-2         # Oxide capacitance (F/m^2)
W = 1e-6           # Width (m)
L = 1e-6           # Length (m)
Vds = 1.0          # Drain voltage (V)

# Gate voltage range
Vg = np.linspace(0, 2, 100)

# Initialize current
Id = []

for vg in Vg:
    if vg < Vth:
        # Subthreshold region (exponential)
        Id.append(1e-12 * np.exp((vg - Vth) / 0.1))
    else:
        # Saturation region (quadratic MOSFET equation)
        Id.append(0.5 * mu * Cox * (W/L) * (vg - Vth)**2)

Id = np.array(Id)

# Plot
plt.figure()
plt.semilogy(Vg, Id, linewidth=2)
plt.xlabel("Gate Voltage (Vg)")
plt.ylabel("Drain Current (Id)")
plt.title("Transfer Characteristics (Id-Vg) of 2D MOSFET Biosensor")
plt.grid(True)
plt.show()