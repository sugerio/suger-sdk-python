# AwsSaasProductDeliveryOption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fulfillment_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.aws_saas_product_delivery_option import AwsSaasProductDeliveryOption

# TODO update the JSON string below
json = "{}"
# create an instance of AwsSaasProductDeliveryOption from a JSON string
aws_saas_product_delivery_option_instance = AwsSaasProductDeliveryOption.from_json(json)
# print the JSON string representation of the object
print AwsSaasProductDeliveryOption.to_json()

# convert the object into a dict
aws_saas_product_delivery_option_dict = aws_saas_product_delivery_option_instance.to_dict()
# create an instance of AwsSaasProductDeliveryOption from a dict
aws_saas_product_delivery_option_form_dict = aws_saas_product_delivery_option.from_dict(aws_saas_product_delivery_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


