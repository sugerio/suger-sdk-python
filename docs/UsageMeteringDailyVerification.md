# UsageMeteringDailyVerification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billed_amount** | **float** | The amount of the usage metering billed by the cloud marketplace metering service. | [optional] 
**billed_date** | **datetime** | The date when the usage metering is billed by the cloud marketplace metering service. | [optional] 
**billed_quantity** | **float** | The quantity of the usage metering billed by the cloud marketplace metering service. | [optional] 
**is_amount_matched** | **bool** | Whether the amount is matched between reported &amp; billed usage metering. | [optional] 
**is_quantity_matched** | **bool** | Whether the quantity is matched between reported &amp; billed usage metering. | [optional] 
**key** | **str** | The dimension key of the usage metering. | [optional] 
**partner** | [**Partner**](Partner.md) |  | [optional] 
**reported_amount** | **float** | The amount of the usage metering reported to the cloud marketplace. | [optional] 
**reported_date** | **datetime** | The date when the usage metering is reported to the cloud marketplace. | [optional] 
**reported_quantity** | **float** | The quantity of the usage metering reported to the cloud marketplace. | [optional] 

## Example

```python
from openapi_client.models.usage_metering_daily_verification import UsageMeteringDailyVerification

# TODO update the JSON string below
json = "{}"
# create an instance of UsageMeteringDailyVerification from a JSON string
usage_metering_daily_verification_instance = UsageMeteringDailyVerification.from_json(json)
# print the JSON string representation of the object
print UsageMeteringDailyVerification.to_json()

# convert the object into a dict
usage_metering_daily_verification_dict = usage_metering_daily_verification_instance.to_dict()
# create an instance of UsageMeteringDailyVerification from a dict
usage_metering_daily_verification_form_dict = usage_metering_daily_verification.from_dict(usage_metering_daily_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


