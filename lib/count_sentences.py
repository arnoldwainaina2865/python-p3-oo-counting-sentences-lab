class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value  # triggers the setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        import re
        # Use regular expression to split by '.', '?', or '!', possibly repeated
        sentences = re.split(r'[.!?]+', self.value)
        # Filter out empty strings and strings that are only whitespace
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)
