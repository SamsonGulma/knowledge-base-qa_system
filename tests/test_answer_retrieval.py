import unittest
from answer_retrieval import AnswerRetrieval
from knowledge_base_crud import KnowledgeBase


class TestAnswerRetrieval(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize with a test knowledge base
        cls.kb = KnowledgeBase('test_knowledge_base.json')
        cls.kb.add_subject('Computer Science')
        cls.kb.add_topic('Computer Science', 'Data Structures')
        cls.kb.add_subtopic('Computer Science', 'Data Structures', 'Arrays', 'A data structure that holds a fixed-size sequence of elements of the same type.')
        
        cls.ar = AnswerRetrieval('test_knowledge_base.json')

    # def test_full_match(self):
    #     result = self.ar.retrieve_answer('Tell me about Arrays in Data Structures.')
    #     self.assertEqual(result['status'], 'found')
    #     self.assertEqual(result['message'], 'A data structure that holds a fixed-size sequence of elements of the same type.')

    def test_partial_match(self):
        result = self.ar.retrieve_answer('Explain Data Structures in Computer Science.')
        self.assertEqual(result['status'], 'partial_match')
        self.assertIn("I found the topic 'Data Structures'", result['message'])

    def test_not_found(self):
        result = self.ar.retrieve_answer('Explain Graph Theory in Mathematics.')
        self.assertEqual(result['status'], 'not_found')
        self.assertEqual(result['message'], "Sorry, I couldn't find the subject in the Knowledge Base.")

    @classmethod
    def tearDownClass(cls):
        # Clean up the test knowledge base
        cls.kb.delete_subject('Computer Science')


if __name__ == '__main__':
    unittest.main()
