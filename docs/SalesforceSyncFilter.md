# SalesforceSyncFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | [optional] 
**operator** | [**SalesforceSyncFilterOperator**](SalesforceSyncFilterOperator.md) |  | [optional] 
**value** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.salesforce_sync_filter import SalesforceSyncFilter

# TODO update the JSON string below
json = "{}"
# create an instance of SalesforceSyncFilter from a JSON string
salesforce_sync_filter_instance = SalesforceSyncFilter.from_json(json)
# print the JSON string representation of the object
print SalesforceSyncFilter.to_json()

# convert the object into a dict
salesforce_sync_filter_dict = salesforce_sync_filter_instance.to_dict()
# create an instance of SalesforceSyncFilter from a dict
salesforce_sync_filter_form_dict = salesforce_sync_filter.from_dict(salesforce_sync_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


