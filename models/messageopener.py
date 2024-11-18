class MessageOpener:
    def __init__(self, pattern):
        self.pattern = pattern
        self.total_count = 1 # Total count this opener was used
        self.response_count = 0 # Response count for this opener

    def add_to_response_count(self):
        '''Increase response count by 1 every time someone responds'''
        self.response_count += 1

    def response_ratio(self):
        if self.total_count == 0:
            return 0  # Avoid division by zero
        return self.response_count / self.total_count

    def __eq__(self, other):
        """Two MessageOpener objects are considered equal if they have the same pattern."""
        if isinstance(other, MessageOpener):
            return self.pattern == other.pattern
        return False

    def __hash__(self):
        """The hash is based on pattern so that we can store MessageOpener objects in sets or dictionaries."""
        return hash((self.pattern))

    def __repr__(self):
        return f"Opener: '{self.pattern}'\n    Number of times sent: {self.total_count}\n    Number of responses: {self.response_count}\n    Response rate: {round(self.response_ratio()*100, 2)}%"
