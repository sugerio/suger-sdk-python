# AwsProductDeliveryOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ami_alias** | **str** | Exclusive Fields For AWS AMI Product | [optional] 
**fulfillment_url** | **str** | Exclusive Fields For AWS SaaS Product | [optional] 
**id** | **str** |  | [optional] 
**recommendations** | **object** |  | [optional] 
**short_description** | **str** |  | [optional] 
**source_id** | **str** |  | [optional] 
**title** | **str** | Exclusive Fields For AWS Container Product | [optional] 
**type** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_product_delivery_option import AwsProductDeliveryOption

# TODO update the JSON string below
json = "{}"
# create an instance of AwsProductDeliveryOption from a JSON string
aws_product_delivery_option_instance = AwsProductDeliveryOption.from_json(json)
# print the JSON string representation of the object
print(AwsProductDeliveryOption.to_json())

# convert the object into a dict
aws_product_delivery_option_dict = aws_product_delivery_option_instance.to_dict()
# create an instance of AwsProductDeliveryOption from a dict
aws_product_delivery_option_from_dict = AwsProductDeliveryOption.from_dict(aws_product_delivery_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


