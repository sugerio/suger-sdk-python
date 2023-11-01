# ClientDescribeOrderResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_quantity** | **int** |  | [optional] 
**ali_uid** | **int** |  | [optional] 
**components** | **Dict[str, object]** |  | [optional] 
**coupon_price** | **float** |  | [optional] 
**created_on** | **int** |  | [optional] 
**instance_ids** | [**ClientDescribeOrderResponseBodyInstanceIds**](ClientDescribeOrderResponseBodyInstanceIds.md) |  | [optional] 
**order_id** | **int** |  | [optional] 
**order_status** | **str** |  | [optional] 
**order_type** | **str** |  | [optional] 
**original_price** | **float** |  | [optional] 
**paid_on** | **int** |  | [optional] 
**pay_status** | **str** |  | [optional] 
**payment_price** | **float** |  | [optional] 
**period_type** | **str** |  | [optional] 
**product_code** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**product_sku_code** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**request_id** | **str** |  | [optional] 
**supplier_company_name** | **str** |  | [optional] 
**supplier_telephones** | [**ClientDescribeOrderResponseBodySupplierTelephones**](ClientDescribeOrderResponseBodySupplierTelephones.md) |  | [optional] 
**total_price** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.client_describe_order_response_body import ClientDescribeOrderResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ClientDescribeOrderResponseBody from a JSON string
client_describe_order_response_body_instance = ClientDescribeOrderResponseBody.from_json(json)
# print the JSON string representation of the object
print ClientDescribeOrderResponseBody.to_json()

# convert the object into a dict
client_describe_order_response_body_dict = client_describe_order_response_body_instance.to_dict()
# create an instance of ClientDescribeOrderResponseBody from a dict
client_describe_order_response_body_form_dict = client_describe_order_response_body.from_dict(client_describe_order_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


