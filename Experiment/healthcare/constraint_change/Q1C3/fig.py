import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter
import numpy as np

plt.rc('text', usetex=True)
plt.rc('font', family='serif')


sns.set_palette("Paired")
# sns.set_palette("deep")
sns.set_context("poster", font_scale=2)
sns.set_style("whitegrid")
# sns.palplot(sns.color_palette("deep", 10))
# sns.palplot(sns.color_palette("Paired", 9))

color = ['C1', 'C3']
label = ["PS", "LT"]

f_size = (14, 10)

x_list = list()
x_naive = list()
execution_timeps = list()
execution_timelt = list()

input_path = r'./constraint_change_q1c3.csv'
input_file = open(input_path, "r")

Lines = input_file.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    if line == '\n':
        continue
    if count < 2:
        continue
    if count > 11:
        break
    items = line.strip().split(',')
    x_list.append(items[0])
    execution_timeps.append(float(items[1]))
    if items[2] != '':
        execution_timelt.append(float(items[2]))
    else:
        execution_timelt.append(0)

print(x_list, execution_timeps, execution_timelt)

index = np.arange(len(x_list))
bar_width = 0.35

fig, ax = plt.subplots(1, 1, figsize=f_size)

plt.bar(index, execution_timeps, bar_width, color=color[0], label=label[0])
# plt.bar(index + bar_width, execution_timelt, bar_width,  color=color[1], label=label[1])
plt.xticks(index, x_list)

plt.xlabel('race = "race3"')
plt.ylabel('Running time (s)')
# plt.legend(bbox_to_anchor=(1, 0.9), loc="upper right")
plt.legend(loc="best")
plt.yticks([0, 20, 40, 60])
plt.tight_layout()
plt.savefig("healthcare_constraint_change_q1c3.png",
            bbox_inches='tight')
plt.show()
