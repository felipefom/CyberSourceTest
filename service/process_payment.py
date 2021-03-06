from CyberSource import *
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "config", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def process_a_payment(flag):
    try:
        # Setting the json message body
        request = CreatePaymentRequest()
        client_reference = Ptsv2paymentsClientReferenceInformation()
        client_reference.code = "8200"
        request.client_reference_information = client_reference.__dict__

        processing_info = Ptsv2paymentsProcessingInformation()

        if flag:
            processing_info.capture = "true"

        request.processing_information = processing_info.__dict__

        aggregator_info = Ptsv2paymentsAggregatorInformation()
        sub_merchant = Ptsv2paymentsAggregatorInformationSubMerchant()
        sub_merchant.card_acceptor_id = "1234567890"
        sub_merchant.country = "BR"
        sub_merchant.phone_number = "650-432-0000"
        sub_merchant.address1 = "900 Metro Center"
        sub_merchant.postal_code = "94404-2775"
        sub_merchant.locality = "Foster City"
        sub_merchant.name = "Visa Inc"
        sub_merchant.administrative_area = "CA"
        sub_merchant.region = "PEN"
        sub_merchant.email = "test@cybs.com"
        aggregator_info.sub_merchant = sub_merchant.__dict__
        aggregator_info.name = "V-Internatio"
        aggregator_info.aggregator_id = "123456789"
        request.aggregator_information = aggregator_info.__dict__

        order_information = Ptsv2paymentsOrderInformation()
        bill_to = Ptsv2paymentsOrderInformationBillTo()
        bill_to.country = "BR"
        bill_to.last_name = "Moreira"
        bill_to.address2 = "Rua Ferucio Brinatti"
        bill_to.address1 = "Rua Ferucio Brinatti"
        bill_to.postal_code = "06394050"
        bill_to.locality = "Carapicuiba"
        bill_to.administrative_area = "SP"
        bill_to.first_name = "Felipe"
        bill_to.phone_number = "11963081304"
        bill_to.district = "SP"
        bill_to.building_number = "313"
        bill_to.company = "Visa"
        bill_to.email = "test@cybs.com"

        amount_details = Ptsv2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "8200"
        amount_details.currency = "BRL"

        order_information.bill_to = bill_to.__dict__
        order_information.amount_details = amount_details.__dict__

        payment_info = Ptsv2paymentsPaymentInformation()
        card = Ptsv2paymentsPaymentInformationCard()
        card.expiration_year = "2031"
        card.number = "4111111111111111"
        card.security_code = "123"
        card.expiration_month = "12"
        card.type = "001"
        payment_info.card = card.__dict__
        request.payment_information = payment_info.__dict__

        request.order_information = order_information.__dict__

        message_body = json.dumps(request.__dict__)

        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        payment_obj = PaymentsApi(details_dict1)
        return_data, status, body = payment_obj.create_payment(message_body)
        print("----------> Process Payment ")
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("Exception when calling PaymentsApi->create_payment: %s\n" % e)


if __name__ == "__main__":
    process_a_payment(False)
