import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from services import FollowerService


FAKE_FOLLOWERS_JSON = [
    {
        "title": "",
        "media_list_data": [],
        "string_list_data": [
            {"href": "https://www.instagram.com/alice", "value": "alice", "timestamp": 123}
        ],
    },
    {
        "title": "",
        "media_list_data": [],
        "string_list_data": [
            {"href": "https://www.instagram.com/bob", "value": "bob", "timestamp": 456}
        ],
    },
]

FAKE_FOLLOWING_JSON = {
    "relationships_following": [
        {
            "title": "",
            "media_list_data": [],
            "string_list_data": [
                {"href": "https://www.instagram.com/alice", "value": "alice", "timestamp": 123}
            ],
        },
        {
            "title": "",
            "media_list_data": [],
            "string_list_data": [
                {"href": "https://www.instagram.com/bob", "value": "bob", "timestamp": 456}
            ],
        },
        {
            "title": "",
            "media_list_data": [],
            "string_list_data": [
                {"href": "https://www.instagram.com/carol", "value": "carol", "timestamp": 789}
            ],
        },
    ]
}


def test_extract_accounts():
    service = FollowerService(FAKE_FOLLOWERS_JSON, FAKE_FOLLOWING_JSON)
    result = service._extract_accounts(FAKE_FOLLOWERS_JSON)
    assert result == ["alice", "bob"]


def test_unfollow_calculator():
    service = FollowerService(FAKE_FOLLOWERS_JSON, FAKE_FOLLOWING_JSON)
    result = service.unfollow_calculator()
    assert result == ["carol"]  # only Carol doesn’t follow back
