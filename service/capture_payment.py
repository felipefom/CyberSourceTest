from CyberSource import *
import process_payment
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "config", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def capture_a_payment():
    try:

        
        # Getting the payment_id dynamically using process_a_payment method
        api_payment_response = process_payment.process_a_payment(
            False)
        payment_id = api_payment_response.id
        print("Ta dentro miseravis2")
        # Setting the json message body
        request = CapturePaymentRequest()
        client_reference = Ptsv2paymentsClientReferenceInformation()
        client_reference.code = "8200"
        request.client_reference_information = client_reference.__dict__

        amount_details = Ptsv2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "8200"
        amount_details.currency = "BRL"
        order_information = Ptsv2paymentsOrderInformation()
        order_information.amount_details = amount_details.__dict__
        request.order_information = order_information.__dict__

        message_body = (json.dumps(request.__dict__))
        print(message_body)

        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        capture_obj = CaptureApi(details_dict1)
        return_data, status, body = capture_obj.capture_payment(message_body, payment_id)
        print("----------> Capture Payment ")
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
        return return_data
    except Exception as e:
        print("Exception when calling CaptureApi->capture_payment: %s\n" % e)


if __name__ == "__main__":
    capture_a_payment()
