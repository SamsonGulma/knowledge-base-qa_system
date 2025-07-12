import spacy
from knowledge_base_crud import KnowledgeBase

class QuestionMatchingEngine:
    def __init__(self, knowledge_base_path='knowledge_base.json'):
        self.kb = KnowledgeBase(knowledge_base_path)
        self.nlp = spacy.load('en_core_web_sm')

    def parse_question(self, question):
        doc = self.nlp(question)
        question_lower = question.lower()

        subjects = self.kb.get_subjects()
        matched_subjects = []

        # Try direct subject name matching
        for s in subjects:
            s_lower = s.lower()
            keywords = s_lower.split()
            if any(keyword in question_lower for keyword in keywords):
                matched_subjects.append(s)

        # If no subject matched, try matching topics or subtopics to infer subject
        if not matched_subjects:
            for s in subjects:
                topics = self.kb.get_topics(s)
                for topic in topics:
                    if topic.lower() in question_lower:
                        matched_subjects.append(s)
                        break
                    subtopics = self.kb.get_subtopics(s, topic)
                    for subtopic in subtopics:
                        if subtopic['name'].lower() in question_lower:
                            matched_subjects.append(s)
                            break

        print("DEBUG - Loaded subjects:", subjects)
        print("DEBUG - Question:", question)
        print("DEBUG - Matched subjects:", matched_subjects)

        return {
            "subjects": matched_subjects,
            "tokens": [token.text for token in doc],
            "nouns": [chunk.text for chunk in doc.noun_chunks],
            "verbs": [token.lemma_ for token in doc if token.pos_ == "VERB"]
        }

    def match_topic_and_subtopic(self, subject, question):
        topics = self.kb.get_topics(subject)
        matched_topics = [t for t in topics if t.lower() in question.lower()]

        subtopics = []
        for topic in matched_topics:
            subtopic_list = self.kb.get_subtopics(subject, topic)
            for subtopic in subtopic_list:
                if subtopic['name'].lower() in question.lower():
                    subtopics.append(subtopic)

        return {
            "topics": matched_topics,
            "subtopics": subtopics
        }

    def get_answer(self, question):
        parsed_data = self.parse_question(question)
        if not parsed_data["subjects"]:
            return "Sorry, I couldn't find the subject in the Knowledge Base."

        subject = parsed_data["subjects"][0]
        topic_data = self.match_topic_and_subtopic(subject, question)

        if topic_data["subtopics"]:
            return topic_data["subtopics"][0]["description"]

        if topic_data["topics"]:
            return f"I found the topic '{topic_data['topics'][0]}' in '{subject}', but the specific subtopic is not clear."

        return "No relevant information found for the question."
