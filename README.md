import json
import os
import sys
from typing import Dict, List, Tuple, Optional

class VertaalMachine:
    """Een offline vertaalmachine voor Nederlands-Frans (thema: eten)"""
    
    def __init__(self, database_path: str = "words_database.json"):
        """Initialiseer de vertaalmachine met een woordenlijst"""
        self.database_path = database_path
        self.words_db = self._load_database()
        self.history = []
        
    def _load_database(self) -> Dict:
        """Laad de woordenlijst uit een JSON-bestand"""
        if os.path.exists(self.database_path):
            with open(self.database_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            raise FileNotFoundError(f"Database niet gevonden: {self.database_path}")
    
    def translate_word(self, dutch_word: str) -> Optional[Dict]:
        """Vertaal een Nederlands woord naar het Frans"""
        dutch_word = dutch_word.lower().strip()
        
        for entry in self.words_db.get("woorden", []):
            if entry["nederlands"].lower() == dutch_word:
                return entry
        
        return None
    
    def check_answer(self, dutch_word: str, user_answer: str) -> Tuple[bool, str]:
        """Controleer of het gegeven antwoord correct is"""
        user_answer = user_answer.lower().strip()
        translation = self.translate_word(dutch_word)
        
        if translation is None:
            return False, f"❌ '{dutch_word}' niet in database gevonden."
        
        correct_french = translation["frans"].lower()
        
        if user_answer == correct_french:
            return True, f"✅ Correct! '{dutch_word}' = '{translation['frans']}'"
        else:
            return False, f"❌ Fout! Het juiste antwoord is: '{translation['frans']}'"
    
    def get_conjugation(self, dutch_word: str, tense: str = "present") -> Optional[Dict]:
        """Geef werkwoordvervoegingen voor verschillende tijden"""
        translation = self.translate_word(dutch_word)
        
        if translation is None or "conjugations" not in translation:
            return None
        
        conjugations = translation.get("conjugations", {})
        return conjugations.get(tense, None)
    
    def get_random_words(self, count: int = 5) -> List[Dict]:
        """Geef willekeurige woorden voor oefening"""
        import random
        return random.sample(self.words_db.get("woorden", []), min(count, len(self.words_db.get("woorden", []))))
    
    def quiz_mode(self, num_questions: int = 10) -> Dict:
        """Interactieve quiz-modus"""
        import random
        
        score = 0
        words = self.get_random_words(num_questions)
        results = []
        
        print("\n" + "="*60)
        print("🎓 QUIZ MODE - Vertaal Nederlands naar Frans (Thema: Eten)")
        print("="*60 + "\n")
        
        for i, word_entry in enumerate(words, 1):
            dutch = word_entry["nederlands"]
            print(f"Vraag {i}/{num_questions}: Wat is het Franse woord voor '{dutch}'?")
            user_input = input("Jouw antwoord: ").strip()
            
            is_correct, message = self.check_answer(dutch, user_input)
            print(message)
            
            if is_correct:
                score += 1
            
            results.append({
                "word": dutch,
                "user_answer": user_input,
                "correct": is_correct
            })
            print()
        
        percentage = (score / num_questions) * 100
        print("="*60)
        print(f"📊 Quiz afgerond! Score: {score}/{num_questions} ({percentage:.1f}%)")
        print("="*60 + "\n")
        
        return {"score": score, "total": num_questions, "percentage": percentage, "results": results}
    
    def interactive_mode(self):
        """Interactieve vertalingsmodus"""
        print("\n" + "="*60)
        print("🌐 INTERACTIEVE VERTAALMACHINE - Nederlands ➔ Frans")
        print("Thema: Eten | Voor alle leeftijden (8-99 jaar)")
        print("="*60)
        print("\nOpdrachten:")
        print("  'vertaal <woord>' - Vertaal een Nederlands woord")
        print("  'check <woord> <antwoord>' - Controleer jouw antwoord")
        print("  'voeg <woord>' - Voeg nieuw woord toe aan quiz")
        print("  'quiz [aantal]' - Start quiz-modus (standaard 10 vragen)")
        print("  'conjugatie <werkwoord> [tense]' - Toon werkwoordvervoegingen")
        print("  'toon [aantal]' - Toon willekeurige woorden")
        print("  'exit' - Afsluiten")
        print("="*60 + "\n")
        
        while True:
            command = input("📝 Voer een opdracht in: ").strip().lower()
            
            if command == "exit":
                print("\n👋 Tot ziens! Veel succes met Frans leren!")
                break
            
            elif command.startswith("vertaal "):
                word = command.replace("vertaal ", "").strip()
                translation = self.translate_word(word)
                if translation:
                    print(f"✅ {translation['nederlands']} = {translation['frans']}")
                    if "beschrijving" in translation:
                        print(f"   📖 {translation['beschrijving']}")
                else:
                    print(f"❌ '{word}' niet gevonden in database.")
            
            elif command.startswith("check "):
                parts = command.replace("check ", "").split(" ", 1)
                if len(parts) == 2:
                    dutch, answer = parts
                    is_correct, message = self.check_answer(dutch, answer)
                    print(message)
                else:
                    print("❌ Gebruik: check <nederlands woord> <jouw antwoord>")
            
            elif command.startswith("conjugatie "):
                parts = command.replace("conjugatie ", "").split()
                word = parts[0]
                tense = parts[1] if len(parts) > 1 else "present"
                
                conjugation = self.get_conjugation(word, tense)
                if conjugation:
                    print(f"✅ Vervoegingen voor '{word}' ({tense}):")
                    for pronoun, form in conjugation.items():
                        print(f"   {pronoun}: {form}")
                else:
                    print(f"❌ Geen vervoegingen gevonden voor '{word}'")
            
            elif command.startswith("toon "):
                try:
                    count = int(command.replace("toon ", ""))
                    words = self.get_random_words(count)
                    print(f"\n📚 {count} willekeurige woorden:")
                    for w in words:
                        print(f"   • {w['nederlands']} = {w['frans']}")
                except ValueError:
                    print("❌ Voer een getal in.")
            
            elif command.startswith("quiz"):
                try:
                    num = int(command.replace("quiz", "").strip()) if "quiz " in command else 10
                    self.quiz_mode(num)
                except ValueError:
                    print("❌ Voer een geldig getal in.")
            
            else:
                print("❌ Onbekende opdracht. Probeer opnieuw.")
            
            print()


def main():
    """Hoofdfunctie"""
    try:
        vm = VertaalMachine("words_database.json")
        vm.interactive_mode()
    except FileNotFoundError as e:
        print(f"❌ Fout: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
