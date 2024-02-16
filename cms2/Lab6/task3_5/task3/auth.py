import hashlib

def raise_func():
    raise KeyError("This is a KeyError")

def except_func():
    try:
        raise_func()
    except KeyError as e:
        print("Caught an exception:", repr(e))

class AuthException(Exception):
    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user


class UsernameAlreadyExists(AuthException):
    def __str__(self):
        return f"Username '{self.username}' already exists"

class PasswordTooShort(AuthException):
    def __init__(self, username):
        super().__init__(username)
        self.message = f"Password for '{username}' is too short"

    def __str__(self):
        return self.message


class InvalidUsername(AuthException):
    def __init__(self, username):
        super().__init__(username)
        self.message = f"Username '{username}' is invalid"

    def __str__(self):
        return self.message


class InvalidPassword(AuthException):
    def __init__(self, username):
        super().__init__(username)
        self.message = f"Invalid password for '{username}'"

    def __str__(self):
        return self.message


class PermissionError(Exception):
    def __init__(self, message, user=None, permission=None):
        self.message = message
        self.user = user
        self.permission = permission

    def __str__(self):
        if self.user and self.permission:
            return f"{self.message}: user '{self.user.username}' does not have permission '{self.permission}'"
        elif self.user:
            return f"{self.message}: user '{self.user.username}'"
        elif self.permission:
            return f"{self.message}: permission '{self.permission}'"
        else:
            return self.message

    @staticmethod
    def not_exists(permission):
        return PermissionError(f"Permission '{permission}' does not exist")

    @staticmethod
    def not_granted(user, permission):
        return PermissionError(f"User '{user.username}' does not have permission '{permission}'", user=user, permission=permission)

    @staticmethod
    def not_logged_in(user):
        return PermissionError("User is not logged in", user=user)


class NotLoggedInError(AuthException):
    def __init__(self, username):
        super().__init__(username)
        self.message = f"User '{username}' is not logged in"
    def __str__(self):
        return self.message

class NotPermittedError(AuthException):
    def __init__(self, username, permission):
        super().__init__(username)
        self.message = f"User '{username}' does not have permission '{permission}'"
    def __str__(self):
        return self.message


class User:
    def __init__(self, username, password):
        """Create a new user object. The password
        will be encrypted before storing."""
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password):
        """Encrypt the password with the username and return
        the sha digest."""
        hash_string = self.username + password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        """Return True if the password is valid for this
        user, false otherwise."""
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password


class Authenticator:
    def __init__(self):
        """Construct an authenticator to manage
        users logging in and out."""
        self.users = {}
    def add_user(self, username, password):
        if not self._is_valid_username(username):
            raise InvalidUsername(username)
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)

    def _is_valid_username(self, username):
        # Check if the username contains only alphanumeric characters
        return username.isalnum()

    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        if not user.check_password(password):
            raise InvalidPassword(username, user)

        user.is_logged_in = True
        return True

    def is_logged_in(self, user):
        if isinstance(user, str):
            user = self.users.get(user)
        return user and user.is_logged_in


class Authorizor:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name):
        """Create a new permission that users
        can be added to"""
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")

    def permit_user(self, perm_name, username):
        """Grant the given permission to the user"""
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username, perm_name)
            else:
                return True
authenticator = Authenticator()
authorizor = Authorizor(authenticator)