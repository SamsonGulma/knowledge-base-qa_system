import unittest
from knowledge_base_crud import KnowledgeBase

class TestKnowledgeBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.kb = KnowledgeBase('test_knowledge_base.json')
    
    def test_create_subject(self):
        result = self.kb.add_subject('Mathematics')
        self.assertEqual(result, "Subject 'Mathematics' added successfully.")

    def test_create_existing_subject(self):
        result = self.kb.add_subject('Mathematics')
        self.assertEqual(result, "Subject 'Mathematics' already exists.")

    def test_add_topic(self):
        result = self.kb.add_topic('Mathematics', 'Algebra')
        self.assertEqual(result, "Topic 'Algebra' added to 'Mathematics'.")

    def test_add_existing_topic(self):
        result = self.kb.add_topic('Mathematics', 'Algebra')
        self.assertEqual(result, "Topic 'Algebra' already exists in 'Mathematics'.")

    def test_add_subtopic(self):
        result = self.kb.add_subtopic('Mathematics', 'Algebra', 'Quadratic Equations', 'Equations of the form ax^2 + bx + c = 0')
        self.assertEqual(result, "Subtopic 'Quadratic Equations' added to 'Algebra'.")

    def test_read_subjects(self):
        subjects = self.kb.get_subjects()
        self.assertIn('Mathematics', subjects)

    def test_read_topics(self):
        topics = self.kb.get_topics('Mathematics')
        self.assertIn('Algebra', topics)

    def test_read_subtopics(self):
        subtopics = self.kb.get_subtopics('Mathematics', 'Algebra')
        self.assertIn({'name': 'Quadratic Equations', 'description': 'Equations of the form ax^2 + bx + c = 0'}, subtopics)

    def test_update_subtopic(self):
        result = self.kb.update_subtopic('Mathematics', 'Algebra', 'Quadratic Equations', 'Updated Description')
        self.assertEqual(result, "Subtopic 'Quadratic Equations' updated successfully.")
        subtopics = self.kb.get_subtopics('Mathematics', 'Algebra')
        self.assertIn({'name': 'Quadratic Equations', 'description': 'Updated Description'}, subtopics)

    def test_delete_subtopic(self):
        result = self.kb.delete_subtopic('Mathematics', 'Algebra', 'Quadratic Equations')
        self.assertEqual(result, "Subtopic 'Quadratic Equations' deleted successfully.")

    def test_delete_topic(self):
        result = self.kb.delete_topic('Mathematics', 'Algebra')
        self.assertEqual(result, "Topic 'Algebra' deleted successfully.")

    def test_delete_subject(self):
        result = self.kb.delete_subject('Mathematics')
        self.assertEqual(result, "Subject 'Mathematics' deleted successfully.")

if __name__ == '__main__':
    unittest.main()
    ""
