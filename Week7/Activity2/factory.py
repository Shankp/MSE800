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

class PayPalPayment:
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"

class StripePayment:
    def process_payment(self, amount):
        return f"Processing ${amount} via Stripe"

class CreditCardPayment:
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"

def checkout(payment_method, amount):
    processor = PaymentFactory.get_payment_processor(payment_method)
    return processor.process_payment(amount)


# Example usage
if __name__ == "__main__":
    print(checkout("paypal", 100))
    print(checkout("stripe", 200))
    print(checkout("credit_card", 300))


