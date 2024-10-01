import json
import os

def message_regulator(first_message):

    hi_pattern = {'hi', 'hello', 'hey', 'hi!', 'hey!', 'hello!', 'hi,', 'hello,', 'hey,'}

    first_word = first_message.lower().split()[0]
    last_word = first_message.lower().split()[-1]

    # if first_word == 'why':
    #     print(first_message)

    if first_word in hi_pattern:
        return "Hey/Hi/Hello ...."

    if last_word == 'question':
        return "I have a question/quick question"

    return first_word

def message_tracker():

    message_dict = {}
    
    for subdir, dirs, files in os.walk('messages/inbox/'):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(".json"): 
                #print(filepath)
                with open(filepath, 'r') as f:
                    account_inbox = json.load(f)

                    message_thread = len(account_inbox['messages']) - 1
                    try:
                        first_message = account_inbox['messages'][message_thread]['content']
                        # print(first_message)
                    except Exception as e:
                        first_message = "-------------------------- First message does not have content"

                    fmessage_key = message_regulator(first_message)

                    if fmessage_key in message_dict:
                        message_dict[fmessage_key] += 1
                    else:
                        message_dict[fmessage_key] = 1

    print(message_dict)
    # print(sorted(message_dict, key=message_dict.get, reverse=True))

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
