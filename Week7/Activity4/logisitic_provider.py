from abc import ABC, abstractmethod


class Logistics(ABC):
    @abstractmethod
    def deliver(self, item):
        pass

# Factory class to create logistics providers
class LogisticsFactory:
    @staticmethod
    def get_logistics(method):
        if method == "road":
            return RoadLogistics()
        elif method == "sea":
            return SeaLogistics()
        else:
            raise ValueError("Unknown logistics method")


class RoadLogistics(Logistics):
    def deliver(self, item):
        return f"Delivering {item} by road."


class SeaLogistics(Logistics):
    def deliver(self, item):
        return f"Delivering {item} by sea."
