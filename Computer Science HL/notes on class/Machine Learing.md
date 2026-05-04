### Confusion Matrix

A **confusion matrix** is a tool used to evaluate the performance of a classification model. It presents a summary of the predictions made by the model, comparing them with the actual values. It shows the counts of:

- **True Positive (TP):** Correctly predicted positive cases.
- **True Negative (TN):** Correctly predicted negative cases.
- **False Positive (FP):** Incorrectly predicted as positive when the true value is negative.
- **False Negative (FN):** Incorrectly predicted as negative when the true value is positive.

From this matrix, metrics like **accuracy**, **precision**, **recall**, and **F1-score** can be derived to better understand model performance.

### Cross Validation

**Cross-validation** is a technique used to assess the generalizability of a machine learning model. It involves splitting the dataset into several subsets (folds) and training the model multiple times on different combinations of the training and testing data. The most common form is **k-fold cross-validation**, where:

1. The data is divided into **k** equal parts (folds).
2. The model is trained **k times**, each time using **k-1** folds for training and the remaining fold for testing.
3. The results from all the folds are averaged to give a final performance metric.

This helps to ensure that the model's performance is consistent and not reliant on a specific training/test split.

