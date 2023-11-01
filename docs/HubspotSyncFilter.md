# HubspotSyncFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** |  | [optional] 
**property_name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.hubspot_sync_filter import HubspotSyncFilter

# TODO update the JSON string below
json = "{}"
# create an instance of HubspotSyncFilter from a JSON string
hubspot_sync_filter_instance = HubspotSyncFilter.from_json(json)
# print the JSON string representation of the object
print HubspotSyncFilter.to_json()

# convert the object into a dict
hubspot_sync_filter_dict = hubspot_sync_filter_instance.to_dict()
# create an instance of HubspotSyncFilter from a dict
hubspot_sync_filter_form_dict = hubspot_sync_filter.from_dict(hubspot_sync_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


