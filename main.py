class PromptologyAnalyzer:
    def __init__(self):
        self.keywords = ['role', 'persona', 'context', 'format', 'output', 'step-by-step']
    def get_score(self, prompt):
        words = prompt.lower().split()
        matches = sum(1 for w in self.keywords if w in words)
        return round((matches / len(self.keywords)) * 100, 2)

if __name__ == "__main__":
    prompt = "Act as an expert. Provide a step-by-step plan in a table format."
    analyzer = PromptologyAnalyzer()
    print(f"Prompt Quality: {analyzer.get_score(prompt)}%")
  
