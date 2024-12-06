# AzureMarketplacePlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**alias** | **str** |  | [optional] 
**azure_government_certifications** | [**List[AzureMarketplaceGovernmentCertification]**](AzureMarketplaceGovernmentCertification.md) |  | [optional] 
**azure_regions** | **List[str]** | enums:[azureGlobal,azureGovernment,azureGermany,azureChina] | [optional] 
**deprecation_schedule** | [**AzureMarketplaceDeprecationSchedule**](AzureMarketplaceDeprecationSchedule.md) |  | [optional] 
**display_rank** | **int** | default 2147483647 | [optional] 
**id** | **str** | in format of \&quot;plan/product-durable-id/plan-durable-id\&quot; | [optional] 
**identity** | [**AzureMarketplaceIdentity**](AzureMarketplaceIdentity.md) |  | [optional] 
**lifecycle_state** | [**AzureMarketplaceResourceLifecycleState**](AzureMarketplaceResourceLifecycleState.md) |  | [optional] 
**product** | **str** | in format of \&quot;product/product-durable-id\&quot; | [optional] 
**resource_name** | **str** |  | [optional] 
**subtype** | **str** | Specifies the plan type (AzureApplication-type products only) see: https://go.microsoft.com/fwlink/?linkid&#x3D;2106322 | [optional] 
**validations** | [**List[AzureMarketplaceValidation]**](AzureMarketplaceValidation.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_plan import AzureMarketplacePlan

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePlan from a JSON string
azure_marketplace_plan_instance = AzureMarketplacePlan.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePlan.to_json())

# convert the object into a dict
azure_marketplace_plan_dict = azure_marketplace_plan_instance.to_dict()
# create an instance of AzureMarketplacePlan from a dict
azure_marketplace_plan_from_dict = AzureMarketplacePlan.from_dict(azure_marketplace_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


