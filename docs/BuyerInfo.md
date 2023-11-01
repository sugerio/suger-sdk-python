# BuyerInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_buyer** | [**AwsAccountIdentifier**](AwsAccountIdentifier.md) |  | [optional] 
**azure_buyer** | [**AzureADIdentifier**](AzureADIdentifier.md) |  | [optional] 
**collectable_amount** | **float** | The amount that the seller can collect. It excludes the marketplace commision fee. | [optional] 
**customer_id** | **str** | customerID of buyer on seller&#39;s side | [optional] 
**disbursed_amount** | **float** | The amount that has been disbursed to the seller account. | [optional] 
**gcp_buyer** | [**GcpMarketplaceUserAccount**](GcpMarketplaceUserAccount.md) |  | [optional] 
**invoiced_amount** | **float** | The amount that the buyer has got invoiced. | [optional] 
**metronome_customer_id** | **str** | The metronome customer ID for the buyer if it is connected to a metronome customer. | [optional] 
**orb_customer_id** | **str** | The orb customer ID for the buyer if it is connected to a orb customer. | [optional] 

## Example

```python
from openapi_client.models.buyer_info import BuyerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BuyerInfo from a JSON string
buyer_info_instance = BuyerInfo.from_json(json)
# print the JSON string representation of the object
print BuyerInfo.to_json()

# convert the object into a dict
buyer_info_dict = buyer_info_instance.to_dict()
# create an instance of BuyerInfo from a dict
buyer_info_form_dict = buyer_info.from_dict(buyer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


