from abc import ABC, abstractmethod


# Abstract base class for payment processors
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


# Factory class to create payment processors
class PaymentFactory:
    @staticmethod
    def processor(method):
        if method == "paypal":
            return PayPalPayment()
        elif method == "stripe":
            return StripePayment()
        elif method == "credit_card":
            return CreditCardPayment()
        else:
            raise ValueError("Unknown payment method")


# Concrete payment processor classes
class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"


# Concrete payment processor classes
class StripePayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Stripe"


# Concrete payment processor classes
class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"
