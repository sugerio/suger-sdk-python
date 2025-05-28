# EntitlementInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addons** | [**List[BillingAddonRecord]**](BillingAddonRecord.md) | The addons for the entitlement. | [optional] 
**alert_days_before_end** | **int** | Alert days before the end of the entitlement | [optional] 
**alibaba_entitlements** | [**List[ClientDescribeInstanceResponseBody]**](ClientDescribeInstanceResponseBody.md) | Nullable. Alibaba Entitlements from Alibaba Marketplace. | [optional] 
**alibaba_orders** | [**List[ClientDescribeOrderResponseBody]**](ClientDescribeOrderResponseBody.md) | Nullable. Alibaba Orders from Alibaba Marketplace. | [optional] 
**auto_renew** | **bool** | Is this Entitlement Auto Renew enabled. | [optional] 
**aws_agreement** | [**AwsMarketplaceAgreementV2**](AwsMarketplaceAgreementV2.md) | Nullable. AWS agreement from AWS Marketplace. | [optional] 
**aws_channel_partner** | [**AwsChannelPartner**](AwsChannelPartner.md) | The AWS channel partner (reseller), only applicable if this entitlement is based on AWS CPPO offer. | [optional] 
**aws_entitlements** | [**List[TypesEntitlement]**](TypesEntitlement.md) | Nullable. AWS Entitlements from AWS Marketplace. | [optional] 
**azure_subscriptions** | [**List[AzureMarketplaceSubscription]**](AzureMarketplaceSubscription.md) | Nullable. Azure Subscriptions from Azure Marketplace. | [optional] 
**billable_dimensions** | [**List[BillableDimension]**](BillableDimension.md) | The dimensions for billable metric usage-based metering. It&#39;s for Suger(Stripe, Ayden) metering. | [optional] 
**billing_cycle** | [**BillingCycle**](BillingCycle.md) | Billing Cycle | [optional] 
**billing_interval_in_months** | **int** | The billing interval from the offer. | [optional] 
**buyer_management_url** | **str** | The buyer&#39;s management URL in the cloud marketplace. For different cloud marketplaces, the buyer management URL maybe different. | [optional] 
**collectable_amount** | **float** | The amount that the seller can collect. It excludes the marketplace commision fee. | [optional] 
**commit_amount** | **float** | The amount that the buyer has committed to pay. It can be the sum of payment installments if applicable. | [optional] 
**commits** | [**List[CommitDimension]**](CommitDimension.md) | The dimensions for flatrate commitment (recurring or one-time). | [optional] 
**currency** | **str** | The default Currency is USD. | [optional] 
**dimensions** | [**List[MeteringDimension]**](MeteringDimension.md) | The dimensions for usage-based metering. It&#39;s for usage metering in cloud marketplaces. The max size of dimensions is 50. The oversized dimensions won&#39;t be saved in the EntitlementInfo. But the dimensions can be accessed from the connected offer info or product info. | [optional] 
**dimensions_oversized** | **bool** | Whether the upper metering dimensions are oversized (exceed the max size 50). | [optional] 
**disbursed_amount** | **float** | The amount that has been disbursed to the seller account. | [optional] 
**eula_type** | [**EulaType**](EulaType.md) |  | [optional] 
**eula_url** | **str** |  | [optional] 
**gcp_entitlements** | [**List[GcpMarketplaceEntitlement]**](GcpMarketplaceEntitlement.md) | Nullable. GCP Entitlements from GCP Marketplace. | [optional] 
**gcp_plans** | [**List[GcpMarketplaceProductPurchaseOptionSpec]**](GcpMarketplaceProductPurchaseOptionSpec.md) | Only applicable for GCP Marketplace Entitlements. | [optional] 
**grace_period_in_days** | **int** | The grace period for the offer. It is same as the TrialConfig in DirectOfferInfo. But can be overridden at the entitlement level. | [optional] 
**gross_amount** | **float** | The gross amount that the buyer has committed to pay, including usage metered amount. | [optional] 
**invoiced_amount** | **float** | The amount that the buyer has got invoiced. | [optional] 
**is_metering_overage_commit** | **bool** | Whether the usage metering will be charged for the amount that exceeds the committed amount from the offer. | [optional] 
**net_terms_in_days** | **int** | The net terms for the offer. It is same as the TrialConfig in DirectOfferInfo. But can be overridden at the entitlement level. | [optional] 
**payment_installments** | [**List[PaymentInstallment]**](PaymentInstallment.md) | For flexible payment schedules | [optional] 
**payment_schedule** | [**PaymentScheduleType**](PaymentScheduleType.md) | The payment schedule for the entitlement. PREPAY means the buyer pays before the service is provided. POSTPAY means the buyer pays after the service is provided. | [optional] 
**refund_cancellation_policy** | **str** |  | [optional] 
**seller_notes** | **str** |  | [optional] 
**snowflake_offer** | [**SnowflakeMarketplaceOffer**](SnowflakeMarketplaceOffer.md) | Snowfalke offer info | [optional] 
**spa_url** | **str** | The URL with JWT as auth method for the entitlement SPA. It can be shared with the buyer to access the SPA without login. | [optional] 
**trial_config** | [**TrialConfig**](TrialConfig.md) | The trial configuration for the offer. It is same as the TrialConfig in DirectOfferInfo. But can be overridden at the entitlement level. | [optional] 

## Example

```python
from suger_sdk_python.models.entitlement_info import EntitlementInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementInfo from a JSON string
entitlement_info_instance = EntitlementInfo.from_json(json)
# print the JSON string representation of the object
print(EntitlementInfo.to_json())

# convert the object into a dict
entitlement_info_dict = entitlement_info_instance.to_dict()
# create an instance of EntitlementInfo from a dict
entitlement_info_from_dict = EntitlementInfo.from_dict(entitlement_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


