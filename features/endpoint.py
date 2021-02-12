from features.implementation import dummy


class FeatureExtractorEndpoint(object):
    """Class implementing the feature extractor endpoint"""

    # TODO: to be implemented (specific to the library)
    def __init__(self, *args, **kwargs):
        """Initializes the FeatureExtractorEndpoint"""
        pass

    # ------------------------- #
    # Endpoint for the features #
    # ------------------------- #

    # Features:
    #   1. dummy feature - an example of a dummy feature (for the dev purposes)
    #   2. ...
    #   3. ...

    @staticmethod
    def get_dummy(data, **kwargs):
        return dummy.compute_dummy(data, **kwargs)
