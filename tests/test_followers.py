import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from services import FollowerService


'''
Fake json data
Get's string_list_data json object's first value in list
Then gets the value of key 'value'
'''
FAKE_FOLLOWERS_JSON = [
    {
        "title": "",
        "media_list_data": [],
        "string_list_data": [{"href": "https://www.instagram.com/alice", "value": "alice", "timestamp": 123}]
    },
    {
        "title": "",
        "media_list_data": [],
        "string_list_data": [{"href": "https://www.instagram.com/bob", "value": "bob", "timestamp": 456}]
    }
]

FAKE_FOLLOWING_JSON = {
    "relationships_following": [
        {
            "title": "",
            "media_list_data": [],
            "string_list_data": [{"href": "https://www.instagram.com/alice", "value": "alice", "timestamp": 123}]
        },
        {
            "title": "",
            "media_list_data": [],
            "string_list_data": [{"href": "https://www.instagram.com/bob", "value": "bob", "timestamp": 456}]
        },
        {
            "title": "",
            "media_list_data": [],
            "string_list_data": [{"href": "https://www.instagram.com/carol", "value": "carol", "timestamp": 789}]
        }
    ]
}


def test_extract_accounts():
    service = FollowerService("fake_followers.json", "fake_following.json")
    result = service._extract_accounts(FAKE_FOLLOWERS_JSON) # since no actual files are passed, we use internal function _extract_accounts
    assert result == ["alice", "bob"] # nonetheless, result should still return the right values


def test_unfollow_calculator(monkeypatch):
    # Patch load_json to return fake data instead of reading from disk
    def fake_load_json(path):
        if "followers" in path:
            return FAKE_FOLLOWERS_JSON
        if "following" in path:
            return FAKE_FOLLOWING_JSON
        return {}

    # Apply the monkeypatch to the module since unfollow_calculator uses load_json function
    from services import follower_reciprocity_service
    monkeypatch.setattr(follower_reciprocity_service, "load_json", fake_load_json)

    service = FollowerService("fake_followers.json", "fake_following.json")
    result = service.unfollow_calculator()

    assert result == ["carol"]  # only Carol doesn’t follow back