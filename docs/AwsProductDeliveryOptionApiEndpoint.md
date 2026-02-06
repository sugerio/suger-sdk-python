# AwsProductDeliveryOptionApiEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_types** | **List[str]** |  | [optional] 
**endpoint_url** | **str** |  | [optional] 
**integration_protocols** | [**List[AwsProductDeliveryOptionApiEndpointIntegrationProtocol]**](AwsProductDeliveryOptionApiEndpointIntegrationProtocol.md) |  | [optional] 
**schemas** | [**List[AwsProductDeliveryOptionApiEndpointSchema]**](AwsProductDeliveryOptionApiEndpointSchema.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_product_delivery_option_api_endpoint import AwsProductDeliveryOptionApiEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of AwsProductDeliveryOptionApiEndpoint from a JSON string
aws_product_delivery_option_api_endpoint_instance = AwsProductDeliveryOptionApiEndpoint.from_json(json)
# print the JSON string representation of the object
print(AwsProductDeliveryOptionApiEndpoint.to_json())

# convert the object into a dict
aws_product_delivery_option_api_endpoint_dict = aws_product_delivery_option_api_endpoint_instance.to_dict()
# create an instance of AwsProductDeliveryOptionApiEndpoint from a dict
aws_product_delivery_option_api_endpoint_from_dict = AwsProductDeliveryOptionApiEndpoint.from_dict(aws_product_delivery_option_api_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


