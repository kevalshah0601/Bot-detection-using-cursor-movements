import numpy as np
import matplotlib.pyplot as plt
import time

sqrt3 = np.sqrt(3)
sqrt5 = np.sqrt(5)

def wind_mouse(start_x, start_y, dest_x, dest_y, num_data_points, G_0=9, W_0=3, M_0=15, D_0=12, delta_t=0.01, interval=3.0):
    '''
    WindMouse algorithm. Returns x and y arrays, and plots the movement graph.
    G_0 - magnitude of the gravitational force
    W_0 - magnitude of the wind force fluctuations
    M_0 - maximum step size (velocity clip threshold)
    D_0 - distance where wind behavior changes from random to damped
    delta_t - time interval to record data (default: 0.01 seconds)
    interval - time interval to start a new line in the arrays (default: 3.0 seconds)
    '''
    current_x, current_y = start_x, start_y
    v_x = v_y = W_x = W_y = 0

    while (dist := np.hypot(dest_x - start_x, dest_y - start_y)) >= 1:
        W_mag = min(W_0, dist)
        if dist >= D_0:
            W_x = W_x / sqrt3 + (2 * np.random.random() - 1) * W_mag / sqrt5
            W_y = W_y / sqrt3 + (2 * np.random.random() - 1) * W_mag / sqrt5
        else:
            W_x /= sqrt3
            W_y /= sqrt3
            if M_0 < 3:
                M_0 = np.random.random() * 3 + 3
            else:
                M_0 /= sqrt5
        v_x += W_x + G_0 * (dest_x - start_x) / dist
        v_y += W_y + G_0 * (dest_y - start_y) / dist
        v_mag = np.hypot(v_x, v_y)
        if v_mag > M_0:
            v_clip = M_0 / 2 + np.random.random() * M_0 / 2
            v_x = (v_x / v_mag) * v_clip
            v_y = (v_y / v_mag) * v_clip
        start_x += v_x
        start_y += v_y

        if num_data_points < interval/delta_t:
            x_values.append(int(start_x))
            y_values.append(int(start_y))
            num_data_points += 1

        else:
          break

    if(num_data_points < interval/delta_t):
      start_x = dest_x
      start_y = dest_y
      dest_x  = np.random.randint(low_x,high_x)
      dest_y  = np.random.randint(low_y,high_y)

      wind_mouse(start_x, start_y, dest_x, dest_y, num_data_points)

    return x_values, y_values

n_cycles = 1
low_x = 0
low_y = 0
high_x = 1920
high_y = 1080

x_string = ''
y_string = ''

for i in range(3,0,-1):
   print(f"Starting in {i}.....")
   time.sleep(1)

for i in range(n_cycles):

  start_x  = np.random.randint(low_x,high_x)
  start_y  = np.random.randint(low_y,high_y)
  end_x  = np.random.randint(low_x,high_x)
  end_y  = np.random.randint(low_y,high_y)

  x_values = []
  y_values = []
  num_data_points = 0

  x_values, y_values = wind_mouse(start_x, start_y, end_x, end_y, num_data_points)

  for x in x_values:
    x_string += str(x) + ' '
  x_string += '\n'

  for y in y_values:
    y_string += str(y) + ' '
  y_string += '\n'

with open('x_test.txt', 'w') as filex:
  filex.write(x_string)

with open('y_test.txt', 'w') as filey:
  filey.write(y_string)

time.sleep(1)