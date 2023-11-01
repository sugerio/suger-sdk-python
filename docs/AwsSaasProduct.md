# AwsSaasProduct


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**AwsSaasProductDescription**](AwsSaasProductDescription.md) |  | [optional] 
**dimensions** | [**List[AwsSaasProductDimension]**](AwsSaasProductDimension.md) |  | [optional] 
**promotional_resources** | [**AwsSaasProductPromotionalResources**](AwsSaasProductPromotionalResources.md) |  | [optional] 
**support_information** | [**AwsSaasProductSupportInformation**](AwsSaasProductSupportInformation.md) |  | [optional] 
**versions** | [**List[AwsSaasProductVersion]**](AwsSaasProductVersion.md) |  | [optional] 
**data_feed_product_id** | **str** | The product Id in AWS Marketplace Data Feed Service. | [optional] 
**product_id** | **str** | AWS Product ID | [optional] 

## Example

```python
from openapi_client.models.aws_saas_product import AwsSaasProduct

# TODO update the JSON string below
json = "{}"
# create an instance of AwsSaasProduct from a JSON string
aws_saas_product_instance = AwsSaasProduct.from_json(json)
# print the JSON string representation of the object
print AwsSaasProduct.to_json()

# convert the object into a dict
aws_saas_product_dict = aws_saas_product_instance.to_dict()
# create an instance of AwsSaasProduct from a dict
aws_saas_product_form_dict = aws_saas_product.from_dict(aws_saas_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


