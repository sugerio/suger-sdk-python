# AwsMarketplaceEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**customer_identifier** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_free_trial_term_present** | **str** |  | [optional] 
**offer_identifier** | **str** |  | [optional] 
**product_code** | **str** |  | [optional] 
**suger_organization_id** | **str** | Populated by Suger Service. | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_event import AwsMarketplaceEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceEvent from a JSON string
aws_marketplace_event_instance = AwsMarketplaceEvent.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceEvent.to_json())

# convert the object into a dict
aws_marketplace_event_dict = aws_marketplace_event_instance.to_dict()
# create an instance of AwsMarketplaceEvent from a dict
aws_marketplace_event_from_dict = AwsMarketplaceEvent.from_dict(aws_marketplace_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


