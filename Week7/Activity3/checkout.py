from Payment_gateway import PaymentGateway

# Client code
def checkout(payment_method, amount):
    gateway = PaymentGateway()
    processor = gateway.get_payment_processor(payment_method)
    return processor.process_payment(amount)


if __name__ == "__main__":

    gateway = PaymentGateway()


    processor = gateway.get_payment_processor("paypal")
    paypal_payment = processor.process_payment(100)
    print(paypal_payment)

    processor = gateway.get_payment_processor("stripe")
    stripe_payment = processor.process_payment(200)
    print(stripe_payment)

    processor = gateway.get_payment_processor("credit_card")
    credit_card_payment = processor.process_payment(300)
    print(credit_card_payment)
   


