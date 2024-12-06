# AwsProductAdditionalResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_product_additional_resource import AwsProductAdditionalResource

# TODO update the JSON string below
json = "{}"
# create an instance of AwsProductAdditionalResource from a JSON string
aws_product_additional_resource_instance = AwsProductAdditionalResource.from_json(json)
# print the JSON string representation of the object
print(AwsProductAdditionalResource.to_json())

# convert the object into a dict
aws_product_additional_resource_dict = aws_product_additional_resource_instance.to_dict()
# create an instance of AwsProductAdditionalResource from a dict
aws_product_additional_resource_from_dict = AwsProductAdditionalResource.from_dict(aws_product_additional_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


