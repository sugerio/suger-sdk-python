# GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAzureCmaRevenue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_asset_id** | **str** |  | [optional] 
**azure_billing_account_id** | **str** |  | [optional] 
**azure_customer_id** | **str** |  | [optional] 
**azure_offer_id** | **str** |  | [optional] 
**azure_plan_id** | **str** |  | [optional] 
**billing_model** | **str** |  | [optional] 
**buyer_id** | **str** |  | [optional] 
**earning_usd** | **float** |  | [optional] 
**entitlement_id** | **str** |  | [optional] 
**estimated_payout_month** | [**DatabaseSqlNullTime**](DatabaseSqlNullTime.md) |  | [optional] 
**offer_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**payment_sent_date** | [**DatabaseSqlNullTime**](DatabaseSqlNullTime.md) |  | [optional] 
**payout_status** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**purchase_record_id** | **str** |  | [optional] 
**revenue_usd** | **float** |  | [optional] 
**term_end_date** | **str** |  | [optional] 
**term_start_date** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_legacy_rds_db_lib_billing_azure_cma_revenue import GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAzureCmaRevenue

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAzureCmaRevenue from a JSON string
github_com_sugerio_marketplace_service_pkg_legacy_rds_db_lib_billing_azure_cma_revenue_instance = GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAzureCmaRevenue.from_json(json)
# print the JSON string representation of the object
print(GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAzureCmaRevenue.to_json())

# convert the object into a dict
github_com_sugerio_marketplace_service_pkg_legacy_rds_db_lib_billing_azure_cma_revenue_dict = github_com_sugerio_marketplace_service_pkg_legacy_rds_db_lib_billing_azure_cma_revenue_instance.to_dict()
# create an instance of GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAzureCmaRevenue from a dict
github_com_sugerio_marketplace_service_pkg_legacy_rds_db_lib_billing_azure_cma_revenue_from_dict = GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAzureCmaRevenue.from_dict(github_com_sugerio_marketplace_service_pkg_legacy_rds_db_lib_billing_azure_cma_revenue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


