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
    '''
    implements of the MBTI test.
    reference: https://github.com/monsef-alahem/MBTI_personality_16_tester/blob/main/main.py
    '''
    def get_questions(self) -> list[tuple[str, list[str]]]:
        return [
            ("1.At a party do you:\n	1. Interact with many, including strangers\n	2. Interact with a few, known to you\n",['1','2']),
			("2. Are you more:\n	1. Realistic than speculative\n	2. Speculative than realistic\n",['1','2']),
			("3. Is it worse to:\n	1. Have your “head in the clouds”\n	2.Be “in a rut”\n",['1','2']),
			("4. Are you more impressed by:\n	1. Principles\n	2. Emotions\n",['1','2']),
			("5. Are more drawn toward the:\n	1. Convincing\n	2. Touching\n",['1','2']),
			("6. Do you prefer to work:\n	1. To deadlines\n	2. Just “whenever”\n",['1','2']),
			("7. Do you tend to choose:\n	1. Rather carefully\n	2. Somewhat impulsively\n",['1','2']),
			("8. At parties do you:\n	1. Stay late, with increasing energy\n	2. Leave early with decreased energy\n",['1','2']),
			("9. Are you more attracted to:\n	1. Sensible people\n	2. Imaginative people\n",['1','2']),
			("10. Are you more interested in:\n	1. What is actual\n	2. What is possible\n",['1','2']),
			("11. In judging others are you more swayed by:\n	1. Laws than circumstances\n	2. Circumstances than laws\n",['1','2']),
			("12. In approaching others is your inclination to be somewhat:\n	1. Objective\n	2. Personal\n",['1','2']),
			("13. Are you more:\n	1. Punctual\n	2. Leisurely\n",['1','2']),
			("14. Does it bother you more having things:\n	1. Incomplete\n	2. Completed\n",['1','2']),
			("15. In your social groups do you:\n	1. Keep abreast of other's happenings\n	2. Get behind on the news\n",['1','2']),
			("16. In doing ordinary things are you more likely to:\n	1. Do it the usual way\n	2. Do it your own way\n",['1','2']),
			("17. Writers should:\n	1. “Say what they mean and mean what they say”\n	2. Express things more by use of analogy\n",['1','2']),
			("18. Which appeals to you more:\n	1. Consistency of thought\n	2. Harmonious human relationships\n",['1','2']),
			("19. Are you more comfortable in making:\n	1. Logical judgments\n	2. Value judgments\n",['1','2']),
			("20. Do you want things:\n	1. Settled and decided\n	2. Unsettled and undecided\n",['1','2']),
			("21. Would you say you are more:\n	1. Serious and determined\n	2. Easy-going\n",['1','2']),
			("22. In phoning do you:\n	1. Rarely question that it will all be said\n	2. Rehearse what you'll say\n",['1','2']),
			("23. Facts:\n	1. “Speak for themselves”\n	2. Illustrate principles\n",['1','2']),
			("24. Are visionaries:\n	1. somewhat annoying\n	2. rather fascinating\n",['1','2']),
			("25. Are you more often:\n	1. a cool-headed person\n	2. a warm-hearted person\n",['1','2']),
			("26. Is it worse to be:\n	1. unjust\n	2. merciless\n",['1','2']),
			("27. Should one usually let events occur:\n	1. by careful selection and choice\n	2. randomly and by chance\n",['1','2']),
			("28. Do you feel better about:\n	1. having purchased\n	2. having the option to buy\n",['1','2']),
			("29. In company do you:\n	1. initiate conversation\n	2. wait to be approached\n",['1','2']),
			("30. Common sense is:\n	1. rarely questionable\n	2. frequently questionable\n",['1','2']),
			("31. Children often do not:\n	1. make themselves useful enough\n	2. exercise their fantasy enough\n",['1','2']),
			("32. In making decisions do you feel more comfortable with:\n	1. standards\n	2. feelings\n",['1','2']),
			("33. Are you more:\n	1. firm than gentle\n	2. gentle than firm\n",['1','2']),
			("34. Which is more admirable:\n	1. the ability to organize and be methodical\n	2. the ability to adapt and make do\n",['1','2']),
			("35. Do you put more value on:\n	1. infinite\n	2. open-minded\n",['1','2']),
			("36. Does new and non-routine interaction with others:\n	1. stimulate and energize you\n	2. tax your reserves\n",['1','2']),
			("37. Are you more frequently:\n	1. a practical sort of person\n	2. a fanciful sort of person\n",['1','2']),
			("38. Are you more likely to:\n	1. see how others are useful\n	2. see how others see\n",['1','2']),
			("39. Which is more satisfying:\n	1. to discuss an issue throughly\n	2. to arrive at agreement on an issue\n",['1','2']),
			("40. Which rules you more:\n	1. your head\n	2. your heart\n",['1','2']),
			("41. Are you more comfortable with work that is:\n	1. contracted\n	2. done on a casual basis\n",['1','2']),
			("42. Do you tend to look for:\n	1. the orderly\n	2. whatever turns up\n",['1','2']),
			("43. Do you prefer:\n	1. many friends with brief contact\n	2. a few friends with more lengthy contact\n",['1','2']),
			("44. Do you go more by:\n	1. facts\n	2. principles\n",['1','2']),
			("45. Are you more interested in:\n	1. production and distribution\n	2. design and research\n",['1','2']),
			("46. Which is more of a compliment:\n	1. “There is a very logical person.”\n	2. “There is a very sentimental person.”\n",['1','2']),
			("47. Do you value in yourself more that you are:\n	1. unwavering\n	2. devoted\n",['1','2']),
			("48. Do you more often prefer the\n	1. final and unalterable statement\n	2. tentative and preliminary statement\n",['1','2']),
			("49. Are you more comfortable:\n	1. after a decision\n	2. before a decision\n",['1','2']),
			("50. Do you:\n	1. speak easily and at length with strangers\n	2. find little to say to strangers\n",['1','2']),
			("51. Are you more likely to trust your:\n	1. experience\n	2. hunch\n",['1','2']),
			("52. Do you feel:\n	1. more practical than ingenious\n	2. more ingenious than practical\n",['1','2']),
			("53. Which person is more to be complimented  - one of:\n	1. clear reason\n	2. strong feeling\n",['1','2']),
			("54. Are you inclined more to be:\n	1. fair-minded\n	2. sympathetic\n",['1','2']),
			("55. Is it preferable mostly to:\n	1. make sure things are arranged\n	2. just let things happen\n",['1','2']),
			("56. In relationships should most things be:\n	1. re-negotiable\n	2. random and circumstantial\n",['1','2']),
			("57. When the phone rings do you:\n	1. hasten to get to it first\n	2. hope someone else will answer\n",['1','2']),
			("58. Do you prize more in yourself:\n	1. a strong sense of reality\n	2. a vivid imagination\n",['1','2']),
			("59. Are you drawn more to:\n	1. fundamentals\n	2. overtones\n",['1','2']),
			("60. Which seems the greater error:\n	1. to be too passionate\n	2. to be too objective\n",['1','2']),
			("61. Do you see yourself as basically:\n	1. hard-headed\n	2. soft-hearted\n",['1','2']),
			("62. Which situation appeals to you more:\n	1. the structured and scheduled\n	2. the unstructured and unscheduled\n",['1','2']),
			("63. Are you a person that is more:\n	1. routinized than whimsical\n	2. whimsical than routinized\n",['1','2']),
			("64. Are you more inclined to be:\n	1. easy to approach\n	2. somewhat reserved\n",['1','2']),
			("65. In writings do you prefer:\n	1. the more literal\n	2. the more figurative\n",['1','2']),
			("66. Is it harder for you to:\n	1. identify with others\n	2. utilize others\n",['1','2']),
			("67. Which do you wish more for yourself:\n	1. clarity of reason\n	2. strength of compassion\n",['1','2']),
			("68. Which is the greater fault:\n	1. being indiscriminate\n	2. being critical\n",['1','2']),
			("69. Do you prefer the:\n	1. planned event\n	2. unplanned event\n",['1','2']),
			("70. Do you tend to be more:\n	1. deliberate than spontaneous\n	2. spontaneous than deliberate\n",['1','2'])
        ]

    def evaluate(self, answers: list[str]):
        '''
        Evaluates the answers to the mbti personality test.
        '''
        ans = [0,0,0,0] # which stand for Extraverted, Sensing, Thinking, Judging
        for i in range(70):
            if ((i+1)%7 == 1) and (answers[i] == 1):
                ans[0] += 0.1
            elif ((i+1)%7 == 2 or (i+1)%7 == 3) and (answers[i] == 1):
                ans[1] += 0.05
            elif ((i+1)%7 == 4 or (i+1)%7 == 5) and (answers[i] == 1):
                ans[2] += 0.05
            elif ((i+1)%7 == 6 or (i+1)%7 == 0) and (answers[i] == 1):
                ans[3] += 0.05
            else: pass
        return ans


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

