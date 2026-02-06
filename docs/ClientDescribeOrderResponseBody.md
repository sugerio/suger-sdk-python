# ClientDescribeOrderResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_quantity** | **int** | example:  0 | [optional] 
**ali_uid** | **int** | example:  190311111111**** | [optional] 
**components** | **Dict[str, object]** |  | [optional] 
**coupon_price** | **float** | example:  0.0 | [optional] 
**created_on** | **int** | example:  1531191564000 | [optional] 
**instance_ids** | [**ClientDescribeOrderResponseBodyInstanceIds**](ClientDescribeOrderResponseBodyInstanceIds.md) |  | [optional] 
**order_id** | **int** | example:  202211111111111 | [optional] 
**order_status** | **str** | example:  NORMAL | [optional] 
**order_type** | **str** | example:  NEW | [optional] 
**original_price** | **float** | example:  10.0 | [optional] 
**paid_on** | **int** | example:  1531191675000 | [optional] 
**pay_status** | **str** | example:  PAID | [optional] 
**payment_price** | **float** | example:  0.0 | [optional] 
**period_type** | **str** | example:  MONTH | [optional] 
**product_code** | **str** | example:  cmgj02**** | [optional] 
**product_name** | **str** |  | [optional] 
**product_sku_code** | **str** | example:  cmgj02****-prepay | [optional] 
**quantity** | **int** | example:  1 | [optional] 
**request_id** | **str** | example:  6EF60BEC-0242-43AF-BB20-270359FB54A7 | [optional] 
**supplier_company_name** | **str** |  | [optional] 
**supplier_telephones** | [**ClientDescribeOrderResponseBodySupplierTelephones**](ClientDescribeOrderResponseBodySupplierTelephones.md) |  | [optional] 
**total_price** | **float** | example:  0.0 | [optional] 

## Example

```python
from suger_sdk_python.models.client_describe_order_response_body import ClientDescribeOrderResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ClientDescribeOrderResponseBody from a JSON string
client_describe_order_response_body_instance = ClientDescribeOrderResponseBody.from_json(json)
# print the JSON string representation of the object
print(ClientDescribeOrderResponseBody.to_json())

# convert the object into a dict
client_describe_order_response_body_dict = client_describe_order_response_body_instance.to_dict()
# create an instance of ClientDescribeOrderResponseBody from a dict
client_describe_order_response_body_from_dict = ClientDescribeOrderResponseBody.from_dict(client_describe_order_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


