import numpy as np
from sklearn import neighbors, datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

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


def knn_classifier_full(bunchobject, feature_list, size, seed):
    data = bunchobject.data[:, feature_list]
    data = normalize_minmax(data)
    data_train, data_part2, target_train, target_part2 = train_test_split(
        data, bunchobject.target, test_size=0.40, random_state=seed)
    validate_x, test_x, validate_y, test_y = train_test_split(
        data_part2, target_part2, test_size=0.50, random_state=seed)
    a_list = []
    for i in range(1, 20):
        clf = neighbors.KNeighborsClassifier(n_neighbors=i)
        clf.fit(data_train, target_train)
        target_predicted = clf.predict(validate_x)
        accuracy = get_metrics(validate_y, target_predicted, [1, 0])[
            'accuracy']
        a_list.append(accuracy)
    a = max(a_list)
    k = a_list.index(a)+1
    results = {}
    results['best k'] = k
    clf = neighbors.KNeighborsClassifier(n_neighbors=k)
    clf.fit(data_train, target_train)
    target_predicted = clf.predict(validate_x)
    target_predicted_test = clf.predict(test_x)
    results['validation set'] = get_metrics(
        validate_y, target_predicted, [1, 0])
    results['test set'] = get_metrics(test_y, target_predicted_test, [1, 0])
    return results