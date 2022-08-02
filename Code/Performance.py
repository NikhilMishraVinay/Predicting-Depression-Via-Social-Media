"""# Importing Accuracy,recall,f1 score,precision related library"""

from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, f1_score, precision_score

"""Function for confusion matrix"""


def confusionMatrix(y_test, y_pred):
    print(confusion_matrix(y_test, y_pred))  # Confusion matrix


"""Function for calculating accuracy,precision,recall and f1 score"""


def perfection(y_test, y_pred):
    # accuracy: (tp + tn) / (p + n)
    accuracy = accuracy_score(y_test, y_pred)
    print('Accuracy: %f' % accuracy)
    # precision tp / (tp + fp)
    precision = precision_score(y_test, y_pred)
    print('Precision: %f' % precision)
    # recall: tp / (tp + fn)
    recall = recall_score(y_test, y_pred)
    print('Recall: %f' % recall)
    # f1: 2 tp / (2 tp + fp + fn)
    f1 = f1_score(y_test, y_pred)
    print('F1 score: %f' % f1)

