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

class MBTI_Extroversion(Eval):
    def get_questions(self) -> list[tuple[str, list[str]]]:
        
        return [
            ("At a party do you:\n  1. Interact with many, including strangers\n    2.Interact with a few, known to you\n", ['1', '2']),
            ("At parties do you:\n	1. Stay late, with increasing energy\n	2. Leave early with decreased energy\n", ['1', '2']),
            ("In your social groups do you:\n	1. Keep abreast of other's happenings\n 2. Get behind on the news\n", ['1', '2']),
            ("In phoning do you:\n	1. Rarely question that it will all be said\n	2. Rehearse what you'll say\n", ['1', '2']),
            ("In company do you:\n  1. initiate conversation\n	2. wait to be approached\n", ['1', '2']),
            ("Does new and non-routine interaction with others:\n	1. stimulate and energize you\n	2. tax your reserves\n", ['1', '2']),
            ("Do you prefer:\n	1. many friends with brief contact\n	2. a few friends with more lengthy contact\n", ['1', '2']),
            ("Do you:\n	1. speak easily and at length with strangers\n	2. find little to say to strangers\n", ['1', '2']),
            ("When the phone rings do you:\n	1. hasten to get to it first\n	2. hope someone else will answer\n", ['1', '2']),
            ("Are you more inclined to be:\n	1. easy to approach\n	2. somewhat reserved\n", ['1', '2'])
        ]

    def evaluate(self, answers: list[str]):
        '''
        Evaluates the answers to the mini personality test.
        '''

        return answers.count('1') / 10




tests_dict = {
    'MiniExtroversionTest': MiniExtroversionTest,
    'MBTI_Extroversion': MBTI_Extroversion
    }
