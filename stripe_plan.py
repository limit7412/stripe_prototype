import stripe

stripe.api_key = "sk_test_XXXXXXXXXXXXXXXXXXXXXXXXX"

def main():
    subscription = stripe.Subscription.create(
        customer='cus_XXXXXXXXXXXXXXX',
        plan='plan_XXXXXXXXXXXXXXX')
    print(subscription)

if __name__ == '__main__':
    main()