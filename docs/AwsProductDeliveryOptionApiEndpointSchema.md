# AwsProductDeliveryOptionApiEndpointSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_url** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_product_delivery_option_api_endpoint_schema import AwsProductDeliveryOptionApiEndpointSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AwsProductDeliveryOptionApiEndpointSchema from a JSON string
aws_product_delivery_option_api_endpoint_schema_instance = AwsProductDeliveryOptionApiEndpointSchema.from_json(json)
# print the JSON string representation of the object
print(AwsProductDeliveryOptionApiEndpointSchema.to_json())

# convert the object into a dict
aws_product_delivery_option_api_endpoint_schema_dict = aws_product_delivery_option_api_endpoint_schema_instance.to_dict()
# create an instance of AwsProductDeliveryOptionApiEndpointSchema from a dict
aws_product_delivery_option_api_endpoint_schema_from_dict = AwsProductDeliveryOptionApiEndpointSchema.from_dict(aws_product_delivery_option_api_endpoint_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


