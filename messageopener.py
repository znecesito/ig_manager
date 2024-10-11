class MessageOpener:
    def __init__(self, pattern):
        self.pattern = pattern
        self.total_count = 1 # Initialize count to 1 when the object is created

    def __eq__(self, other):
        """Two MessageOpener objects are considered equal if they have the same pattern."""
        if isinstance(other, MessageOpener):
            return self.pattern == other.pattern
        return False

    def __hash__(self):
        """The hash is based on pattern so that we can store MessageOpener objects in sets or dictionaries."""
        return hash((self.pattern))

    def __repr__(self):
        return f"Opener(pattern='{self.pattern}', count={self.total_count})"
