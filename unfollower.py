import json
import os
from messageopener import MessageOpener

def message_regulator(first_message):

    hi_pattern = {'hi', 'hello', 'hey', 'hi!', 'hey!', 'hello!', 'hi,', 'hello,', 'hey,'}

    first_word = first_message.lower().split()[0]
    last_word = first_message.lower().split()[-1]

    # if first_word == 'idk':
    #     print(first_message)

    if 'english' in first_message.lower():
        return "English or <insert language>?"
    elif first_word in hi_pattern:
        return "Hey/Hi/Hello ...."
    elif last_word == 'question':
        return "I have a question/quick question"

    return first_word

def message_tracker():

    # obj = MessageOpener(19)
    # obj.print_value()
    # exit()

    message_opener_set = {}
    
    for subdir, dirs, files in os.walk('messages/inbox/'):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(".json"): 
                #print(filepath)
                with open(filepath, 'r') as f:
                    message_thread = json.load(f)

                    message_thread_length = len(message_thread['messages']) - 1
                    try:
                        first_message = message_thread['messages'][message_thread_length]['content']
                        # print(first_message)
                    except Exception as e:
                        continue
                        # first_message = "-------------------------- First message does not have content"

                    opening_line_pattern = message_regulator(first_message)

                    if opening_line_pattern in message_opener_set:
                        message_opener_set[opening_line_pattern] += 1
                    else:
                        message_opener_set[opening_line_pattern] = 1

    print(message_opener_set)
    # print(sorted(message_opener_set, key=message_opener_set.get, reverse=True))

def open_file_paths(input_file):

    directory_path = input("Enter file path for %s: " % (input_file))

    with open(directory_path, 'r') as f:
        return json.load(f)

def list_accounts(account_array):
    account_list = []

    for json_object in account_array:
        account = json_object['string_list_data'][0]
        account_list.append(account['value'])

    return account_list

def unfollow_calculator(followers, following):
    count = 0

    for account in following:
        if account in followers:
            continue
        else:
            count += 1
            print("%d\t%s" % (count,account))  

def main():

    message_tracker()
    exit()
    following_array = open_file_paths('following')
    follower_array = open_file_paths('followers')
    following_array = following_array['relationships_following']
    following_accounts = list_accounts(following_array)
    follower_accounts = list_accounts(follower_array)

    print("These dickheads aren't following you back:")

    unfollow_calculator(follower_accounts, following_accounts)

if __name__ == "__main__":
         main()
