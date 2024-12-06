# BuyerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adyen_buyer** | [**AdyenBuyer**](AdyenBuyer.md) | Buyer on Adyen | [optional] 
**aws_buyer** | [**AwsAccountIdentifier**](AwsAccountIdentifier.md) | Buyer from AWS Marketplace | [optional] 
**azure_buyer** | [**AzureADIdentifier**](AzureADIdentifier.md) | Buyer from Azure Marketplace | [optional] 
**collectable_amount** | **float** | The amount that the seller can collect. It excludes the marketplace commision fee. | [optional] 
**company_info** | [**CompanyInfo**](CompanyInfo.md) |  | [optional] 
**customer_id** | **str** | customerID of buyer on seller&#39;s side | [optional] 
**disbursed_amount** | **float** | The amount that has been disbursed to the seller account. | [optional] 
**email_address** | **str** | The email address of the buyer. This was copied from the new client signup form. | [optional] 
**fields** | **Dict[str, object]** | Fields to store key-value pairs of buyer information. | [optional] 
**gcp_buyer** | [**GcpMarketplaceUserAccount**](GcpMarketplaceUserAccount.md) | Buyer from GCP Marketplace | [optional] 
**gross_amount** | **float** | The gross amount that the buyer has committed to pay, including usage metered amount. | [optional] 
**invoiced_amount** | **float** | The amount that the buyer has got invoiced. | [optional] 
**lago_customer_id** | **str** | The lgo customer ID for the buyer if it is connected to a lago customer. | [optional] 
**last_modified_by** | **str** | Last modifier user ID. | [optional] 
**metronome_customer_id** | **str** | The metronome customer ID for the buyer if it is connected to a metronome customer. | [optional] 
**orb_customer_id** | **str** | The orb customer ID for the buyer if it is connected to a orb customer. | [optional] 
**payment_config** | [**PaymentConfig**](PaymentConfig.md) | Payment Config for billing. | [optional] 
**spa_url** | **str** | Buyer SPA url, public page visited with jwt. | [optional] 
**stripe_buyer** | [**StripeCustomer**](StripeCustomer.md) | Buyer as Customer on Stripe | [optional] 

## Example

```python
from suger_sdk_python.models.buyer_info import BuyerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BuyerInfo from a JSON string
buyer_info_instance = BuyerInfo.from_json(json)
# print the JSON string representation of the object
print(BuyerInfo.to_json())

# convert the object into a dict
buyer_info_dict = buyer_info_instance.to_dict()
# create an instance of BuyerInfo from a dict
buyer_info_from_dict = BuyerInfo.from_dict(buyer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


