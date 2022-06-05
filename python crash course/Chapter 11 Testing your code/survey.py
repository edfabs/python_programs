class AnonymousSurvey:
    """Collect anonymous answers to a survey qusttion."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_questions(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all th responses that have been given."""
        print("Surevy results:")
        for response in self.responses:
            print(f"- {response}")
