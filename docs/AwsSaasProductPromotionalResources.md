# AwsSaasProductPromotionalResources


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_resources** | [**List[AwsSaasProductAdditionalResource]**](AwsSaasProductAdditionalResource.md) |  | [optional] 
**logo_url** | **str** |  | [optional] 
**video_urls** | **List[str]** | Currently, AWS only support 1 url in the array. | [optional] 

## Example

```python
from openapi_client.models.aws_saas_product_promotional_resources import AwsSaasProductPromotionalResources

# TODO update the JSON string below
json = "{}"
# create an instance of AwsSaasProductPromotionalResources from a JSON string
aws_saas_product_promotional_resources_instance = AwsSaasProductPromotionalResources.from_json(json)
# print the JSON string representation of the object
print AwsSaasProductPromotionalResources.to_json()

# convert the object into a dict
aws_saas_product_promotional_resources_dict = aws_saas_product_promotional_resources_instance.to_dict()
# create an instance of AwsSaasProductPromotionalResources from a dict
aws_saas_product_promotional_resources_form_dict = aws_saas_product_promotional_resources.from_dict(aws_saas_product_promotional_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


