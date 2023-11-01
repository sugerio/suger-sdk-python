# GcpIntegration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_chrome_sync** | **bool** | Enable GCP marketplace sync from GCP Chrome. If true, Suger will sync GCP Marketplace Product &amp; Private Offer from GCP Chrome. | [optional] 
**enable_manual_approve_entitlement** | **bool** | Enable manually approve the GCP Marketplace Entitlement. If true, Suger will not automatically approve the GCP Marketplace Entitlement. Util the GCP Marketplace Entitlement is manually approved, it will not be activated. | [optional] 
**gcp_project_id** | **str** |  | [optional] 
**gcp_project_number** | **str** |  | [optional] 
**identity_provider_id** | **str** |  | [optional] 
**login_url** | **str** | The Login URL for GCP Marketplace buyers to login to your service with or without SSO JWT token. If not set, the login will be redirected to the Product&#39;s fulfillment URL. | [optional] 
**partner_id** | **str** | The GCP Marketplace Partner ID, it is also called as Provider ID somewhere. | [optional] 
**pubsub_subscription** | **str** | The resource name of the Pub/Sub subscription to receive notifications from Google cloud marketplace. | [optional] 
**pubsub_topic** | **str** | The resource name of the Pub/Sub topic to receive notifications from Google when a user signs up for your service, purchases a plan, or changes an existing plan. | [optional] 
**report_bucket** | **str** | The GCP storage bucket name to store the GCP Marketplace reports. | [optional] 
**report_full_sync_done** | **bool** | Is GCP Marketplace Report full-sync done. | [optional] 
**report_start_date** | **datetime** | The UTC date when GCP Marketplace reports start to generate. | [optional] 
**report_sync_disabled** | **bool** | Disable GCP Marketplace Report sync. If true, Suger stop to sync GCP Marketplace reports. | [optional] 
**revenue_record_full_sync_done** | **bool** | Is GCP Marketplace Revenue Record full-sync done. | [optional] 
**revenue_record_sync_disabled** | **bool** | Disable GCP Marketplace Revenue Record sync. If true, Suger stop to sync GCP Marketplace Revenue Records. | [optional] 
**service_account_email** | **str** |  | [optional] 
**service_names** | **List[str]** | The array of service resource names of the listings in GCP Marketplace. | [optional] 
**signup_redirect_without_entitlement_enabled** | **bool** | If enabled, Suger will redirect the new client to the signup page even the entitlement is not found. If disabled, Suger will redirect the new client to the error page if the entitlement is not found. | [optional] 
**usage_metering_disabled** | **bool** | Disable Usage Metering to GCP Marketplace. If true, Suger stop to report usage records to GCP Marketplace. | [optional] 
**workload_identity_pool_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.gcp_integration import GcpIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of GcpIntegration from a JSON string
gcp_integration_instance = GcpIntegration.from_json(json)
# print the JSON string representation of the object
print GcpIntegration.to_json()

# convert the object into a dict
gcp_integration_dict = gcp_integration_instance.to_dict()
# create an instance of GcpIntegration from a dict
gcp_integration_form_dict = gcp_integration.from_dict(gcp_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


