# AzureListingContact


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_listing_contact import AzureListingContact

# TODO update the JSON string below
json = "{}"
# create an instance of AzureListingContact from a JSON string
azure_listing_contact_instance = AzureListingContact.from_json(json)
# print the JSON string representation of the object
print AzureListingContact.to_json()

# convert the object into a dict
azure_listing_contact_dict = azure_listing_contact_instance.to_dict()
# create an instance of AzureListingContact from a dict
azure_listing_contact_form_dict = azure_listing_contact.from_dict(azure_listing_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


