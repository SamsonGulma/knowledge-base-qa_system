import unittest
from question_matching_engine import QuestionMatchingEngine
from knowledge_base_crud import KnowledgeBase

class TestQuestionMatchingEngine(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize with a test knowledge base
        cls.kb = KnowledgeBase('test_knowledge_base.json')
        cls.kb.add_subject('Computer Science')
        cls.kb.add_topic('Computer Science', 'Data Structures')
        cls.kb.add_subtopic('Computer Science', 'Data Structures', 'Arrays', 'A data structure that holds a fixed-size sequence of elements of the same type.')
        
        cls.qme = QuestionMatchingEngine('test_knowledge_base.json')

    def test_parse_question(self):
        result = self.qme.parse_question('Tell me about Arrays in Data Structures.')
        self.assertIn('Computer Science', result['subjects'])
        self.assertIn('Arrays', result['tokens'])

    def test_match_topic_and_subtopic(self):
        result = self.qme.match_topic_and_subtopic('Computer Science', 'Tell me about Arrays in Data Structures.')
        self.assertIn('Data Structures', result['topics'])
        self.assertEqual(result['subtopics'][0]['name'], 'Arrays')

    def test_get_answer_found(self):
        result = self.qme.get_answer('Tell me about Arrays in Data Structures.')
        self.assertEqual(result, 'A data structure that holds a fixed-size sequence of elements of the same type.')

    def test_get_answer_not_found(self):
        result = self.qme.get_answer('Explain Graph Theory in Mathematics.')
        self.assertEqual(result, "Sorry, I couldn't find the subject in the Knowledge Base.")

    def test_get_answer_partial_match(self):
        result = self.qme.get_answer('Explain Data Structures in Computer Science.')
        self.assertIn("I found the topic 'Data Structures'", result)

    @classmethod
    def tearDownClass(cls):
        # Clean up the test knowledge base
        cls.kb.delete_subject('Computer Science')

if __name__ == '__main__':
    unittest.main()
