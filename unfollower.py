import json

def message_tracker():
    
    with open('messages/inbox/aadya_1361219638612809/message_1.json', 'r') as f:
        message_thread = json.load(f)

    print(message_thread['messages'][1]['content'])

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

    #message_tracker()

    following_array = open_file_paths('following')
    follower_array = open_file_paths('followers')
    following_array = following_array['relationships_following']
    following_accounts = list_accounts(following_array)
    follower_accounts = list_accounts(follower_array)

    print("These dickheads aren't following you back:")

    unfollow_calculator(follower_accounts, following_accounts)

if __name__ == "__main__":
         main()
