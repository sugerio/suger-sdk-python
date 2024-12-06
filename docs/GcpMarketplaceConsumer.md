# GcpMarketplaceConsumer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | **str** | The project name with format &#x60;projects/&#x60;. | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_consumer import GcpMarketplaceConsumer

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceConsumer from a JSON string
gcp_marketplace_consumer_instance = GcpMarketplaceConsumer.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceConsumer.to_json())

# convert the object into a dict
gcp_marketplace_consumer_dict = gcp_marketplace_consumer_instance.to_dict()
# create an instance of GcpMarketplaceConsumer from a dict
gcp_marketplace_consumer_from_dict = GcpMarketplaceConsumer.from_dict(gcp_marketplace_consumer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


