import matplotlib.pyplot as plt
import numpy as np

# Example data for different models
model_names = ['XG-Boost', 'GRB', 'Random Forest','LR', 'DT', 'Hybrid',]
accuracy =  [0.61, 0.60, 0.66, 0.62, 0.58, 0.64,]
precision = [0.68, 0.74, 0.67, 0.65, 0.61, 0.68, ]
recall =    [0.61, 0.60, 0.66, 0.62, 0.58, 0.64, ]
f1_score =  [0.63, 0.63, 0.65, 0.63, 0.59, 0.65,] 

# Bar width
bar_width = 0.2

# Set up the bar positions
index = np.arange(len(model_names))

# Plot the bars
plt.figure(figsize=(10, 6))
bar1 = plt.bar(index, accuracy, bar_width, label='Accuracy')
bar2 = plt.bar(index + bar_width, precision, bar_width, label='Precision')
bar3 = plt.bar(index + 2 * bar_width, recall, bar_width, label='Recall')
bar4 = plt.bar(index + 3 * bar_width, f1_score, bar_width, label='F1 Score')

# Add numerical values on top of each bar
for i, acc in enumerate(accuracy):
    plt.text(i - 0.1, acc + 0.02, f'{acc:.2f}', color='black')
    plt.text(i + bar_width - 0.1, precision[i] + 0.02, f'{precision[i]:.2f}', color='black')
    plt.text(i + 2 * bar_width - 0.1, recall[i] + 0.02, f'{recall[i]:.2f}', color='black')
    plt.text(i + 3 * bar_width - 0.1, f1_score[i] + 0.02, f'{f1_score[i]:.2f}', color='black')

# Add labels, title, and legend
plt.xlabel('Models')
plt.ylabel('Scores')
plt.title('Model Comparison Metrics of French Language')
plt.xticks(index + 1.5 * bar_width, model_names)
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()