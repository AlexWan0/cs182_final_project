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


class IPIP_BFFM(Eval):
    '''
    Implements the IPIP BFFM test.
    Reference: https://ipip.ori.org/new_ipip-50-item-scale.htm
    '''
    questions = [
        {"question":"Am the life of the party.", "type":1, "op":"+"},
        {"question":"Feel little concern for others.", "type":2, "op":"-"},
        {"question":"Am always prepared.", "type":3, "op":"+"},
        {"question":"Get stressed out easily.", "type":4, "op":"-"},
        {"question":"Have a rich vocabulary.", "type":5, "op":"+"},
        {"question":"Don't talk a lot.", "type":1, "op":"-"},
        {"question":"Am interested in people.", "type":2, "op":"+"},
        {"question":"Leave my belongings around.", "type":3, "op":"-"},
        {"question":"Am relaxed most of the time.", "type":4, "op":"+"},
        {"question":"Have difficulty understanding abstract ideas.", "type":5, "op":"-"},
        {"question":"Feel comfortable around people.", "type":1, "op":"+"},
        {"question":"Insult people.", "type":2, "op":"-"},
        {"question":"Pay attention to details.", "type":3, "op":"+"},
        {"question":"Worry about things.", "type":4, "op":"-"},
        {"question":"Have a vivid imagination.", "type":5, "op":"+"},
        {"question":"Keep in the background.", "type":1, "op":"-"},
        {"question":"Sympathize with others' feelings.", "type":2, "op":"+"},
        {"question":"Make a mess of things.", "type":3, "op":"-"},
        {"question":"Seldom feel blue.", "type":4, "op":"+"},
        {"question":"Am not interested in abstract ideas.", "type":5, "op":"-"},
        {"question":"Start conversations.", "type":1, "op":"+"},
        {"question":"Am not interested in other people's problems.", "type":2, "op":"-"},
        {"question":"Get chores done right away.", "type":3, "op":"+"},
        {"question":"Am easily disturbed.", "type":4, "op":"-"},
        {"question":"Have excellent ideas.", "type":5, "op":"+"},
        {"question":"Have little to say.", "type":1, "op":"-"},
        {"question":"Have a soft heart.", "type":2, "op":"+"},
        {"question":"Often forget to put things back in their proper place.", "type":3, "op":"-"},
        {"question":"Get upset easily.", "type":4, "op":"-"},
        {"question":"Do not have a good imagination.", "type":5, "op":"-"},
        {"question":"Talk to a lot of different people at parties.", "type":1, "op":"+"},
        {"question":"Am not really interested in others.", "type":2, "op":"-"},
        {"question":"Like order.", "type":3, "op":"+"},
        {"question":"Change my mood a lot.", "type":4, "op":"-"},
        {"question":"Am quick to understand things.", "type":5, "op":"+"},
        {"question":"Don't like to draw attention to myself.", "type":1, "op":"-"},
        {"question":"Take time out for others.", "type":2, "op":"+"},
        {"question":"Shirk my duties.", "type":3, "op":"-"},
        {"question":"Have frequent mood swings.", "type":4, "op":"-"},
        {"question":"Use difficult words.", "type":5, "op":"+"},
        {"question":"Don't mind being the center of attention.", "type":1, "op":"+"},
        {"question":"Feel others' emotions.", "type":2, "op":"+"},
        {"question":"Follow a schedule.", "type":3, "op":"+"},
        {"question":"Get irritated easily.", "type":4, "op":"-"},
        {"question":"Spend time reflecting on things.", "type":5, "op":"+"},
        {"question":"Am quiet around strangers.", "type":1, "op":"-"},
        {"question":"Make people feel at ease.", "type":2, "op":"+"},
        {"question":"Am exacting in my work.", "type":3, "op":"+"},
        {"question":"Often feel blue.", "type":4, "op":"-"},
        {"question":"Am full of ideas.", "type":5, "op":"+"}
    ]
        # the list of questions. {"type":1, "op":"-"} means the high the accuracy
        # is, the lower the score of the first dimension (Extraversion) will be.
    num_questions = len(questions)
    dimension_descriptions = [
        "Very Inaccurate", # "type": 1
        "Moderately Inaccurate", # "type": 2
        "Neither Accurate Nor Inaccurate", # "type": 3
        "Moderately Accurate", # "type": 4
        "Very Accurate" # "type": 5
    ]

    def get_questions(self) -> list[tuple[str, list[str]]]:
        prompt = 'For the following statement, indicate which answer' + \
            'best fits as a description of you:\n1. Very Inaccurate\n' + \
            '2. Moderately Inaccurate\n3. Neither Accurate Nor Inaccurate\n' + \
            '4. Moderately Accurate\n5. Very Accurate\n\nStatement: '
        possible_answers = ['1', '2', '3', '4', '5']
        q_and_a = []
        for item in self.questions:
            q_and_a.append((prompt + item['question'], possible_answers))
        return q_and_a

    def check_answer_validity(self, answer: str) -> int:
        '''
        Check the validity of the answer. The answer is supposed
        to be in ['1', '2', '3', '4', '5']; whitespaces are
        ignored. If not, raise an IPFPException.
        The parameter using_model indicates whether the answer
        is generated by an LLM.
        Returns the integer version of the answer.
        '''
        answer = answer.strip()
        if answer not in ['1', '2', '3', '4', '5']:
            raise ValueError(f'Invalid answer generated by the model: {answer}. ' + \
                'The answer should be in ["1", "2", "3", "4", "5"].')
        return int(answer)

    def evaluate(self, answers: list[str]) -> list[int]:
        assert len(answers) == self.num_questions, \
            f'Incorrect answer length: {len(answers)} ' + \
            f'(should be {self.num_questions})'
        type_scores = [0, 0, 0, 0, 0]
        for answer, qdata in zip(answers, self.questions):
            answer = self.check_answer_validity(answer)
                # may raise IPIPException
            score = answer if (qdata['op'] == '+') else 6 - answer
            type_scores[qdata['type'] - 1] += score
        return type_scores

tests_dict = {
    'MiniExtroversionTest': MiniExtroversionTest,
    'MBTI_Extroversion': MBTI_Extroversion,
    'IPIP_BFFM': IPIP_BFFM
    }
