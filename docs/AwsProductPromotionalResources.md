# AwsProductPromotionalResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_resources** | [**List[AwsProductAdditionalResource]**](AwsProductAdditionalResource.md) |  | [optional] 
**logo_url** | **str** |  | [optional] 
**videos** | [**List[AwsProductVideo]**](AwsProductVideo.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_product_promotional_resources import AwsProductPromotionalResources

# TODO update the JSON string below
json = "{}"
# create an instance of AwsProductPromotionalResources from a JSON string
aws_product_promotional_resources_instance = AwsProductPromotionalResources.from_json(json)
# print the JSON string representation of the object
print(AwsProductPromotionalResources.to_json())

# convert the object into a dict
aws_product_promotional_resources_dict = aws_product_promotional_resources_instance.to_dict()
# create an instance of AwsProductPromotionalResources from a dict
aws_product_promotional_resources_from_dict = AwsProductPromotionalResources.from_dict(aws_product_promotional_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


