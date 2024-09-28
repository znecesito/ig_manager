import json
import os

def message_tracker():
    
    for subdir, dirs, files in os.walk('messages/inbox/'):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(".json"): 
                #print(filepath)
                with open(filepath, 'r') as f:
                    message_thread = json.load(f)

                    first_message = len(message_thread['messages']) - 1
                    try:
                        #dummy = message_thread['messages'][first_message]['content']
                        print(message_thread['messages'][first_message]['content'])
                    except Exception as e:
                        #print("-------------------------- First message does not have content")
                        #print(filepath)
                        print(e)
                        continue

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
