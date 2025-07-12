import json

class KnowledgeBase:
    def __init__(self, path):
        with open(path, 'r') as f:
            self.data = json.load(f)

    def get_subjects(self):
        return [subject['name'] for subject in self.data['subjects']]

    def get_topics(self, subject_name):
        for subject in self.data['subjects']:
            if subject['name'] == subject_name:
                return [topic['name'] for topic in subject['topics']]
        return []

    def get_subtopics(self, subject_name, topic_name):
        for subject in self.data['subjects']:
            if subject['name'] == subject_name:
                for topic in subject['topics']:
                    if topic['name'] == topic_name:
                        return topic.get('subtopics', [])
        return []
