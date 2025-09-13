import payment_processor
import threading

# Singleton class for Payment Gateway
class PaymentGateway:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(PaymentGateway, cls).__new__(cls)
                    cls._instance.gateway = None
        return cls._instance

    def get(self):
        if self.gateway is None:
            self.gateway = payment_processor.PaymentFactory()
        return self.gateway
