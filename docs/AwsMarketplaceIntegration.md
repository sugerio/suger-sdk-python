# AwsMarketplaceIntegration

The data struct to store integration info for Suger service to access the client's AWS services.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_info_full_sync_done** | **bool** | Is AWS Marketplace Basic Info (Private Offers, Entitlements/Agreements) full-sync done. | [optional] 
**create_entitlement_before_notification_enabled** | **bool** | If enabled, Suger will create an active entitlement based on the default offer when the new client is redirected from AWS Marketplace, but the notification evnet from AWS Marketplace is not received yet by Suger. If disabled, Suger will not create the entitlement when the new client is redirected from AWS Marketplace. So the redirect URL won&#39;t contain the sugerEntitlementId parameter. | [optional] 
**enable_marketplace_beta_api** | **bool** | Enable the use of AWS Marketplace beta APIs in the backend. If true, Suger will use the beta APIs. | [optional] 
**event_bridge_rule_name** | **str** | AWS EventBridge rule name for AWS Marketplace events. | [optional] 
**external_id** | **str** | The external ID for assuming IAM role. If empty, means no external ID set or needed. Otherwise, it should be auth_id in table identity.organization. | [optional] 
**iam_role_arn** | **str** | The AWS IAM role for Suger service to assume to access the client&#39;s AWS services. | [optional] 
**marketplace_start_date** | **datetime** | AWS Marketplace start date which comes from MDFS Full-Sync. | [optional] 
**mcas_full_sync_done** | **bool** | Is AWS Marketplace Commerce Analytics Service (MCAS) full-sync done. | [optional] 
**mcas_iam_role_arn** | **str** | IAM role ARN to allow AWS Marketplace to write to the S3 bucket and publish notifications to the SNS topic. | [optional] 
**mcas_s3_bucket** | **str** | S3 bucket for AWS Marketplace Commerce Analytics Service (MCAS) | [optional] 
**mcas_sns_topic** | **str** | SNS topic ARN for AWS Marketplace Commerce Analytics Service (MCAS) | [optional] 
**mcas_sync_disabled** | **bool** | Disable Sync with AWS MCAS. If true, Suger stop to sync with MCAS. | [optional] 
**mdfs_full_sync_done** | **bool** | Is AWS Marketplace Data Feeds Service (MDFS) full-sync done. | [optional] 
**mdfs_kms_key_arn** | **str** | KMS Key ARN for the S3 bucket of AWS Marketplace Data Feeds Service (MDFS) | [optional] 
**mdfs_s3_bucket_arn** | **str** | S3 bucket ARN for AWS Marketplace Data Feeds Service (MDFS) | [optional] 
**mdfs_sync_disabled** | **bool** | Disable Sync with AWS MDFS. If true, Suger stop to sync with MDFS. | [optional] 
**policy_arns** | **List[str]** | The policy ARNs in the IAM role. | [optional] 
**revenue_record_full_sync_done** | **bool** | Is AWS Marketplace Revenue Record full-sync done. | [optional] 
**signup_redirect_without_entitlement_enabled** | **bool** | If enabled, Suger will redirect the new client to the signup page even the entitlement is not found. If disabled, Suger will redirect the new client to the error page if the entitlement is not found. | [optional] 
**usage_metering_disabled** | **bool** | Disable Usage Metering to AWS Marketplace. If true, Suger stop to report usage records to AWS Marketplace. | [optional] 

## Example

```python
from openapi_client.models.aws_marketplace_integration import AwsMarketplaceIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceIntegration from a JSON string
aws_marketplace_integration_instance = AwsMarketplaceIntegration.from_json(json)
# print the JSON string representation of the object
print AwsMarketplaceIntegration.to_json()

# convert the object into a dict
aws_marketplace_integration_dict = aws_marketplace_integration_instance.to_dict()
# create an instance of AwsMarketplaceIntegration from a dict
aws_marketplace_integration_form_dict = aws_marketplace_integration.from_dict(aws_marketplace_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


