from Payment_gateway import PaymentGateway

# Client code
def checkout(payment_method, amount):
    gateway = PaymentGateway()
    processor = gateway.get(payment_method)
    return processor.process_payment(amount)


if __name__ == "__main__":
    print(checkout("paypal", 100))
    print(checkout("stripe", 200))
    print(checkout("credit_card", 300))


