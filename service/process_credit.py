from CyberSource import *
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "config", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def process_a_credit():
    try:
        # Setting the json message body
        request = CreateCreditRequest()
        client_reference = Ptsv2paymentsClientReferenceInformation()
        client_reference.code = "6680"
        request.client_reference_information = client_reference.__dict__

        order_information = Ptsv2paymentsOrderInformation()
        amount_details = Ptsv2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "6680"
        amount_details.currency = "BRL"
        bill_to = Ptsv2paymentsOrderInformationBillTo()
        bill_to.country = "BR"
        bill_to.first_name = "Felipe"
        bill_to.last_name = "Moreira"
        bill_to.address1 = "Rua Ferucio Brinatti"
        bill_to.phone_number = "11963081304"
        bill_to.postal_code = "06394050"
        bill_to.locality = "Carapicuiba"
        bill_to.administrative_area = "SP"
        bill_to.email = "test@cybs.com"
        order_information.amount_details = amount_details.__dict__
        order_information.bill_to = bill_to.__dict__

        payment_information = Ptsv2paymentsPaymentInformation()
        card_information = Ptsv2paymentsPaymentInformationCard()
        card_information.expiration_month = "12"
        card_information.expiration_year = "2031"
        card_information.type = "001"
        card_information.number = "4111111111111111"
        payment_information.card = card_information.__dict__
        request.order_information = order_information.__dict__
        request.payment_information = payment_information.__dict__
        message_body = json.dumps(request.__dict__)
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        credit_obj = CreditApi(details_dict1)
        return_data, status, body = credit_obj.create_credit(message_body)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
        return return_data

    except Exception as e:
        print("Exception when calling CreditApi->create_credit: %s\n" % e)


if __name__ == "__main__":
    process_a_credit()
