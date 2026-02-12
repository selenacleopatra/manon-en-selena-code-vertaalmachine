class Vertaalmachine:
    def __init__(self):
        self.translations = {}  # Dictionary to hold translations
        self.verbs = {}  # Dictionary to hold verb conjugations
        self.questions = []  # List to hold quiz questions

    def load_translations(self, filename):
        """Load translations from a file"""
        with open(filename, 'r') as file:
            self.translations = eval(file.read())  # Assuming file contains a dict

    def add_translation(self, word, translation):
        """Add a new translation"""
        self.translations[word] = translation

    def check_answer(self, word, answer):
        """Check if the provided answer is correct"""
        return self.translations.get(word) == answer

    def conjugate_verb(self, verb, tense):
        """Conjugate a verb based on the tense"""
        return self.verbs.get(verb, {}).get(tense, "")

    def load_verbs(self, filename):
        """Load verb conjugations from a file"""
        with open(filename, 'r') as file:
            self.verbs = eval(file.read())  # Assuming file contains a dict

    def interactive_learning(self):
        """An interactive learning session"""
        print("Welcome to the Vertaalmachine interactive learning session!")
        for word in self.translations:
            answer = input(f"What is the translation for '{word}'? ")
            if self.check_answer(word, answer):
                print("Correct!")
            else:
                print(f"Incorrect. The correct translation is '{self.translations[word]}'.")

    def start(self):
        """Start the translation machine"""
        print("Starting Vertaalmachine...")
        self.interactive_learning()

if __name__ == '__main__':
    machine = Vertaalmachine()
    machine.load_translations('translations.txt')  # Load translations from a file
    machine.load_verbs('verbs.txt')  # Load verbs from a file
    machine.start()  # Start the machine