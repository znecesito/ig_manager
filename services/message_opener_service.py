import os
from data.json_reader import load_json

class MessageOpenerService:
	def message_tracker():

    message_opener_set = set()
    
    for subdir, dirs, files in os.walk('messages/inbox/'):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(".json"): 
                #print(filepath)
                with open(filepath, 'r') as f:
                    message_thread = json.load(f)

                    # message_thread_length = len(message_thread['messages']) - 1
                    try:
                        first_message = message_thread['messages'][-1]['content']
                    except Exception as e:
                        first_message = "Exception: First message was unsent"

                    opening_line_pattern = message_regulator(first_message) # Finds pattern in opener. Maybe should rename it to patternfinder
                    
                    add_message_opener_to_set(message_opener_set, opening_line_pattern) # Adding new opener object to set and adding to count if it object already exists within set                    
                    
                    if response_checker(message_thread['messages']):
                        update_response_in_opener_set(message_opener_set, opening_line_pattern)
    print("Let's check your field goal percentage gangy")
    for opener in message_opener_set:
        print(opener)
    print("Yeah give up. What Future say? Chase a check. Never chase a b***.")