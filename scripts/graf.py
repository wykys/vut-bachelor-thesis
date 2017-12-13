#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

fn = 37.9e3
Tn = 1/fn
n = [] # nosna

IR_TIM_START_PULS   = 5000,
IR_TIM_START_SPACE  = IR_TIM_START_PULS,
IR_TIM_DATA_PULS    = 600,
IR_TIM_DATA0_SPACE  = IR_TIM_DATA_PULS,
IR_TIM_DATA1_SPACE  = IR_TIM_DATA0_SPACE*2,
IR_TIM_END_PULS     = 3000,
IR_TIM_PACKET_SPACE = 30000,
IR_TIM_TOLERANCE    = 250

t = np.arange(0, 82.6e-3, Tn)
for i in range(len(t)):
    n.append(i%2)

n = np.array(n)
t = np.array(t) * 1e6
d = []

puls = 0
for i in t:
    if i < 5000:
        d.append(1)
    elif i < 10000:
        d.append(0)
    elif puls < 24 and i < 10000 + 600 * (puls + 1) + 1200 * puls:
        d.append(1)
    elif puls < 24 and i < 10000 + 600 * (puls + 1) + 1200 * (puls + 1):
        d.append(0)
    elif puls == 24 and i < 10000 + 600 * (puls + 1) + 1200 * (puls + 1) + 3000:
        d.append(1)
    elif puls == 24:
        d.append(0)
    else:
        puls += 1
        d.append(1)

d = np.array(d)
v = n * d

plt.subplot(411)
plt.step(t/1000, n*5, 'k', linewidth=1.5)
plt.grid(True)
plt.xlim([0,3])
plt.title('Detail nosného signálu 37,9 kHz')
plt.xlabel('$t$ [$\mu s$]')
plt.ylabel('U [V]')

plt.subplot(412)
plt.step(t/1000, d*5, 'b', linewidth=1.5)
plt.grid(True)
plt.xlim([0,82.600])
plt.title('Modulační signál na vstupu hradla AND')
plt.xlabel('$t$ [$\mu s$]')
plt.ylabel('U [V]')

plt.subplot(413)
plt.step(t/1000, v, 'r', linewidth=1.5)
plt.grid(True)
plt.xlim([0,82.600])
plt.title('Modulovaný signál vysílaný IR LED')
plt.xlabel('$t$ [$\mu s$]')
plt.ylabel('nesvítí       svítí')

plt.subplot(414)
plt.step(t/1000, (-1*d*5 + 5), 'g', linewidth=1.5)
plt.grid(True)
plt.xlim([0,82.600])
plt.title('Demodulovaný signál na výstupu detektoru')
plt.xlabel('$t$ [$\mu s$]')
plt.ylabel('U [V]')
plt.show()
