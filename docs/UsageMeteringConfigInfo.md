# UsageMeteringConfigInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_usage_metering_configs** | [**List[PartnerUsageMeteringConfig]**](PartnerUsageMeteringConfig.md) | The usage metering configuration for each Partner, such as AWS, AZURE &amp; GCP. | [optional] 

## Example

```python
from suger_sdk_python.models.usage_metering_config_info import UsageMeteringConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UsageMeteringConfigInfo from a JSON string
usage_metering_config_info_instance = UsageMeteringConfigInfo.from_json(json)
# print the JSON string representation of the object
print(UsageMeteringConfigInfo.to_json())

# convert the object into a dict
usage_metering_config_info_dict = usage_metering_config_info_instance.to_dict()
# create an instance of UsageMeteringConfigInfo from a dict
usage_metering_config_info_from_dict = UsageMeteringConfigInfo.from_dict(usage_metering_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


