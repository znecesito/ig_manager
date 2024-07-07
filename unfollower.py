import json

following_count = 0
follower_count = 0

with open('connections/following.json', 'r') as f:
    following_array = json.load(f)

with open('connections/followers_1.json', 'r') as f:
    follower_array = json.load(f)


following_dict = following_array['relationships_following']
following_list = []
follower_list = []

for json_object in following_dict:
    account = json_object['string_list_data'][0]
    following_list.append(account['value'])
    following_count += 1

for json_object in follower_array:
    account = json_object['string_list_data'][0]
    follower_list.append(account['value'])
    follower_count += 1

print("These dickheads aren't following you back:")

count = 0
for account in following_list:
    if account in follower_list:
        continue
    else:
        count += 1
        print("%d\t%s" % (count,account))
