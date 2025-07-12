from question_matching_engine import QuestionMatchingEngine

class AnswerRetrieval:
    def __init__(self, knowledge_base_path='knowledge_base.json'):
        self.qme = QuestionMatchingEngine(knowledge_base_path)

    def retrieve_answer(self, question):
        answer = self.qme.get_answer(question)
        
        if "Sorry" in answer or "No relevant information" in answer:
            return {
                "status": "not_found",
                "message": answer
            }
        
        if "I found the topic" in answer:
            return {
                "status": "partial_match",
                "message": answer
            }
        
        return {
            "status": "found",
            "message": answer
        }


