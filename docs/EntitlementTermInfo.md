# EntitlementTermInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension_quantity_decimal_parts** | **Dict[str, float]** | The decimal part of the dimension quantity, in format of &lt;dimensionKey, decimalPart&gt; It is used to save the decimal part of the dimension quantity for AWS Marketplace only. Because AWS Marketplace only accepts integer for dimension quantity. If the dimension quantity is a decimal number, we need to save the decimal part for future use. | [optional] 
**is_commit_divided** | **bool** | Whether the commit is divided into multiple sub entitlement terms. If true, it has subEntitlementTermIds. | [optional] 
**parent_entitlement_term_id** | **str** | The partner&#39;s entitlement term ID. It stands for the partner&#39;s entitlement term. Applicable to the sub entitlement term only. | [optional] 
**sub_entitlement_term_ids** | **List[str]** | All sub entitlement terms id of this entitlement term if it is commit divided. | [optional] 
**type** | [**EntitlementTermType**](EntitlementTermType.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.entitlement_term_info import EntitlementTermInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementTermInfo from a JSON string
entitlement_term_info_instance = EntitlementTermInfo.from_json(json)
# print the JSON string representation of the object
print(EntitlementTermInfo.to_json())

# convert the object into a dict
entitlement_term_info_dict = entitlement_term_info_instance.to_dict()
# create an instance of EntitlementTermInfo from a dict
entitlement_term_info_from_dict = EntitlementTermInfo.from_dict(entitlement_term_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


