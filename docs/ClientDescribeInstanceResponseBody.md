# ClientDescribeInstanceResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_address** | **str** |  | [optional] 
**app_json** | **str** | example:  {\&quot;frontEndUrl\&quot;:\&quot;https://****.aliyundoc.com\&quot;,\&quot;password\&quot;:\&quot;Sjtv***\&quot;,\&quot;adminUrl\&quot;:\&quot;https://****.aliyundoc.com\&quot;,\&quot;username\&quot;:\&quot;aliyun***\&quot;} | [optional] 
**auto_renewal** | **str** |  | [optional] 
**began_on** | **int** | example:  1570634021000 | [optional] 
**component_json** | **str** | example:  {\&quot;package_version\&quot;:\&quot;yuncode000111\&quot;} | [optional] 
**constraints** | **str** | example:  {} | [optional] 
**created_on** | **int** | example:  1570634018000 | [optional] 
**end_on** | **int** | example:  1602259200000 | [optional] 
**extend_json** | **str** |  | [optional] 
**host_json** | **str** | example:  {\&quot;password\&quot;:\&quot;***\&quot;,\&quot;ip\&quot;:\&quot;118.31.***.41\&quot;,\&quot;innerIp\&quot;:\&quot;118.31.***.41\&quot;,\&quot;region\&quot;:\&quot;\&quot;,\&quot;username\&quot;:\&quot;***\&quot;,\&quot;beianInfo\&quot;:\&quot;\&quot;} | [optional] 
**instance_id** | **int** | example:  1551111111 | [optional] 
**is_trial** | **bool** | example:  true | [optional] 
**license_code** | **str** |  | [optional] 
**modules** | [**ClientDescribeInstanceResponseBodyModules**](ClientDescribeInstanceResponseBodyModules.md) |  | [optional] 
**order_id** | **int** | example:  204211111111111 | [optional] 
**product_code** | **str** | example:  cmgj00**11 | [optional] 
**product_name** | **str** |  | [optional] 
**product_sku_code** | **str** | example:  cmgj00**11-prepay | [optional] 
**product_type** | **str** | example:  APP | [optional] 
**relational_data** | [**ClientDescribeInstanceResponseBodyRelationalData**](ClientDescribeInstanceResponseBodyRelationalData.md) |  | [optional] 
**status** | **str** | example:  OPENED | [optional] 
**supplier_name** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.client_describe_instance_response_body import ClientDescribeInstanceResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ClientDescribeInstanceResponseBody from a JSON string
client_describe_instance_response_body_instance = ClientDescribeInstanceResponseBody.from_json(json)
# print the JSON string representation of the object
print(ClientDescribeInstanceResponseBody.to_json())

# convert the object into a dict
client_describe_instance_response_body_dict = client_describe_instance_response_body_instance.to_dict()
# create an instance of ClientDescribeInstanceResponseBody from a dict
client_describe_instance_response_body_from_dict = ClientDescribeInstanceResponseBody.from_dict(client_describe_instance_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


