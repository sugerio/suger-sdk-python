# GithubComSugerioMarketplaceServiceRdsDbLibBillingAwsBillingEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**agreement_id** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**balance_impacting** | **int** |  | [optional] 
**bank_trace_id** | **str** |  | [optional] 
**billing_address_id** | **str** |  | [optional] 
**broker_id** | **str** |  | [optional] 
**buyer_id** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**data_feed_product_id** | **str** |  | [optional] 
**disbursement_billing_event_id** | **str** |  | [optional] 
**end_user_account_id** | **str** |  | [optional] 
**entitlement_id** | **str** |  | [optional] 
**from_account_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**insert_date** | [**SqlNullTime**](SqlNullTime.md) |  | [optional] 
**invoice_date** | [**SqlNullTime**](SqlNullTime.md) |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**offer_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**parent_billing_event_id** | **str** |  | [optional] 
**payment_due_date** | [**SqlNullTime**](SqlNullTime.md) |  | [optional] 
**product_id** | **str** |  | [optional] 
**to_account_id** | **str** |  | [optional] 
**transaction_reference_id** | **str** |  | [optional] 
**transaction_type** | **str** |  | [optional] 
**usage_period_end_date** | [**SqlNullTime**](SqlNullTime.md) |  | [optional] 
**usage_period_start_date** | [**SqlNullTime**](SqlNullTime.md) |  | [optional] 

## Example

```python
from openapi_client.models.github_com_sugerio_marketplace_service_rds_db_lib_billing_aws_billing_event import GithubComSugerioMarketplaceServiceRdsDbLibBillingAwsBillingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComSugerioMarketplaceServiceRdsDbLibBillingAwsBillingEvent from a JSON string
github_com_sugerio_marketplace_service_rds_db_lib_billing_aws_billing_event_instance = GithubComSugerioMarketplaceServiceRdsDbLibBillingAwsBillingEvent.from_json(json)
# print the JSON string representation of the object
print GithubComSugerioMarketplaceServiceRdsDbLibBillingAwsBillingEvent.to_json()

# convert the object into a dict
github_com_sugerio_marketplace_service_rds_db_lib_billing_aws_billing_event_dict = github_com_sugerio_marketplace_service_rds_db_lib_billing_aws_billing_event_instance.to_dict()
# create an instance of GithubComSugerioMarketplaceServiceRdsDbLibBillingAwsBillingEvent from a dict
github_com_sugerio_marketplace_service_rds_db_lib_billing_aws_billing_event_form_dict = github_com_sugerio_marketplace_service_rds_db_lib_billing_aws_billing_event.from_dict(github_com_sugerio_marketplace_service_rds_db_lib_billing_aws_billing_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


