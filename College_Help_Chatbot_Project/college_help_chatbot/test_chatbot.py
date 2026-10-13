"""Basic offline tests for the College Help Chatbot."""
import unittest
from chatbot import get_response


class CollegeChatbotTests(unittest.TestCase):
    def test_greeting(self):
        self.assertIn("Welcome to College Help Chatbot", get_response("hello"))

    def test_admissions_rule(self):
        self.assertIn("Admissions", get_response("How do I apply for admission?"))

    def test_fees_rule(self):
        self.assertIn("Fees", get_response("Tell me about tuition fees"))

    def test_unknown_question_fallback(self):
        self.assertIn("don't have a rule", get_response("Can you order pizza?"))

    def test_blank_input(self):
        self.assertIn("Please type a question", get_response("   "))


if __name__ == "__main__":
    unittest.main()
