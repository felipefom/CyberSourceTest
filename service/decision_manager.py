from CyberSource import *
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "config", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def decision_manager_with_buyer_information():
    try:
        # Setting the json message body
        request = CreateDecisionManagerCaseRequest()
        client_reference = Riskv1decisionsClientReferenceInformation()
        client_reference.code = "6690"
        request.client_reference_information = client_reference.__dict__

        processing_info = Riskv1decisionsPaymentInformation()

        request.processing_information = processing_info.__dict__

        order_information = Riskv1decisionsOrderInformation()
		
        bill_to = Riskv1decisionsOrderInformationBillTo()
        bill_to.country = "US"
        bill_to.last_name = "smith"
        bill_to.address1 = "96, powers street."
        bill_to.postal_code = "03055"
        bill_to.locality = "Clearwater milford"
        bill_to.administrative_area = "NH"
        bill_to.first_name = "James"
        bill_to.phone_number = "7606160717"
        bill_to.company = "Visa"
        bill_to.email = "test@cybs.com"

        amount_details = Riskv1decisionsOrderInformationAmountDetails("BRL")
        amount_details.total_amount = "6690"

        order_information.bill_to = bill_to.__dict__
        order_information.amount_details = amount_details.__dict__
        request.order_information = order_information.__dict__

        payment_info = Riskv1decisionsPaymentInformation()
        card = Riskv1decisionsPaymentInformationCard()
        card.expiration_year = "2031"
        card.number = "4444444444444448"
        card.expiration_month = "12"
        payment_info.card = card.__dict__
        request.payment_information = payment_info.__dict__

        buyer_information = Riskv1decisionsBuyerInformation()
        buyer_information.hashed_password = ""
        buyer_information.date_of_birth = "1987-5-5"
        buyer_information.personal_identification = []

        personal_identification0 = Ptsv2paymentsBuyerInformationPersonalIdentification()
        personal_identification0.type = "CPF"
        personal_identification0.id = "1a23apwe98"
        buyer_information.personal_identification.append(personal_identification0.__dict__)

        request.buyer_information = buyer_information.__dict__
        
        message_body = json.dumps(request.__dict__)

        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()

        dm_obj = DecisionManagerApi(details_dict1)
        return_data, status, body = dm_obj.create_decision_manager_case(message_body)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)

        return status
    except Exception as e:
        print("Exception when calling DecisionManagerApi->create_decision_manager_case: %s\n" % e)


if __name__ == "__main__":
    decision_manager_with_buyer_information()
