# TypesUsageRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_identifier** | **str** | The CustomerIdentifier is obtained through the ResolveCustomer operation and represents an individual buyer in your application.  This member is required. | [optional] 
**dimension** | **str** | During the process of registering a product on AWS Marketplace, dimensions are specified. These represent different units of value in your application.  This member is required. | [optional] 
**quantity** | **int** | The quantity of usage consumed by the customer for the given dimension and time. Defaults to 0 if not specified. | [optional] 
**timestamp** | **str** | Timestamp, in UTC, for which the usage is being reported. Your application can meter usage for up to one hour in the past. Make sure the timestamp value is not before the start of the software usage.  This member is required. | [optional] 
**usage_allocations** | [**List[TypesUsageAllocation]**](TypesUsageAllocation.md) | The set of UsageAllocations to submit. The sum of all UsageAllocation quantities must equal the Quantity of the UsageRecord. | [optional] 

## Example

```python
from openapi_client.models.types_usage_record import TypesUsageRecord

# TODO update the JSON string below
json = "{}"
# create an instance of TypesUsageRecord from a JSON string
types_usage_record_instance = TypesUsageRecord.from_json(json)
# print the JSON string representation of the object
print TypesUsageRecord.to_json()

# convert the object into a dict
types_usage_record_dict = types_usage_record_instance.to_dict()
# create an instance of TypesUsageRecord from a dict
types_usage_record_form_dict = types_usage_record.from_dict(types_usage_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


