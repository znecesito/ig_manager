import json
import os
from data.json_reader import load_json
from services import FollowerService
from services import MessageOpenerService


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

def run_message_analysis():

    # Define paths to JSON files
    message_dir = os.path.join('data', 'messages', 'inbox')
    pattern_dir = os.path.join('data', 'config', 'default_patterns.json')

    patterns = load_json(pattern_dir)['patterns']

    message_service = MessageOpenerService(message_dir, patterns)

    openers_and_response_rates_set = message_service.message_opener_calculator()
    print("Response rates by opener:")
    for opener in openers_and_response_rates_set:
        print(opener)

def main():
    user_task = input("What would you like to do today? \n\n1) Follower Reciprocity Analysis\n2) Message Opener Response Calculator\n\nSelect a number please: ")
    
    if user_task == '1':
        run_follower_analysis()
    elif user_task == '2':
        run_message_analysis()
    else:
        print("Did not select correctly. Try Again.")

if __name__ == "__main__":
        main()
