# ClientDescribeInstanceResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_json** | **str** |  | [optional] 
**auto_renewal** | **str** |  | [optional] 
**began_on** | **int** |  | [optional] 
**component_json** | **str** |  | [optional] 
**constraints** | **str** |  | [optional] 
**created_on** | **int** |  | [optional] 
**end_on** | **int** |  | [optional] 
**extend_json** | **str** |  | [optional] 
**host_json** | **str** |  | [optional] 
**instance_id** | **int** |  | [optional] 
**is_trial** | **bool** |  | [optional] 
**modules** | [**ClientDescribeInstanceResponseBodyModules**](ClientDescribeInstanceResponseBodyModules.md) |  | [optional] 
**order_id** | **int** |  | [optional] 
**product_code** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**product_sku_code** | **str** |  | [optional] 
**product_type** | **str** |  | [optional] 
**relational_data** | [**ClientDescribeInstanceResponseBodyRelationalData**](ClientDescribeInstanceResponseBodyRelationalData.md) |  | [optional] 
**status** | **str** |  | [optional] 
**supplier_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.client_describe_instance_response_body import ClientDescribeInstanceResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ClientDescribeInstanceResponseBody from a JSON string
client_describe_instance_response_body_instance = ClientDescribeInstanceResponseBody.from_json(json)
# print the JSON string representation of the object
print ClientDescribeInstanceResponseBody.to_json()

# convert the object into a dict
client_describe_instance_response_body_dict = client_describe_instance_response_body_instance.to_dict()
# create an instance of ClientDescribeInstanceResponseBody from a dict
client_describe_instance_response_body_form_dict = client_describe_instance_response_body.from_dict(client_describe_instance_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


