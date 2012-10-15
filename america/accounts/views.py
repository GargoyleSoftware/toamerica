# Create your views here.

from django.conf import settings

def view_that_asks_for_money(request):
    # What you want the button to do.
    paypal_dict = {
        "business": "yourpaypalemail@example.com",
        "amount": "10000000.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": "http://www.example.com/your-ipn-location/",
        "return_url": "http://www.example.com/your-return-location/",
        "cancel_return": "http://www.example.com/your-cancel-location/",

    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render_to_response("payment.html", context)


def subscribe(request):
    # What you want the button to do.
    paypal_dict = {
    "cmd": "_xclick-subscriptions",
	"business": settings.PAYPAL_RECEIVER_EMAIL,
	"a1": "0",	                   # trial price
	"p1": 1,	                   # trial duration, duration of unit defaults to month
	"a3": "29.95",                     # yearly price
	"p3": 1,                           # duration of each unit (depends on unit)
	"t3": "Y",                         # duration unit ("M for Month")
    "src": "1",                        # make payments recur
	"sra": "1",                        # reattempt payment on payment error
	"no_note": "1",                    # remove extra notes (optional)
    "item_name": "PayPal Shows This To The User",
    "invoice": "101",
    "notify_url": "http://example.com/something/hard/to/guess/",
    "return_url": "http://example.com/thanks/",
    "cancel_return": "http://example.com/cancel/",
    "custom": request.user.username,   # put whatever data you need to track things here
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict, button_type="subscribe")

    context = {"form": form, "encoded_email" : urlquote(settings.PAYPAL_RECEIVER_EMAIL), "paid" : request.user.get_profile().paid}
