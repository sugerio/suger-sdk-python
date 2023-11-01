# AlibabaMarketplaceIntegration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliyun_uid** | **str** | The uid of the seller&#39;s main Alibaba Account. | [optional] 
**auto_cancel_suspended_entitlements_enabled** | **bool** | If true, the suspended entitlements will be automatically canceled after the specified days. | [optional] 
**credential** | [**AlibabaIntegrationCredential**](AlibabaIntegrationCredential.md) |  | [optional] 
**days_until_auto_cancel_suspended_entitlements** | **int** | Specifies the number of days after which an entitlement in suspended status will be automatically canceled. Only applicable if AutoCancelSuspendedEntitlementsEnabled is true. If the value is 0 or negative, the auto cancel feature is disabled. | [optional] 
**product_codes** | **List[str]** | The codes of the products that the seller is selling on Alibaba Marketplace. | [optional] 
**secret_key** | **str** | The secret key used to store the AlibabaIntegrationCredential in AWS Secret manager. For internal usage only. | [optional] 
**usage_metering_disabled** | **bool** | Disable Usage Metering to Alibaba Cloud Marketplace. If true, Suger stop to report usage records to Alibaba Cloud Marketplace. | [optional] 

## Example

```python
from openapi_client.models.alibaba_marketplace_integration import AlibabaMarketplaceIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of AlibabaMarketplaceIntegration from a JSON string
alibaba_marketplace_integration_instance = AlibabaMarketplaceIntegration.from_json(json)
# print the JSON string representation of the object
print AlibabaMarketplaceIntegration.to_json()

# convert the object into a dict
alibaba_marketplace_integration_dict = alibaba_marketplace_integration_instance.to_dict()
# create an instance of AlibabaMarketplaceIntegration from a dict
alibaba_marketplace_integration_form_dict = alibaba_marketplace_integration.from_dict(alibaba_marketplace_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


