# AwsProductDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_products** | **object** |  | [optional] 
**categories** | **List[str]** |  | [optional] 
**eu_w8_submitted** | **bool** |  | [optional] 
**highlights** | **List[str]** |  | [optional] 
**long_description** | **str** |  | [optional] 
**manufacturer** | **str** |  | [optional] 
**product_code** | **str** |  | [optional] 
**product_title** | **str** |  | [optional] 
**registered** | **bool** |  | [optional] 
**search_keywords** | **List[str]** |  | [optional] 
**short_description** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**us_w9_submitted** | **bool** |  | [optional] 
**visibility** | [**AwsMarketplaceProductVisibility**](AwsMarketplaceProductVisibility.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_product_description import AwsProductDescription

# TODO update the JSON string below
json = "{}"
# create an instance of AwsProductDescription from a JSON string
aws_product_description_instance = AwsProductDescription.from_json(json)
# print the JSON string representation of the object
print(AwsProductDescription.to_json())

# convert the object into a dict
aws_product_description_dict = aws_product_description_instance.to_dict()
# create an instance of AwsProductDescription from a dict
aws_product_description_from_dict = AwsProductDescription.from_dict(aws_product_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


