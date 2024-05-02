from lib.user_account import UserAccount
from lib.user_account_repository import UserAccountRepository

def test_for_all_user_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserAccountRepository(db_connection)

    user_accounts = repository.all()

    assert user_accounts == [
        UserAccount(1, 'bob@hot.co.uk', 'bobby'),
        UserAccount(2, 'lol@yahoo.com', 'lolol'),
        UserAccount(3, 'yoyo@joke.com', 'yoyoyoyo')
    ]


def test_for_find_user_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserAccountRepository(db_connection)

    user_account = repository.find(2)
    assert user_account == UserAccount(2, 'lol@yahoo.com', 'lolol')