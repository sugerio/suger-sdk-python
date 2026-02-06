# CreateBuyerParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adyen_customer_id** | **str** | Adyen customerId of this buyer. If not provided but Partner is ADYEN, will create a new customer on Adyen. | [optional] 
**chargebee_customer_id** | **str** | The Chargebee Customer ID of the buyer. If not provided, the Chargebee Customer ID will not be updated. | [optional] 
**company_info** | [**CompanyInfo**](CompanyInfo.md) | Optional. CompanyInfo of the buyer. | [optional] 
**customer_id** | **str** | The customer ID to recognize the cloud marketplace buyer in your internal system. | [optional] 
**description** | **str** | The description of the buyer. | [optional] 
**lago_customer_id** | **str** | Optional. The Lago Customer ID of the buyer. | [optional] 
**metronome_customer_id** | **str** | Optional. The Metronome Customer ID of the buyer. | [optional] 
**name** | **str** | The name of the buyer. | [optional] 
**orb_customer_id** | **str** | Optional. The Orb Customer ID of the buyer. | [optional] 
**partner** | [**Partner**](Partner.md) | The channel partner where this buyer is billed. Only STRIPE &amp; ADYEN are supported at the moment. | [optional] 
**payment_config** | [**PaymentConfig**](PaymentConfig.md) | Payment config for billing. | [optional] 
**quickbooks_customer_id** | **str** | The Quickbooks Customer ID of the buyer. If not provided, the Quickbooks Customer ID will not be updated. | [optional] 
**stripe_customer_id** | **str** | Stripe customerId of this buyer. If not provided but Partner is STRIPE, will create a new customer on stripe. | [optional] 

## Example

```python
from suger_sdk_python.models.create_buyer_params import CreateBuyerParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBuyerParams from a JSON string
create_buyer_params_instance = CreateBuyerParams.from_json(json)
# print the JSON string representation of the object
print(CreateBuyerParams.to_json())

# convert the object into a dict
create_buyer_params_dict = create_buyer_params_instance.to_dict()
# create an instance of CreateBuyerParams from a dict
create_buyer_params_from_dict = CreateBuyerParams.from_dict(create_buyer_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


