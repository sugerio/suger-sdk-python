# AwsProductVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_date** | **datetime** |  | [optional] 
**delivery_options** | [**List[AwsProductDeliveryOption]**](AwsProductDeliveryOption.md) |  | [optional] 
**id** | **str** |  | [optional] 
**release_notes** | **str** |  | [optional] 
**version_title** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_product_version import AwsProductVersion

# TODO update the JSON string below
json = "{}"
# create an instance of AwsProductVersion from a JSON string
aws_product_version_instance = AwsProductVersion.from_json(json)
# print the JSON string representation of the object
print(AwsProductVersion.to_json())

# convert the object into a dict
aws_product_version_dict = aws_product_version_instance.to_dict()
# create an instance of AwsProductVersion from a dict
aws_product_version_from_dict = AwsProductVersion.from_dict(aws_product_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


