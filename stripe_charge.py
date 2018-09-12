import stripe

stripe.api_key = "sk_test_XXXXXXXXXXXXXXXXXXXXXXXXX"

def main():
    charge = stripe.Charge.create(
        amount='283',
        currency='jpy',
        customer='cus_XXXXXXXXXXXXXXX',
        description='test')
    print(charge)

if __name__ == '__main__':
    main()