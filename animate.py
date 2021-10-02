import numpy as np
from matplotlib import animation
import matplotlib.pyplot as plt

# Funciones de «x» y «y» #
# x(t) con opcion de cambiar amplitudes y omega
def x(time, amplitude=15, omega=3):
    return amplitude*np.cos(omega*time)

# y(t) con opcion de cambiar amplitudes, omega y psi
def y(time, amplitude=15, omega=3, phi=0):
    return amplitude*np.cos(omega*time-phi)

# Generando graficas #
# Subplots
fig, ax = plt.subplots(1)
# Set limits
ax.set_aspect('equal')
ax.set_xlim(left=-15, right=15)
ax.set_ylim(bottom=-15, top=15)

# Haciendo cada plot
line, = ax.plot([], [])

# Datos para correr
data = [i for i in range(360+1)]

# Funcion para crear la animación
def animate(i):
    ax.set_title(f"$\phi={i}°$")
    t = np.linspace(-10, 10, 1000)
    xt = x(t)
    yt = y(t,phi=i*np.pi/180)
    line.set_data(xt, yt)
    return line,

# Animador
anim = animation.FuncAnimation(fig, animate, frames=data, interval=16, repeat=False)

anim.save('basic_animation.mp4', fps=30)

plt.show()

# EOF #