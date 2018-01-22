import time
import pandas as pd

TAGS = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']


def create_submission(predictor, train_x, train_ys, test_x, test_id, write_to):
    """
    Creates a submissions file for the given test set

    :param predictor: The predictor to be used for fitting and predicting
    :param train_x: The (preprocessed) features to be used for fitting
    :param train_ys: A dictionary from tag name to its values in the training set.
    :param test_x: The (preprocessed) features to be used for predicting.
    :param write_to: A file path where the submission is written
    """

    submission = pd.DataFrame({'id': test_id})
    for tag in TAGS:
        print("{} Fitting on {} tag".format(predictor, tag))
        predictor.fit(train_x, train_ys[tag])
        submission[tag] = predictor.predict(test_x)

    submission.to_csv(write_to, index=False)
    print("Submissions created at location " + write_to)


def timing(f):
    """
    Decorator to time a function call and print results.
    :param f: Callable to be timed
    :return: Void. Prints to std:out as a side effect
    """
    def wrap(*args, **kwargs):
        start = time.time()
        ret = f(*args, **kwargs)
        stop = time.time()
        print('{} function took {:.1f} seconds to complete\n'.format(f.__name__, (stop - start)))
        return ret
    return wrap
