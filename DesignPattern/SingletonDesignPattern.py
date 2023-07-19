class Singleton:
    _instance = None  # Private class attribute to store the singleton instance

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = Singleton()  # Create the singleton instance if it doesn't exist
        return cls._instance
