# AwsProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**AwsProductDescription**](AwsProductDescription.md) |  | [optional] 
**dimensions** | [**List[AwsProductDimension]**](AwsProductDimension.md) |  | [optional] 
**promotional_resources** | [**AwsProductPromotionalResources**](AwsProductPromotionalResources.md) |  | [optional] 
**repositories** | [**List[AwsProductRepository]**](AwsProductRepository.md) |  | [optional] 
**signature_verification_keys** | [**List[AwsProductSignatureVerificationKey]**](AwsProductSignatureVerificationKey.md) |  | [optional] 
**support_information** | [**AwsProductSupportInformation**](AwsProductSupportInformation.md) |  | [optional] 
**versions** | [**List[AwsProductVersion]**](AwsProductVersion.md) |  | [optional] 
**data_feed_product_id** | **str** | The product Id in AWS Marketplace Data Feed Service. | [optional] 
**product_id** | **str** | AWS Product ID | [optional] 

## Example

```python
from suger_sdk_python.models.aws_product import AwsProduct

# TODO update the JSON string below
json = "{}"
# create an instance of AwsProduct from a JSON string
aws_product_instance = AwsProduct.from_json(json)
# print the JSON string representation of the object
print(AwsProduct.to_json())

# convert the object into a dict
aws_product_dict = aws_product_instance.to_dict()
# create an instance of AwsProduct from a dict
aws_product_from_dict = AwsProduct.from_dict(aws_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


