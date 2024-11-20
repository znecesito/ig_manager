import os
from models import MessageOpener
from data.json_reader import load_json

class MessageOpenerService:
    def __init__(self, message_dir, patterns):
        """
        Initializes the service with the path to the message data file and patterns.

        :param message_dir: Path to the message data file.
        :param patterns: List of patterns to identify message openers.

        """
        self.message_dir = message_dir
        self._patterns = patterns
        self._message_openers = set()

    def _response_checker(self, messages):
        for message in messages:
            if message['sender_name'] != 'zacknecesito':
                return True
        return False

    def _update_response_in_opener_set(self, pattern):
        dummy_opener = MessageOpener(pattern)

        for opener in self._message_openers:
            if opener == dummy_opener:
                opener.add_to_response_count()
                return

    def _add_message_opener_to_set(self, pattern):
        new_opener = MessageOpener(pattern)

        # Check if an opener with the same pattern already exists in the set
        for opener in self._message_openers:
            if opener == new_opener:
                opener.total_count += 1  # Increase the count if a opener with the same make and model exists
                return

        self._message_openers.add(MessageOpener(pattern))  # Add the new opener to the set if it doesn't exist

    def _load_all_messages(self):
        """Loads all message threads from JSON files, including those in subdirectories."""
        messages = []
        for root, _, files in os.walk(self.message_dir):  # Recursively traverse subdirectories
            for filename in files:
                if filename.endswith('.json'):
                    file_path = os.path.join(root, filename)
                    messages.append(load_json(file_path))
        return messages

    def _pattern_identifier(self, message_pattern):

        first_word = message_pattern.lower().split()[0]
        last_word = message_pattern.lower().split()[-1]

        for pattern in self._patterns:
            for word in pattern:
                if word in message_pattern:
                    return '|'.join(pattern)
        
        return 'Random Pattern'

        # hi_pattern = {'hi', 'hello', 'hey', 'hi!', 'hey!', 'hello!', 'hi,', 'hello,', 'hey,'}

        # first_word = message_pattern.lower().split()[0]
        # last_word = message_pattern.lower().split()[-1]


        # if 'english' in message_pattern.lower():
        #     return "English or <insert language>?"
        # elif first_word in hi_pattern:
        #     return "Hey/Hi/Hello <name>"
        # elif last_word == 'question':
        #     return "I have a question/quick question"
        # elif 'exception' in message_pattern.lower():
        #     return message_pattern
        # else:
        #     return "Random opener (immature, hard to quantify through data)"

    def message_opener_calculator(self):
        messages = self._load_all_messages()

        for message in messages:
            try:
                first_message = message['messages'][-1]['content']
            except Exception as e:
                # first_message = "Exception: First message was unsent"
                self._add_message_opener_to_set("Exception: First message was unsent")
                continue

            # Identify the first message pattern from the message
            first_message_pattern = self._pattern_identifier(first_message.lower())

            # Add message opener to set or increase existing one by 1
            self._add_message_opener_to_set(first_message_pattern)

            if self._response_checker(message['messages']):
                self._update_response_in_opener_set(first_message_pattern)

        return self._message_openers

    