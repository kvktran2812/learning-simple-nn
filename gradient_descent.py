def L(w, b):
    return 32.8 - 24.613*w - 10.96*b + (14/3)*w**2 + 4*w*b + b**2

def dLdw(w, b):
    return -24.613 + (28/3) * w + 4*b

def dLdb(w, b):
    return -10.96 + 4*w + w*b

x = [1.0, 2.0, 3.0]
y = [3.33, 5.77, 7.35]

import matplotlib.pyplot as plt

w0 = 0
b0 = 0
learning_rate = 0.01

dw = dLdw(w0, b0)
db = dLdb(w0, b0)

w = [w0]
b = [b0]
dw_hist = [dw]
db_hist = [db]

for i in range(1000):
    old_w = w[-1]
    old_b = b[-1]
    new_w = old_w - learning_rate * dw
    new_b = old_b - learning_rate * db
    dw = dLdw(new_w, new_b)
    db = dLdb(new_w, new_b)

    # append
    w.append(new_w)
    b.append(new_b)
    dw_hist.append(dw)
    db_hist.append(db)

import numpy as np
import matplotlib.animation as animation

X = np.array(x)
Y = np.array(y)

fig, ax = plt.subplots()
ax.scatter(X, Y, color='blue', alpha=0.5, label="Data points")
line, = ax.plot(X, w0 * X + b0, 'r-', linewidth=2, label="Regression Line")
ax.legend()

# Animation function
def update(frame):
    line.set_ydata(w[frame] * X + b[frame])  # Update line equation
    return line,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(w), interval=500, blit=True)

# Show animation
plt.show()