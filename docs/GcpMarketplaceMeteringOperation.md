# GcpMarketplaceMeteringOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer_id** | **str** | ConsumerId: Identity of the consumer who is using the service. This field should be filled in for the operations initiated by a consumer, but not for service-initiated operations that are not related to a specific consumer. - This can be in one of the following formats: - project:PROJECT_ID, - project&#x60;_&#x60;number:PROJECT_NUMBER, - projects/PROJECT_ID or PROJECT_NUMBER, - folders/FOLDER_NUMBER, - organizations/ORGANIZATION_NUMBER, - api&#x60;_&#x60;key:API_KEY. | [optional] 
**end_time** | **str** | EndTime: End time of the operation. Required when the operation is used in ServiceController.Report, but optional when the operation is used in ServiceController.Check. | [optional] 
**labels** | **Dict[str, str]** | Labels: Labels describing the operation. Only the following labels are allowed: - Labels describing monitored resources as defined in the service configuration. - Default labels of metric values. When specified, labels defined in the metric value override these default. - The following labels defined by Google Cloud Platform: - &#x60;cloud.googleapis.com/location&#x60; describing the location where the operation happened, - &#x60;servicecontrol.googleapis.com/user_agent&#x60; describing the user agent of the API request, - &#x60;servicecontrol.googleapis.com/service_agent&#x60; describing the service used to handle the API request (e.g. ESP), - &#x60;servicecontrol.googleapis.com/platform&#x60; describing the platform where the API is served, such as App Engine, Compute Engine, or Kubernetes Engine. | [optional] 
**metric_value_sets** | [**List[GcpMarketplaceMeteringMetricValueSet]**](GcpMarketplaceMeteringMetricValueSet.md) | MetricValueSets: Represents information about this operation. Each MetricValueSet corresponds to a metric defined in the service configuration. The data type used in the MetricValueSet must agree with the data type specified in the metric definition. Within a single operation, it is not allowed to have more than one MetricValue instances that have the same metric names and identical label value combinations. If a request has such duplicated MetricValue instances, the entire request is rejected with an invalid argument error. | [optional] 
**operation_id** | **str** | OperationId: Identity of the operation. This must be unique within the scope of the service that generated the operation. If the service calls Check() and Report() on the same operation, the two calls should carry the same id. UUID version 4 is recommended, though not required. In scenarios where an operation is computed from existing information and an idempotent id is desirable for deduplication purpose, UUID version 5 is recommended. See RFC 4122 for details. | [optional] 
**operation_name** | **str** | OperationName: Fully qualified name of the operation. Reserved for future use. | [optional] 
**start_time** | **str** | StartTime: Required. Start time of the operation. | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_metering_operation import GcpMarketplaceMeteringOperation

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceMeteringOperation from a JSON string
gcp_marketplace_metering_operation_instance = GcpMarketplaceMeteringOperation.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceMeteringOperation.to_json())

# convert the object into a dict
gcp_marketplace_metering_operation_dict = gcp_marketplace_metering_operation_instance.to_dict()
# create an instance of GcpMarketplaceMeteringOperation from a dict
gcp_marketplace_metering_operation_from_dict = GcpMarketplaceMeteringOperation.from_dict(gcp_marketplace_metering_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


