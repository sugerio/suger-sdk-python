# PartnerUsageMeteringConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension_mapping** | [**Dict[str, UsageMeteringDimensionMappingValue]**](UsageMeteringDimensionMappingValue.md) | The mapping of the source dimension key to the destination dimension key of the usage metering. | [optional] 
**enable_commit_with_additional_usage_at_list_price** | **bool** | Enable the commit (discount) with additional usage metering at list price. Only applicable if EnableCommitWithAdditionalUsageMetering is true. The default is false, which means the commit with additional usage metering at the discounted price in the private offer. If set to true, the additional usage is metered at the list price (the price in public product listing) instead of the discounted price. | [optional] 
**enable_commit_with_additional_usage_metering** | **bool** | Enable the commit with additional usage metering. The default is false, which means all usage records are reported to partner no matter how much is the commit. If set to true, the usage records will be reported to partner only if the current commit has been exhausted. | [optional] 
**enable_dimension_mapping** | **bool** | Enable the dimension mapping for the usage metering. The default is false, which means no dimension conversion and just use the origin dimension. | [optional] 
**partner** | [**Partner**](Partner.md) |  | [optional] 

## Example

```python
from openapi_client.models.partner_usage_metering_config import PartnerUsageMeteringConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerUsageMeteringConfig from a JSON string
partner_usage_metering_config_instance = PartnerUsageMeteringConfig.from_json(json)
# print the JSON string representation of the object
print PartnerUsageMeteringConfig.to_json()

# convert the object into a dict
partner_usage_metering_config_dict = partner_usage_metering_config_instance.to_dict()
# create an instance of PartnerUsageMeteringConfig from a dict
partner_usage_metering_config_form_dict = partner_usage_metering_config.from_dict(partner_usage_metering_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


