from datasets import load_dataset


class RawData():
    '''
    Raw data class
    Each function for getting a data split should return a list of strings.
    '''
    def get_train_data(self) -> list[str]:
        raise NotImplementedError

    def get_valdiation_data(self) -> list[str]:
        raise NotImplementedError

    def get_test_data(self) -> list[str]:
        raise NotImplementedError

    def get_data(self):
        return {
            'train': self.get_train_data(),
            'validation': self.get_valdiation_data(),
            'test': self.get_test_data()
        }

class TweetData(RawData):
    def __init__(self):
        self.tweets = load_dataset("tweet_eval", "sentiment")

    def get_train_data(self):
        return self.tweets['train']['text']

    def get_valdiation_data(self):
        return self.tweets['validation']['text']

    def get_test_data(self):
        return self.tweets['test']['text']


dataset_classes: dict[str, RawData] = {
    'TweetData': TweetData
}
