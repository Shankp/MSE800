import payment_processor


# Singleton class for Payment Gateway
class PaymentGateway:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PaymentGateway, cls).__new__(cls)
            cls._instance.gateway = None
        return cls._instance

    # Method to get the payment factory instance
    def get_payment_processor(self, method=None):
        if self.gateway is None:
            self.gateway = payment_processor.PaymentFactory().processor(method)
        return self.gateway
