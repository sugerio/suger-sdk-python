# AwsSaasProductDimension


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**types** | **List[str]** |  | [optional] 
**unit** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.aws_saas_product_dimension import AwsSaasProductDimension

# TODO update the JSON string below
json = "{}"
# create an instance of AwsSaasProductDimension from a JSON string
aws_saas_product_dimension_instance = AwsSaasProductDimension.from_json(json)
# print the JSON string representation of the object
print AwsSaasProductDimension.to_json()

# convert the object into a dict
aws_saas_product_dimension_dict = aws_saas_product_dimension_instance.to_dict()
# create an instance of AwsSaasProductDimension from a dict
aws_saas_product_dimension_form_dict = aws_saas_product_dimension.from_dict(aws_saas_product_dimension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


