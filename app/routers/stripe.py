import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi import Request
import stripe

# Load your Stripe secret key from an environment variable
stripe.api_key = 'sk_test_51Pr59aAy6NGVe8IXwmbkhCn6XmezszKfhFfR6SkaVmyRJYX1iJa7eYivC6x3vUvxFJEkcN0ejXl1nNWldLBsq0Rz00rAZEQdqs'

# Request model for payment data
class PaymentRequest(BaseModel):
    payment_method_id: str
    amount: int  # Amount in cents
    currency: str
    # description: str

router = APIRouter()
@router.post("/create-payment-intent/")
async def create_payment_intent(payment: PaymentRequest):
    try:
        # Create a PaymentIntent on the server side
        intent = stripe.PaymentIntent.create(
            amount=payment.amount,
            currency=payment.currency,
            payment_method=payment.payment_method_id,
            # description=payment.description,
            confirm=True,  # Automatically confirm the payment
            automatic_payment_methods={
                "enabled": True,  # Automatically process payments
                "allow_redirects": "never",  # Disable redirects
            },
        )
        return {"status": "success", "payment_intent": intent}

    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=f"Payment failed: {str(e)}")

@router.post("/webhook/")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get('stripe-signature')
    webhook_secret = os.getenv('STRIPE_WEBHOOK_SECRET')

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)

        if event['type'] == 'payment_intent.succeeded':
            intent = event['data']['object']
            print(f"PaymentIntent for {intent['amount']} was successful!")

        return {"status": "success"}

    except Exception as e:
        return {"status": "failed", "error": str(e)}
