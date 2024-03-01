import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

accuracy_rf = 85
accuracy_xgb = 85
accuracy_grb = 84
accuracy_LR = 85
accuracy_DT = 82
accuracy_xbglrrf = 85
accuracy_bert = 17

tt_rf = 6
tt_xgb = 32
tt_grb = 100
tt_LR = 0.2
tt_DT = 0.4
tt_xbglrrf = 4
tt_bert = 641

# Ensure the lengths of accuracy_scores and tt are the same
accuracy_scores = [accuracy_rf, accuracy_xgb, accuracy_grb, accuracy_LR, accuracy_DT, accuracy_xbglrrf, accuracy_bert]
tt = [tt_rf, tt_xgb, tt_grb, tt_LR, tt_DT, tt_xbglrrf, tt_bert]

# Remove duplicate 'GRU' entry
model_data = {'Model': ['Random Forest', 'XGBoost', 'GRB', 'LR', 'DT', 'Hybrid', "BERT"],
              'Accuracy': accuracy_scores,
              'Time taken': tt}
data = pd.DataFrame(model_data)

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 10))
ax1.set_title('Model Comparison: Accuracy and Time taken for execution', fontsize=13)

color = 'tab:blue'
ax1.set_xlabel('Model', fontsize=13)
ax1.set_ylabel('Time taken', fontsize=13, color=color)
# Use barplot for time taken
ax2 = sns.barplot(x='Model', y='Time taken', data=data, palette='summer')
ax1.tick_params(axis='y')

# Overlay lineplot for accuracy
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Accuracy', fontsize=13, color=color)
ax2 = sns.lineplot(x='Model', y='Accuracy', data=data, sort=False, color=color)
ax2.tick_params(axis='y', color=color)

plt.show()