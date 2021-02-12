import numpy as np


# TODO: iterate over the subjects (last dimension)
def compute_dummy(data, **kwargs):
    """
    Extract the dummy features (for the dev purposes only)

    :param data: data to extract the features from
    :type data: numpy.ndarray
    :param kwargs: feature extraction arguments
    :type kwargs: dict, optional
    :return: extracted features and labels
    :rtype: dict {"features": ..., "labels": ...}
    """
    return {
        "features": np.random.rand(10, 1),
        "labels": [str(i) for i in range(10)]
    }
