# GithubComAwsAwsSdkGoV2ServiceMarketplaceentitlementserviceTypesEntitlement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_aws_account_id** | **str** | The CustomerAWSAccountID parameter specifies the AWS account ID of the buyer. | [optional] 
**customer_identifier** | **str** | The customer identifier is a handle to each unique customer in an application. Customer identifiers are obtained through the ResolveCustomer operation in AWS Marketplace Metering Service. | [optional] 
**dimension** | **str** | The dimension for which the given entitlement applies. Dimensions represent categories of capacity in a product and are specified when the product is listed in AWS Marketplace. | [optional] 
**expiration_date** | **str** | The expiration date represents the minimum date through which this entitlement is expected to remain valid. For contractual products listed on AWS Marketplace, the expiration date is the date at which the customer will renew or cancel their contract. Customers who are opting to renew their contract will still have entitlements with an expiration date. | [optional] 
**license_arn** | **str** |  | [optional] 
**product_code** | **str** | The product code for which the given entitlement applies. Product codes are provided by AWS Marketplace when the product listing is created. | [optional] 
**value** | [**GithubComAwsAwsSdkGoV2ServiceMarketplaceentitlementserviceTypesEntitlementValue**](GithubComAwsAwsSdkGoV2ServiceMarketplaceentitlementserviceTypesEntitlementValue.md) | The EntitlementValue represents the amount of capacity that the customer is entitled to for the product. | [optional] 

## Example

```python
from suger_sdk_python.models.github_com_aws_aws_sdk_go_v2_service_marketplaceentitlementservice_types_entitlement import GithubComAwsAwsSdkGoV2ServiceMarketplaceentitlementserviceTypesEntitlement

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComAwsAwsSdkGoV2ServiceMarketplaceentitlementserviceTypesEntitlement from a JSON string
github_com_aws_aws_sdk_go_v2_service_marketplaceentitlementservice_types_entitlement_instance = GithubComAwsAwsSdkGoV2ServiceMarketplaceentitlementserviceTypesEntitlement.from_json(json)
# print the JSON string representation of the object
print(GithubComAwsAwsSdkGoV2ServiceMarketplaceentitlementserviceTypesEntitlement.to_json())

# convert the object into a dict
github_com_aws_aws_sdk_go_v2_service_marketplaceentitlementservice_types_entitlement_dict = github_com_aws_aws_sdk_go_v2_service_marketplaceentitlementservice_types_entitlement_instance.to_dict()
# create an instance of GithubComAwsAwsSdkGoV2ServiceMarketplaceentitlementserviceTypesEntitlement from a dict
github_com_aws_aws_sdk_go_v2_service_marketplaceentitlementservice_types_entitlement_from_dict = GithubComAwsAwsSdkGoV2ServiceMarketplaceentitlementserviceTypesEntitlement.from_dict(github_com_aws_aws_sdk_go_v2_service_marketplaceentitlementservice_types_entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


