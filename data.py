from datasets import load_dataset
import pandas as pd
import glob

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

class RedditData(RawData):
    def __init__(self, test_size=0.2, val_size=0.1):
        # https://www.kaggle.com/datasets/mexwell/reddit-comment-and-thread
        # there are datasets of comments from different kinds of topics on Reddit
        # firstly combine all the data and then split the data
        reddit_data = glob.glob('*.csv')
        combined_df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
        combined_df.to_csv('reddit_comment.csv', index=False)
        train_val_df, test_df = train_test_split(combined_df, test_size=test_size, random_state=42)
        train_df, val_df = train_test_split(train_val_df, test_size=val_size/(1-test_size), random_state=42)
        train_df.to_csv('reddit_train_dataset.csv', index=False)
        val_df.to_csv('reddit_validation_dataset.csv', index=False)
        test_df.to_csv('reddit_test_dataset.csv', index=False)
        self.train_data = train_df
        self.validation_data = val_df
        self.test_data = test_df
        
    def get_train_data(self):
        return self.train_data['text'].tolist()

    def get_validation_data(self):
        return self.validation_data['text'].tolist()

    def get_test_data(self):
        return self.test_data['text'].tolist()

dataset_classes: dict[str, RawData] = {
    'TweetData': TweetData,
    'NewsData': NewsData,
    'CommentData': CommentData,
    'RedditData': RedditData
}
