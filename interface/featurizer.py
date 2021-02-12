from features.endpoint import FeatureExtractorEndpoint


class FeatureExtractorMapping(object):
    """Class implementing the features extractor mapping"""

    def __init__(self, *args, **kwargs):
        """Initializes the FeatureExtractorMapping (mapping actual extractor)"""
        self.endpoint = FeatureExtractorEndpoint(*args, **kwargs)

    def __repr__(self):
        return str(self.endpoint)

    def __str__(self):
        return str({"endpoint": self.endpoint})

    def __call__(self, feature_name):
        return self.map(feature_name)

    def map(self, feature_name):
        """Map the feature name to the actual extractor's method"""

        # TODO: prepare the mapping for the actual features
        # Prepare the mapping
        mapping = {
            "dummy": self.endpoint.get_dummy
        }

        # Map the feature name to the feature extraction method
        return mapping[feature_name]


class FeatureExtractor(object):
    """Class implementing the features extractor interface"""

    def __init__(self, *args, **kwargs):
        """Initializes the FeatureExtractor featurizer interface"""
        self.mapper = FeatureExtractorMapping(*args, **kwargs)

    def __repr__(self):
        return str(self.mapper)

    def __str__(self):
        return str({"mapper": self.mapper})

    def __call__(self, feature_name, data, **kwargs):
        return self.extract(feature_name, data, **kwargs)

    # TODO: must return dict: {"features": np.ndarray, "labels": list}
    def extract(self, feature_name, data, **kwargs):
        """
        Extract the the specified feature from the input data and kwargs

        :param feature_name: name of the feature to extract
        :type feature_name: str
        :param data: data to extract the features from
        :type data: numpy.ndarray
        :param kwargs: feature extraction arguments
        :type kwargs: dict, optional
        :return: extracted features and labels (see <extractor>.extract)
        :rtype: dict {"features": ..., "labels": ...}
        """
        return self.mapper.map(feature_name)(data, **kwargs)
