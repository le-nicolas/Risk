import numpy as np
import matplotlib.pyplot as plt

# Define risk scenarios
scenarios = {
    "Rare but Severe": {"likelihood": 0.01, "consequence": 1000},
    "Frequent but Less Severe": {"likelihood": 0.5, "consequence": 20},
    "Moderate Frequency and Severity": {"likelihood": 0.2, "consequence": 200},
}

# Assess consequences and calculate expected consequences
for scenario, data in scenarios.items():
    data["expected_consequence"] = data["likelihood"] * data["consequence"]

# Print scenario details
for scenario, data in scenarios.items():
    print(f"{scenario}:")
    print(f"  Likelihood: {data['likelihood']}")
    print(f"  Consequence: {data['consequence']}")
    print(f"  Expected Consequence: {data['expected_consequence']}\n")

# Plot the scenarios
labels = scenarios.keys()
likelihoods = [data["likelihood"] for data in scenarios.values()]
consequences = [data["consequence"] for data in scenarios.values()]
expected_consequences = [data["expected_consequence"] for data in scenarios.values()]

x = np.arange(len(labels))

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Scenarios')
ax1.set_ylabel('Likelihood', color=color)
ax1.bar(x - 0.2, likelihoods, 0.4, label='Likelihood', color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:blue'
ax2.set_ylabel('Consequence', color=color)  # we already handled the x-label with ax1
ax2.bar(x + 0.2, consequences, 0.4, label='Consequence', color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title('Risk Scenario Analysis')
plt.xticks(x, labels)

# Show expected consequences on the plot
for i in range(len(labels)):
    plt.text(x[i], expected_consequences[i] + 10, f'{expected_consequences[i]:.2f}', ha='center', color='black')

fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

plt.show()
