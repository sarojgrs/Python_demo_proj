class Logger:
    def log(self, message):
        print(f"[Logger] {message}")


class UserService:
    def __init__(self, logger):
        self.logger = logger

    def register_user(self, username):
        self.logger.log(f"User '{username}' registered successfully.")


# Creating instances of dependencies
logger = Logger()
user_service = UserService(logger)

# Using the UserService
user_service.register_user("John")
