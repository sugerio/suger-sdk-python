# OriginalEulaInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_eula_urls** | **List[str]** | The URL of the additional EULA files. Only applicable when EulaType &#x3D; CUSTOM. The additional EULA files will be attached to the EULA file in the EulaUrl, and form a single EULA file. | [optional] 
**additional_reseller_eula_urls** | **List[str]** | The URL of the additional reseller EULA files. Only applicable when ResellerEulaType &#x3D; CUSTOM. | [optional] 
**attach_eula_type** | [**EulaType**](EulaType.md) | Attach the standard EULA file to the CUSTOM EULA file. Only applicable when EulaType &#x3D; CUSTOM | [optional] 
**eula_merge_order** | **List[int]** | The merge order of the EULA files. Only applicable when EulaType &#x3D; CUSTOM. Elements are the original index of the EULA files in the index they should be transferred to, where original indexes are: AttachEulaType is index 0, EulaUrl is index 1, additionalEulaUrls is index 2 onwards. | [optional] 
**eula_type** | [**EulaType**](EulaType.md) | The type of the EULA. | [optional] 
**eula_url** | **str** | The URL of the EULA file. | [optional] 
**reseller_attach_eula_type** | [**EulaType**](EulaType.md) | Attach the standard EULA file to the CUSTOM EULA file. Only applicable when EulaType &#x3D; CUSTOM | [optional] 
**reseller_eula_type** | [**EulaType**](EulaType.md) | The type of the reseller EULA. Only applicable for CPPO offers. | [optional] 
**reseller_eula_url** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.original_eula_info import OriginalEulaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OriginalEulaInfo from a JSON string
original_eula_info_instance = OriginalEulaInfo.from_json(json)
# print the JSON string representation of the object
print(OriginalEulaInfo.to_json())

# convert the object into a dict
original_eula_info_dict = original_eula_info_instance.to_dict()
# create an instance of OriginalEulaInfo from a dict
original_eula_info_from_dict = OriginalEulaInfo.from_dict(original_eula_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


