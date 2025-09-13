from abc import ABC, abstractmethod

# Abstract base class for payment processors
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

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

# Factory class to create payment processors
class PaymentFactory:
    # Factory method to get the appropriate payment processor
    @staticmethod
    def get_payment_processor(method):
        if method == "paypal":
            return PayPalPayment()
        elif method == "stripe":
            return StripePayment()
        elif method == "credit_card":
            return CreditCardPayment()
        else:
            raise ValueError("Unknown payment method")


# Client code
def checkout(payment_method, amount):
    processor = PaymentFactory.get_payment_processor(payment_method)
    return processor.process_payment(amount)


if __name__ == "__main__":
    print(checkout("paypal", 100))
    print(checkout("stripe", 200))
    print(checkout("credit_card", 300))


