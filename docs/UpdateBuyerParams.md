# UpdateBuyerParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | The customer ID to recognize the cloud marketplace buyer in your internal system. This may be used for uploading CSV files for Batch Metering Usage | [optional] 
**description** | **str** | The description of the buyer. If not provided, the description will not be updated. | [optional] 
**metronome_customer_id** | **str** | The Metronome Customer ID of the buyer. If not provided, the Metronome Customer ID will not be updated. | [optional] 
**name** | **str** | The name of the buyer. If not provided, the name will not be updated. | [optional] 
**orb_customer_id** | **str** | The Orb Customer ID of the buyer. If not provided, the Orb Customer ID will not be updated. | [optional] 

## Example

```python
from openapi_client.models.update_buyer_params import UpdateBuyerParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBuyerParams from a JSON string
update_buyer_params_instance = UpdateBuyerParams.from_json(json)
# print the JSON string representation of the object
print UpdateBuyerParams.to_json()

# convert the object into a dict
update_buyer_params_dict = update_buyer_params_instance.to_dict()
# create an instance of UpdateBuyerParams from a dict
update_buyer_params_form_dict = update_buyer_params.from_dict(update_buyer_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


