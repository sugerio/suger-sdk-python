# WorkloadProduct


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** |  | [optional] 
**creation_time** | **datetime** |  | [optional] 
**external_id** | **str** |  | [optional] 
**fulfillment_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**info** | [**ProductInfo**](ProductInfo.md) |  | [optional] 
**last_update_time** | **datetime** |  | [optional] 
**last_updated_by** | **str** |  | [optional] 
**meta_info** | [**WorkloadMetaInfo**](WorkloadMetaInfo.md) |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**partner** | [**Partner**](Partner.md) |  | [optional] 
**product_type** | **str** |  | [optional] 
**service** | [**PartnerService**](PartnerService.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.workload_product import WorkloadProduct

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadProduct from a JSON string
workload_product_instance = WorkloadProduct.from_json(json)
# print the JSON string representation of the object
print WorkloadProduct.to_json()

# convert the object into a dict
workload_product_dict = workload_product_instance.to_dict()
# create an instance of WorkloadProduct from a dict
workload_product_form_dict = workload_product.from_dict(workload_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


