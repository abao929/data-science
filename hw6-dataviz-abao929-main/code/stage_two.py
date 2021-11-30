from utils import *
from matplotlib.colors import rgb_to_hsv
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score, confusion_matrix
import itertools
import seaborn as sns

#Which set of features yields highest accuracy for logistic regression model
bank_df = get_banknote_df()
features = ['Variance', 'Skewness', 'Curtosis', 'Entropy']
combos = [[f] for f in features]
for x in range(2, 5):
    combo_tuple = list(itertools.combinations(features, x))
    combos.extend([list(t) for t in combo_tuple])
accuracies = []
dummy_accuracies = []
features_axis = []
for combo in combos:
    model, ohe, train_df, test_df = get_trained_model('banknote_authentication', 'logistic_regression', 'Class', combo)
    acc, y_pred, y_targ = get_model_accuracy(model, train_df, ohe, dataset_name='banknote_authentication', target_name='Class', feature_names=combo)
    dummy_model, dummy_ohe, dummy_train_df, dummy_test_df = get_trained_model('banknote_authentication', 'dummy', 'Class', combo)
    dummy_acc, dummy_y_pred, dummy_y_targ = get_model_accuracy(dummy_model, dummy_train_df, ohe, dataset_name='banknote_authentication', target_name='Class', feature_names=combo)
    accuracies.append(acc)
    dummy_accuracies.append(dummy_acc)
    letters =  [f[0] for f in combo]
    features_axis.append(', '.join(letters))
fig, ax = plt.subplots(figsize =(16, 9))
ax.set_title('Features vs. Regression Accuracy', loc ='left')
ax.bar(features_axis, accuracies)
plt.xlabel('Features', fontweight ='bold', fontsize = 15)
plt.ylabel('Accuracies', fontweight ='bold', fontsize = 15)
plt.savefig('../graphs/s2q1.png')
acc_dict = dict(zip(accuracies, features_axis))
max_acc = max(accuracies)
min_acc = min(accuracies)
print(f'Features: {acc_dict[max_acc]} had the highest accuracy: {max_acc}')
print(f'Features: {acc_dict[min_acc]} had the lowest accuracy: {min_acc}')

#Which set of features yields did best compared to dummy for logistic regression model
diff = np.subtract(accuracies, dummy_accuracies)
print(dummy_accuracies)
print(diff)
fig, ax = plt.subplots(figsize =(16, 9))
ax.set_title('Features vs. Regression Accuracy Difference', loc ='left')
ax.bar(features_axis, diff)
plt.xlabel('Features', fontweight ='bold', fontsize = 15)
plt.ylabel('Accuracy Difference', fontweight ='bold', fontsize = 15)
plt.savefig('../graphs/s2q2.png')
acc_dict = dict(zip(diff, features_axis))
max_acc = max(diff)
min_acc = min(diff)
print(f'Features: {acc_dict[max_acc]} had the highest accuracy difference: {max_acc}')
print(f'Features: {acc_dict[min_acc]} had the lowest accuracy difference: {min_acc}')


#Best Confusion matrix
model, ohe, train_df, test_df = get_trained_model('banknote_authentication', 'logistic_regression', 'Class', ['Variance', 'Skewness', 'Curtosis'])
acc, y_pred, y_targ = get_model_accuracy(model, train_df, ohe, dataset_name='banknote_authentication', target_name='Class', feature_names=['Variance', 'Skewness', 'Curtosis'])
cf_matrix = confusion_matrix(y_targ, y_pred)
names = ['True Neg', 'False Pos', 'False Neg', 'True Pos']
counts = ['{0:0.0f}'.format(value) for value in cf_matrix.flatten()]
percents = ['{0:.2%}'.format(value) for value in cf_matrix.flatten()/np.sum(cf_matrix)]
labels = [f'{v1}\n{v2}\n{v3}' for v1, v2, v3 in zip(names, counts, percents)]
labels = np.asarray(labels).reshape(2,2)
fig, ax = plt.subplots(figsize =(16, 9))
ax.set_title('Best Logistic Regression Model\'s Confusion Matrix', loc ='left')
ax = sns.heatmap(cf_matrix, annot=labels, fmt='', cmap='Blues')
plt.savefig('../graphs/s2q3_1.png')

#Worst Confusion Matrix
model, ohe, train_df, test_df = get_trained_model('banknote_authentication', 'logistic_regression', 'Class', ['Entropy'])
acc, y_pred, y_targ = get_model_accuracy(model, train_df, ohe, dataset_name='banknote_authentication', target_name='Class', feature_names=['Entropy'])
cf_matrix = confusion_matrix(y_targ, y_pred)
names = ['True Neg', 'False Pos', 'False Neg', 'True Pos']
counts = ['{0:0.0f}'.format(value) for value in cf_matrix.flatten()]
percents = ['{0:.2%}'.format(value) for value in cf_matrix.flatten()/np.sum(cf_matrix)]
labels = [f'{v1}\n{v2}\n{v3}' for v1, v2, v3 in zip(names, counts, percents)]
labels = np.asarray(labels).reshape(2,2)
fig, ax = plt.subplots(figsize =(16, 9))
ax.set_title('Worst Logistic Regression Model\'s Confusion Matrix', loc ='left')
ax = sns.heatmap(cf_matrix, annot=labels, fmt='', cmap='Blues')
plt.savefig('../graphs/s2q3_2.png')