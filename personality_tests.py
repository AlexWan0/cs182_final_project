class Eval:
    '''
    Class for personality test evaluation
    '''
    def get_questions(self) -> list[tuple[str, list[str]]]:
        '''
        Outputs a list of questions and answer options.
        [
            ('Question 1', ['Option 1', 'Option 2', 'Option 3']),
            ('Question 2', ['Option 1', 'Option 2', 'Option 3']),
            ...
        ]
        '''
        raise NotImplementedError
    
    def evaluate(self, answers: list[str]):
        '''
        The model be run on the question and answers returned by `get_questions()`.
        The model's answers (evaluated in-order) will be passed into the `answers` parameter.
        This function should output a personality score for the model.
        Ideally, this returns a numerical score, (e.g., 20% extroverted) because
        we might not see drastic changes.
        '''
        raise NotImplementedError


class MiniExtroversionTest(Eval):
    def get_questions(self) -> list[tuple[str, list[str]]]:
        '''
        Mini personality test for debugging.
        Partially adapted from https://students.bowdoin.edu/peer-health/wp-content/uploads/sites/10/2012/09/IntroExtroQuiz.pdf.
        '''
        return [
            ('Do you prefer to spend time with others or alone?', ['Alone', 'With others']),
            ('Do you prefer to spend time with a few close friends or a large group of people?', ['Few close friends', 'Large group of people']),
            ('Do you prefer to spend time with people you know or people you don\'t know?', ['People I know', 'People I don\'t know']),
            ('Do you enjoy being the center of attention?', ['No', 'Yes']),
            ('Do you enjoy solitude?', ['Yes', 'No']),
            ('Do you dislike small talk?', ['Yes', 'No']),
            ('Are you a big risk taker?', ['No', 'Yes'])
        ]

    def evaluate(self, answers: list[str]):
        '''
        Evaluates the answers to the mini personality test.
        '''
        score = 0
        score += 1 if answers[0] == 'Alone' else 0
        score += 1 if answers[1] == 'Few close friends' else 0
        score += 1 if answers[2] == 'People I know' else 0
        score += 1 if answers[3] == 'No' else 0
        score += 1 if answers[4] == 'Yes' else 0
        score += 1 if answers[5] == 'Yes' else 0
        score += 1 if answers[6] == 'No' else 0

        return score / 7


tests_dict = {
    'MiniExtroversionTest': MiniExtroversionTest
}
