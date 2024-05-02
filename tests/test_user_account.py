from lib.user_account import UserAccount



def test_user_accounts_constructs():
    user_account = UserAccount(1, 'bob@hot.co.uk', 'bobby')
    assert user_account.id == 1
    assert user_account.email_address == 'bob@hot.co.uk'
    assert user_account.username == 'bobby'


def test_user_accounts_equal():
    user_account1 = UserAccount(1, 'bob@hot.co.uk', 'bobby')
    user_account2 = UserAccount(1, 'bob@hot.co.uk', 'bobby')
    assert user_account1 == user_account2


def test_user_account_format():
    user_account = UserAccount(1, 'bob@hot.co.uk', 'bobby')
    assert str(user_account) == "UserAccount(1, bob@hot.co.uk, bobby)"