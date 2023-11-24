from datasets import load_dataset


class RawData():
    '''
    Raw data class
    Each function for getting a data split should return a list of strings.
    '''
    def get_train_data(self) -> list[str]:
        raise NotImplementedError

    def get_validation_data(self) -> list[str]:
        raise NotImplementedError

    def get_test_data(self) -> list[str]:
        raise NotImplementedError

    def get_data(self):
        return {
            'train': self.get_train_data(),
            'validation': self.get_validation_data(),
            'test': self.get_test_data()
        }

class TweetData(RawData):
    def __init__(self):
        self.tweets = load_dataset("tweet_eval", "sentiment")

    def get_train_data(self):
        return self.tweets['train']['text']

    def get_validation_data(self):
        return self.tweets['validation']['text']

    def get_test_data(self):
        return self.tweets['test']['text']

class NewsData(RawData):
    def __init__(self):
        raw_dataset = load_dataset('ag_news')
        train_and_val = raw_dataset['train'].train_test_split(test_size=0.04)
        self.news = {
            'train': train_and_val['train'],
            'validation': train_and_val['test'],
            'test': raw_dataset['test']
        }
    
    def get_train_data(self):
        return self.news['train']['text']

    def get_validation_data(self):
        return self.news['validation']['text']

    def get_test_data(self):
        return self.news['test']['text']
    
class CommentData(RawData):
    def __init__(self):
        raw_dataset = load_dataset('ag_comments')
        train_and_val = raw_dataset['train'].train_test_split(test_size=0.04)
        self.comments = {
            'train': train_and_val['train'],
            'validation': train_and_val['test'],
            'test': raw_dataset['test']
        }
    
    def get_train_data(self):
        return self.comments['train']['text']

    def get_validation_data(self):
        return self.comments['validation']['text']

    def get_test_data(self):
        return self.comments['test']['text']

dataset_classes: dict[str, RawData] = {
    'TweetData': TweetData,
    'NewsData': NewsData,
    'CommentData': CommentData
}
