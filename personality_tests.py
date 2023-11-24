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
            'best fits as a description of you with 1, 2, 3, 4, or 5:\n' + \
            '1. Very Inaccurate\n' + \
            '2. Moderately Inaccurate\n3. Neither Accurate Nor Inaccurate\n' + \
            '4. Moderately Accurate\n5. Very Accurate\n\n' + \
            'Statement: '
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

class sociotype(Eval):
    '''
    Implements the sociotype test.
    Reference: https://github.com/asalduur/sociotype-quiz
    '''
    questions = [{
        "RATQ1":
        "QUESTION ONE\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. I'm consistent and reliable, but not flexible enough.\n   b. I'm flexible and changeable, but lack consistency."
    }, {
        "RATQ2":
        "QUESTION TWO\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. A bad mood has little impact on my productivity.\n   b. I'm strongly dependent on my internal biorhythms."
    }, {
        "RATQ3":
        "QUESTION THREE\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. I do not start something new until I've finished the previous task.\n   b. Usually, I start several projects at once."
    }, {
        "EXTQ1":
        "QUESTION FOUR\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. I am an open person.\n   b. I am a reserved person."
    }, {
        "EXTQ2":
        "QUESTION FIVE\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. Contacts with strangers do not bother me.\n   b. Contacts with strangers require effort."
    }, {
        "EXTQ3":
        "QUESTION SIX\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. It is easier for me to understand others than myself.\n   b. It is easier for me to understand myself than others."
    }, {
        "SENQ1":
        "QUESTION SEVEN\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. If nothing is clear, I actively collect information\n   b. If nothing is clear, I rely on my intuition."
    }, {
        "SENQ2":
        "QUESTION EIGHT\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. I see everything that happens around me.\n   b. I see only what I attach importance to."
    }, {
        "SENQ3":
        "QUESTION NINE\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. I see better ways of achieving a goal.\n   b. I see a goal better than the ways to achieve it."
    }, {
        "LOGQ1":
        "QUESTION TEN\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. I live more by reason than by heart.\n   b. I live more with my heart than with my mind."
    }, {
        "LOGQ2":
        "QUESTION ELEVEN\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. I react more to the content of the conversation.\n   b. I am very responsive to the intonation of the speaker."
    }, {
        "LOGQ3":
        "QUESTION TWELVE\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. It is better to prove than to persuade.\n   b. It is better to persuade than to prove."
    }, {
        "RATEX":
        "The following questions will aim to sort you into one of the 4 Jungian dichotomies, rationality and irrationality.\nThe former bases judgement on actions and truths while the latter is governed by perceptions of the mind and body."
    }, {
        "EXTEX":
        "These next questions will see where on the extroversion and introversion spectrum you lean more towards."
    }, {
        "SENEX":
        "The sensing vs intuition dichotomy are understood as mental processes where sensing types focus on experience with the concrete and tangible, whereas intuitive types are receptive of the intangible details of reality, say for instance time/trend."
    }, {
        "LOGEX":
        "The next questions will sort based on the final Jungian dichotomy, logic vs ethics, rational judgement involving inanimate objects and systems ('right or wrong') and rational judgement involving interpersonal relations ('good or evil')."
    }]

    def get_questions(self) -> list[tuple[str, list[str]]]:
        options = ['a', 'b']
        QNA = []
        for item in self.questions:
            QNA.append(next(iter(item.values())), options)

    def evaluate(self, answers: list[str]):
        socio = [0, 0, 0, 0]

        rat_count = 0
        irrat_count = 0
        for answer in answers[:3]:
            if answer == "a":
                rat_count += 1
            else:
                irrat_count += 1
        if irrat_count > rat_count:
            socio[0] = 1

        extro_count = 0
        intro_count = 0
        for answer in answers[3:6]:
            if answer == "a":
                extro_count += 1
            else:
                intro_count += 1
        if intro_count > extro_count:
            socio[1] = 1

        sen_count = 0
        intui_count = 0
        for answer in answers[6:9]:
            if answer == "a":
                sen_count += 1
            else:
                intui_count += 1
        if intui_count > sen_count:
            socio[2] = 1

        log_count = 0
        eth_count = 0
        for answer in answers[9:12]:
            if answer == "a":
                log_count += 1
            else:
                eth_count += 1
        if eth_count > log_count:
            socio[3] = 1

        return socio

    def get_sociotype(socio):
        """ Loops through sociotype dictionary to find user match """
    
        sociotype = {
            "ESE": [0,0,0,1],
            "LII": [0,1,1,0],
            "ILE": [1,0,1,0],
            "SEI": [1,1,0,1],
            "EIE": [0,0,1,1],
            "LSI": [0,1,0,0],
            "SLE": [1,0,0,0],
            "IEI": [1,1,1,1],
            "LIE": [0,0,1,0],
            "ESI": [0,1,0,1],
            "SEE": [1,0,0,1],
            "ILI": [1,1,1,0],
            "IEE": [1,0,1,1],
            "SLI": [1,1,0,0],
            "LSE": [0,0,0,0],
            "EII": [0,1,1,1]
        }
        
        for personality in sociotype:
            if sociotype[personality] == socio:
                return personality
    
    def type_blurb(personality):
        """ Parses through dictionary of type and prints user a blurb about their type """
        
        type_and_blurb = {
            "ESE": (ESE),
            "LII": (LII),
            "ILE": (ILE),
            "SEI": (SEI),
            "EIE": (EIE),
            "LSI": (LSI),
            "SLE": (SLE),
            "IEI": (IEI),
            "LIE": (LIE),
            "ESI": (ESI),
            "SEE": (SEE),
            "ILI": (ILI),
            "IEE": (IEE),
            "SLI": (SLI),
            "LSE": (LSE),
            "EII": (EII)
        }
        
        for key in type_and_blurb:
            if key == personality:
                print(type_and_blurb[key])
                
tests_dict = {
    'MiniExtroversionTest': MiniExtroversionTest,
    'MBTI_Extroversion': MBTI_Extroversion,
    'IPIP_BFFM': IPIP_BFFM
    'sociotype': sociotype
    }
