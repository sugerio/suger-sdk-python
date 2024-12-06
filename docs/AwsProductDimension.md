# AwsProductDimension


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**length** | **int** | The term length for the commit amount, such as 6 months, or 1 year. The length is used together with timeUnit. Length and TimeUnit are only used for commit dimension. | [optional] 
**name** | **str** |  | [optional] 
**rate** | **float** | Below three fields are only used for pass data when create or update product&#39;s public offer pricing. Rate is only used for update public offer, becasue rate will be set as 0.01 when create new product. | [optional] 
**time_unit** | [**TimeUnit**](TimeUnit.md) |  | [optional] 
**types** | **List[str]** |  | [optional] 
**unit** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_product_dimension import AwsProductDimension

# TODO update the JSON string below
json = "{}"
# create an instance of AwsProductDimension from a JSON string
aws_product_dimension_instance = AwsProductDimension.from_json(json)
# print the JSON string representation of the object
print(AwsProductDimension.to_json())

# convert the object into a dict
aws_product_dimension_dict = aws_product_dimension_instance.to_dict()
# create an instance of AwsProductDimension from a dict
aws_product_dimension_from_dict = AwsProductDimension.from_dict(aws_product_dimension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


