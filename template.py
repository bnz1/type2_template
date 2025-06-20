""" Type 2 entry template """
import numpy as np
import matplotlib.pyplot as plt

""" STAGE 1 (find contact points) """
# TODO: Find contact points

CONTACT_LEFT = 1
CONTACT_RIGHT = 2

""" STAGE 2 (find first number) """
# TODO: Fill in AWL contact point entries
awl = np.array([
    (0, 0, 0),
    (2, 0, 0),
    (4, 0, 0),
    (6, 0, 0),
    (8, 0, 0),
    (10, 0, 0),
    (12, 0, 0),
    (14, 0, 0),
    (16, 0, 0),
    (18, 0, 0),
    (20, 0, 0),
    (22, 0, 0),
    (24, 0, 0),
    (26, 0, 0),
    (28, 0, 0),
    (30, 0, 0),
    (32, 0, 0),
    (34, 0, 0),
    (36, 0, 0),
    (38, 0, 0),
    (40, 0, 0),
    (42, 0, 0),
    (44, 0, 0),
    (46, 0, 0),
    (48, 0, 0),
    (50, 0, 0),
    (52, 0, 0),
    (54, 0, 0),
    (56, 0, 0),
    (58, 0, 0),
    (60, 0, 0),
    (62, 0, 0),
    (64, 0, 0),
    (66, 0, 0),
    (68, 0, 0),
    (70, 0, 0),
    (72, 0, 0),
    (74, 0, 0),
    (76, 0, 0),
    (78, 0, 0),
    (80, 0, 0),
    (82, 0, 0),
    (84, 0, 0),
    (86, 0, 0),
    (88, 0, 0),
    (90, 0, 0),
    (92, 0, 0),
    (94, 0, 0),
    (96, 0, 0),
    (98, 0, 0),
    (100, 0, 0),
])

# Generate AWL plot
x = awl[:, 0]
y_left = awl[:, 1]
y_right = awl[:, 2]

fig, ax1 = plt.subplots()

ax1.plot(x, y_left, marker='o', color='tab:blue', label='left')
ax1.set_xlabel('start position')
ax1.set_ylabel('Left contact', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.plot(x, y_right, marker='s', color='tab:red', label='right')
ax2.set_ylabel('Right contact', color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

plt.title('AWL contact points')
fig.tight_layout()
plt.savefig('awl.png')
# plt.show()

# TODO: Find wheel number (high test)
# E.g. if target is "41", use following formula:
# R51 L41 L41 (3 rev R then to 51, 2 rev L then to 41)
# L41 R51 L41 (3 rev L then to 41, 2 rev R then to 51, 1 rev L then to 41)
# L41 L41 R51 (3 rev L then to 41, 1 rev R then to 51)

# W1: ___ ___ ___ Width: ___
# W2: ___ ___ ___ Width: ___
# W3: ___ ___ ___ Width: ___

""" STAGE 3 (find second number) """
