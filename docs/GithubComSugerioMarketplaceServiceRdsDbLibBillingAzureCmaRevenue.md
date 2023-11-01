# GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue


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
**estimated_payout_month** | [**SqlNullTime**](SqlNullTime.md) |  | [optional] 
**offer_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**payment_sent_date** | [**SqlNullTime**](SqlNullTime.md) |  | [optional] 
**payout_status** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**purchase_record_id** | **str** |  | [optional] 
**revenue_usd** | **float** |  | [optional] 
**term_end_date** | **str** |  | [optional] 
**term_start_date** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.github_com_sugerio_marketplace_service_rds_db_lib_billing_azure_cma_revenue import GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue from a JSON string
github_com_sugerio_marketplace_service_rds_db_lib_billing_azure_cma_revenue_instance = GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue.from_json(json)
# print the JSON string representation of the object
print GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue.to_json()

# convert the object into a dict
github_com_sugerio_marketplace_service_rds_db_lib_billing_azure_cma_revenue_dict = github_com_sugerio_marketplace_service_rds_db_lib_billing_azure_cma_revenue_instance.to_dict()
# create an instance of GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue from a dict
github_com_sugerio_marketplace_service_rds_db_lib_billing_azure_cma_revenue_form_dict = github_com_sugerio_marketplace_service_rds_db_lib_billing_azure_cma_revenue.from_dict(github_com_sugerio_marketplace_service_rds_db_lib_billing_azure_cma_revenue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


