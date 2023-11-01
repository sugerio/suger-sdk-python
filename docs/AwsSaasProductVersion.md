# AwsSaasProductVersion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_options** | [**List[AwsSaasProductDeliveryOption]**](AwsSaasProductDeliveryOption.md) |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.aws_saas_product_version import AwsSaasProductVersion

# TODO update the JSON string below
json = "{}"
# create an instance of AwsSaasProductVersion from a JSON string
aws_saas_product_version_instance = AwsSaasProductVersion.from_json(json)
# print the JSON string representation of the object
print AwsSaasProductVersion.to_json()

# convert the object into a dict
aws_saas_product_version_dict = aws_saas_product_version_instance.to_dict()
# create an instance of AwsSaasProductVersion from a dict
aws_saas_product_version_form_dict = aws_saas_product_version.from_dict(aws_saas_product_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


