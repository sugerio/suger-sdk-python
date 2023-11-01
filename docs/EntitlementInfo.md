# EntitlementInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alibaba_entitlements** | [**List[ClientDescribeInstanceResponseBody]**](ClientDescribeInstanceResponseBody.md) | Nullable. Alibaba Entitlements from Alibaba Marketplace. | [optional] 
**alibaba_orders** | [**List[ClientDescribeOrderResponseBody]**](ClientDescribeOrderResponseBody.md) | Nullable. Alibaba Orders from Alibaba Marketplace. | [optional] 
**auto_renew** | **bool** | Is this Entitlement Auto Renew enabled. | [optional] 
**aws_entitlements** | [**List[TypesEntitlement]**](TypesEntitlement.md) | Nullable. AWS Entitlements from AWS Marketplace. | [optional] 
**azure_subscriptions** | [**List[AzureMarketplaceSubscription]**](AzureMarketplaceSubscription.md) | Nullable. Azure Subscriptions from Azure Marketplace. | [optional] 
**collectable_amount** | **float** | The amount that the seller can collect. It excludes the marketplace commision fee. | [optional] 
**commit_amount** | **float** | The amount that the buyer has committed to pay. It can be the sum of payment installments if applicable. | [optional] 
**commits** | [**List[CommitDimension]**](CommitDimension.md) | The dimensions for commit. | [optional] 
**currency** | **str** | The default Currency is USD. | [optional] 
**dimensions** | [**List[MeteringDimension]**](MeteringDimension.md) | The dimensions for usage-based metering. | [optional] 
**disbursed_amount** | **float** | The amount that has been disbursed to the seller account. | [optional] 
**eula_type** | [**EulaType**](EulaType.md) |  | [optional] 
**eula_url** | **str** |  | [optional] 
**gcp_entitlements** | [**List[GcpMarketplaceEntitlement]**](GcpMarketplaceEntitlement.md) | Nullable. GCP Entitlements from GCP Marketplace. | [optional] 
**gcp_plans** | [**List[GcpMarketplaceProductPurchaseOptionSpec]**](GcpMarketplaceProductPurchaseOptionSpec.md) | Only applicable for GCP Marketplace Entitlements. | [optional] 
**invoiced_amount** | **float** | The amount that the buyer has got invoiced. | [optional] 
**payment_installments** | [**List[PaymentInstallment]**](PaymentInstallment.md) | For flexible payment schedules | [optional] 
**refund_cancelation_policy** | **str** |  | [optional] 
**seller_notes** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.entitlement_info import EntitlementInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementInfo from a JSON string
entitlement_info_instance = EntitlementInfo.from_json(json)
# print the JSON string representation of the object
print EntitlementInfo.to_json()

# convert the object into a dict
entitlement_info_dict = entitlement_info_instance.to_dict()
# create an instance of EntitlementInfo from a dict
entitlement_info_form_dict = entitlement_info.from_dict(entitlement_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