class Sociotype(Eval):
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

    ESE = """
                                        YOU ARE...
    
                                                    E S E
                                                4D Fe | 3D Si
                                                1D Ni | 2D Te
                                                2D Ne | 1D Ti
                                                3D Fi | 4D Se
        ESEs, with strong extraverted ethics (Fe), are lively, animated, and are skilled at creating emotional ambience and energizing others wherever they go. They are highly intuned with their inner homeostasis and love creating comfort for themselves and those around them due to favoring introverted sensing (Si). They tend to have a good eye for aesthetics and enjoy organizing events for loved ones.
        """
    LII = """
                                        YOU ARE...
    
                                                    LII
                                                4D Ti | 3D Ne
                                                1D Se | 2D Fi
                                                2D Si | 1D Fe
                                                3D Te | 4D Ni
        LIIs are known to be the strong analytical types due to their 4 dimensional introverted thinking (Ti). They are usually able to understand abstract systems and conceptualize, compartmentalize them. If they could be left to think and research for a living, they would reach self-actualization. With extroverted intuition (Ne), they are able to see the big picture and ways of realizing their ideas.
        """
    ILE = """
                                        YOU ARE...
    
                                                    ILE
                                                4D Ne | 3D Ti
                                                1D Fi | 2D Se
                                                2D Fe | 1D Si
                                                3D Ni | 4D Te
        ILEs are creative thinkers who love ideas purely for their unlimited 
        """
    SEI = """
                                        YOU ARE...
    
                                                    SEI
                                                4D Si | 3D Fe
                                                1D Te | 2D Ni
                                                2D Ti | 1D Ne
                                                3D Se | 4D Fi
        """
    EIE = """
                                        YOU ARE...
    
                                                    EIE
                                                4D Fe | 3D Ni
                                                1D Si | 2D Te
                                                2D Se | 1D Ti
                                                3D Fi | 4D Ne
        """
    LSI = """
                                        YOU ARE...
    
                                                    LSI
                                                4D Ti | 3D Se
                                                1D Ne | 2D Fi
                                                2D Ni | 1D Fe
                                                3D Te | 4D Si
        """
    SLE = """
                                        YOU ARE...
    
                                                    SLE
                                                4D Se | 3D Ti
                                                1D Fi | 2D Ne
                                                2D Fe | 1D Ni
                                                3D Si | 4D Te
        """
    IEI = """
                                        YOU ARE...
    
                                                    IEI
                                                4D Ni | 3D Fe
                                                1D Te | 2D Si
                                                2D Ti | 1D Se
                                                3D Ne | 4D Fi
        """
    LIE = """
                                        YOU ARE...
    
                                                    LIE
                                                4D Te | 3D Ni
                                                1D Si | 2D Fe
                                                2D Se | 1D Fi
                                                3D Ti | 4D Ne
        """
    ESI = """
                                        YOU ARE...
    
                                                    ESI
                                                4D Fi | 3D Se
                                                1D Ne | 2D Ti
                                                2D Ni | 1D Te
                                                3D Fe | 4D Si
        """
    SEE = """
                                        YOU ARE...
    
                                                    SEE
                                                4D Se | 3D Fi
                                                1D Ti | 2D Ne
                                                2D Te | 1D Ni
                                                3D Si | 4D Fe
        """
    ILI = """
                                        YOU ARE...
    
                                                    ILI
                                                4D Ni | 3D Te
                                                1D Fe | 2D Si
                                                2D Fi | 1D Se
                                                3D Ne | 4D Ti
        """
    IEE = """
                                        YOU ARE...
    
                                                    IEE
                                                4D Ne | 3D Fi
                                                1D Ti | 2D Se
                                                2D Te | 1D Si
                                                3D Ni | 4D Fe
        """
    SLI = """
                                        YOU ARE...
    
                                                    SLI
                                                4D Si | 3D Te
                                                1D Fe | 2D Ni
                                                2D Fi | 1D Ne
                                                3D Se | 4D Ti
        """
    LSE = """
                                        YOU ARE...
    
                                                    LSE
                                                4D Te | 3D Si
                                                1D Ni | 2D Fe
                                                2D Ne | 1D Fi
                                                3D Ti | 4D Se
        """
    EII = """
                                        YOU ARE...
    
                                                    EII
                                                4D Fi | 3D Ne
                                                1D Se | 2D Ti
                                                2D Si | 1D Te
                                                3D Fe | 4D Ni
        """

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
    'IPIP_BFFM': IPIP_BFFM,
    'Sociotype': Sociotype
    }
