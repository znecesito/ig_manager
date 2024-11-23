class Pattern:
    def __init__(self, words, rule="any"):
        """
        Initialize a Pattern object.
        :param words: A list of words to match.
        :param rule: The rule for matching ('start', 'end', 'any').
        """
        if not isinstance(words, list):
            raise ValueError("Words must be a list of strings.")
        if rule not in {"start", "end", "any"}:
            raise ValueError("Rule must be one of 'start', 'end', or 'any'.")
        
        self.words = words
        self.rule = rule

    def matches(self, message):
        """
        Check if the pattern matches the given message.
        :param message: The message to check.
        :return: The matched word, or None if no match.
        """
        message = message.lower()
        for word in self.words:
            word = word.lower()
            if self.rule == "start" and message.startswith(word):
                return word
            elif self.rule == "end" and message.endswith(word):
                return word
            elif self.rule == "any" and word in message:
                return word
        return None
