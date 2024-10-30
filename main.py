import json
import os
# from models import MessageOpener
from services.follower_reciprocity_service import FollowerService

def response_checker(messages):
    for message in messages:
        if message['sender_name'] != 'zacknecesito':
            return True
    return False

def update_response_in_opener_set(message_opener_set, pattern):
    dummy_opener = MessageOpener(pattern)

    if dummy_opener in message_opener_set:
        for opener in message_opener_set:
            if opener == dummy_opener:
                opener.response()
                break
    else:
        print("Opener is not in set")

def add_message_opener_to_set(message_opener_set, pattern):
    new_opener = MessageOpener(pattern)

    # Check if an opener with the same pattern already exists in the set
    if new_opener in message_opener_set:
        for opener in message_opener_set:
            if opener == new_opener:
                opener.total_count += 1  # Increase the count if a opener with the same make and model exists
                break
    else:
        message_opener_set.add(new_opener)  # Add the new opener to the set if it doesn't exist

def message_regulator(first_message):

    hi_pattern = {'hi', 'hello', 'hey', 'hi!', 'hey!', 'hello!', 'hi,', 'hello,', 'hey,'}

    first_word = first_message.lower().split()[0]
    last_word = first_message.lower().split()[-1]

    # if first_word == 'idk':
    #     print(first_message)

    if 'english' in first_message.lower():
        return "English or <insert language>?"
    elif first_word in hi_pattern:
        return "Hey/Hi/Hello <name>"
    elif last_word == 'question':
        return "I have a question/quick question"
    elif 'exception' in first_message.lower():
        return first_message
    else:
        return "Random opener (immature, hard to quantify through data)"


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

def run_follower_analysis():
    
    # Define paths to JSON files
    follower_file = os.path.join('data','connections', 'followers_1.json')
    following_file = os.path.join('data', 'connections', 'following.json')

    # Initialize the FollowerService
    follower_service = FollowerService(follower_file, following_file)

    # Perform follower reciprocity check
    non_followers = follower_service.unfollow_calculator()

    print("These are the dickheads who aren't following you back:")
    for user in non_followers:
        print(f"{user}")

def main():
    run_follower_analysis()

if __name__ == "__main__":
        main()
