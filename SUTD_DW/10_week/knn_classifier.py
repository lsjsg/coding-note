from sklearn.model_selection import train_test_split
from sklearn import neighbors, datasets
from sklearn.metrics import confusion_matrix
import numpy as np
bunchobject = datasets.load_breast_cancer()


def get_metrics(actual_targets, predicted_targets, labels):
    c_matrix = confusion_matrix(actual_targets, predicted_targets, labels)
    output = {}
    output['confusion matrix'] = c_matrix
    output['total records'] = round(np.sum(c_matrix), 3)
    output['accuracy'] = round(
        (c_matrix[0, 0] + c_matrix[1, 1]) / np.sum(c_matrix), 3)
    output['sensitivity'] = round(c_matrix[1, 1] / np.sum(c_matrix[1]), 3)
    output['false positive rate'] = round(
        c_matrix[0, 1] / np.sum(c_matrix[0]), 3)
    return output


def five_number_summary(x):
    l = []
    if len(x.shape) == 2:
        for j in range(x.shape[1]):
            i = x[:, [j]]
            l.append({'minimum': np.min(i), "first quartile": np.percentile(i, 25), "median": np.percentile(
                i, 50), "third quartile": np.percentile(i, 75), "maximum": np.max(i)})
        return l
    else:
        return None


def normalize_minmax(data):
    if len(data.shape) == 2:
        for j in range(data.shape[1]):
            i = data[:, [j]]
            data[:, [j]] = (data[:, [j]]-np.ones(data[:, [j]].shape)
                            * min(data[:, [j]])) / (np.max(i) - np.min(i))
        return data
    return None


def knn_classifier(bunchobject, feature_list, size, seed, k):
    data = bunchobject.data[:, feature_list]
    data = normalize_minmax(data)
    target = bunchobject.target
    data_train, data_test, target_train, target_test = train_test_split(
        data, target, test_size=0.40, random_state=seed)
    clf = neighbors.KNeighborsClassifier(k)
    clf.fit(data_train, target_train)
    target_predicted = clf.predict(data_test)
    results = get_metrics(target_test, target_predicted, [1, 0])
    return results
