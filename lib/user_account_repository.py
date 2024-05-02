from lib.user_account import UserAccount

class UserAccountRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM user_accounts')
        user_accounts = []
        for row in rows:
            item = UserAccount(
                row["id"],
                row["email_address"],
                row["username"]
            )
            user_accounts.append(item)
        return user_accounts

    def find(self, user_account_id):
        rows = self._connection.execute('SELECT * FROM user_accounts WHERE id = %s', [user_account_id])
        row = rows[0]

        return UserAccount(
            row["id"],
            row["email_address"],
            row["username"])
    


