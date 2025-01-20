# UpdateBuyerParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_info** | [**CompanyInfo**](CompanyInfo.md) | Optional. CompanyInfo of the buyer. | [optional] 
**customer_id** | **str** | The customer ID to recognize the cloud marketplace buyer in your internal system. This may be used for uploading CSV files for Batch Metering Usage | [optional] 
**description** | **str** | The description of the buyer. If not provided, the description will not be updated. | [optional] 
**lago_customer_id** | **str** | The Lago Customer ID of the buyer. If not provided, the Lago Customer ID will not be updated. | [optional] 
**metronome_customer_id** | **str** | The Metronome Customer ID of the buyer. If not provided, the Metronome Customer ID will not be updated. | [optional] 
**name** | **str** | The name of the buyer. If not provided, the name will not be updated. | [optional] 
**orb_customer_id** | **str** | The Orb Customer ID of the buyer. If not provided, the Orb Customer ID will not be updated. | [optional] 
**payment_config** | [**PaymentConfig**](PaymentConfig.md) | Optional. PaymentConfig of the buyer. The currency can&#39;t be updated. | [optional] 
**stripe_customer_id** | **str** | The Stripe Customer ID of the buyer. If not provided, the Stripe Customer ID will not be updated. | [optional] 

## Example

```python
from suger_sdk_python.models.update_buyer_params import UpdateBuyerParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBuyerParams from a JSON string
update_buyer_params_instance = UpdateBuyerParams.from_json(json)
# print the JSON string representation of the object
print(UpdateBuyerParams.to_json())

# convert the object into a dict
update_buyer_params_dict = update_buyer_params_instance.to_dict()
# create an instance of UpdateBuyerParams from a dict
update_buyer_params_from_dict = UpdateBuyerParams.from_dict(update_buyer_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


