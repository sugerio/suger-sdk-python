# ProductInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alibaba_product** | [**AlibabaMarketplaceProduct**](AlibabaMarketplaceProduct.md) |  | [optional] 
**attributes** | **Dict[str, str]** |  | [optional] 
**aws_saas_product** | [**AwsSaasProduct**](AwsSaasProduct.md) |  | [optional] 
**aws_sns_subscriptions** | [**List[AwsSnsSubscription]**](AwsSnsSubscription.md) |  | [optional] 
**azure_product** | [**AzureProduct**](AzureProduct.md) |  | [optional] 
**azure_product_resource** | [**AzureMarketplaceProductResource**](AzureMarketplaceProductResource.md) |  | [optional] 
**commits** | [**List[CommitDimension]**](CommitDimension.md) |  | [optional] 
**currency** | **str** |  | [optional] 
**dimensions** | [**List[MeteringDimension]**](MeteringDimension.md) |  | [optional] 
**eula_url** | **str** |  | [optional] 
**gcp_product** | [**GcpMarketplaceProduct**](GcpMarketplaceProduct.md) |  | [optional] 
**refund_cancelation_policy** | **str** |  | [optional] 
**seller_notes** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.product_info import ProductInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProductInfo from a JSON string
product_info_instance = ProductInfo.from_json(json)
# print the JSON string representation of the object
print ProductInfo.to_json()

# convert the object into a dict
product_info_dict = product_info_instance.to_dict()
# create an instance of ProductInfo from a dict
product_info_form_dict = product_info.from_dict(product_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


