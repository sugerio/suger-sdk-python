# AwsSaasProductDescription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_products** | **str** |  | [optional] 
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
**visibility** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.aws_saas_product_description import AwsSaasProductDescription

# TODO update the JSON string below
json = "{}"
# create an instance of AwsSaasProductDescription from a JSON string
aws_saas_product_description_instance = AwsSaasProductDescription.from_json(json)
# print the JSON string representation of the object
print AwsSaasProductDescription.to_json()

# convert the object into a dict
aws_saas_product_description_dict = aws_saas_product_description_instance.to_dict()
# create an instance of AwsSaasProductDescription from a dict
aws_saas_product_description_form_dict = aws_saas_product_description.from_dict(aws_saas_product_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


