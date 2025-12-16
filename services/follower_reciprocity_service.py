from data.json_reader import load_json

class FollowerService:
    def __init__(self, followers, following):
        # Accept either file paths (str) or already-loaded JSON (dict/list)
        self.follower_data = load_json(followers) if isinstance(followers, str) else followers
        self.following_data = load_json(following) if isinstance(following, str) else following

    def _extract_following(self, json_data):
        """Further manipulates json to return a list of pure account usernames."""
        account_list = []
        for json_object in json_data:
            account = json_object
            account_list.append(account['title'])
        return account_list

    def _extract_followers(self, json_data):
        """Further manipulates json to return a list of pure account usernames."""
        account_list = []
        for json_object in json_data:
            account = json_object['string_list_data'][0]
            account_list.append(account['value'])
        return account_list

    def unfollow_calculator(self):
        """Finds users who are not following back."""
        followers = self._extract_followers(self.follower_data)
        following = self._extract_following(self.following_data['relationships_following'])

        non_followers = [user for user in following if user not in followers]
        return non_followers
