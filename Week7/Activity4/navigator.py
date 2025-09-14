from Week7.Activity4.port_service import LogisticsFactory

# Singleton Navigator class
class Navigator:
    _instance = None

# Singleton instance accessor
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Navigator, cls).__new__(cls)
        return cls._instance

    def get_medium(self, method=None):
        if method is None:
            raise ValueError("Logistics method must be provided")

        return LogisticsFactory.get_logistics(method)
