from data.json_reader import load_json

class FollowerService:
	def __init__(self, follower_file, following_file):
		self.follower_file = follower_file
		self.following_file = following_file

	def _extract_accounts(self, json_data):
		"""Further manipulates json to return a list of pure account usernames."""
		account_list = []

		for json_object in json_data:
			account = json_object['string_list_data'][0]
			account_list.append(account['value'])

		return account_list

	def unfollow_calculator(self):
		"""Finds users who are not following back."""
		followers = self._extract_accounts(load_json(self.follower_file))
		following = self._extract_accounts(load_json(self.following_file)['relationships_following'])

		non_followers = []
		for user in following:
			if user not in followers:
				non_followers.append(user)

		return non_followers
