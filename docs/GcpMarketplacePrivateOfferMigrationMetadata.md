# GcpMarketplacePrivateOfferMigrationMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_flavor_external_name** | **str** | Plan name maybe with term suffix, such as \&quot;plan-name-P1Y\&quot; | [optional] 
**product_external_name** | **str** | in format of \&quot;product-service-id.endpoints.gcp-project-id.cloud.goog\&quot; | [optional] 
**project_number** | **str** | The GCP project number of the provider. | [optional] 
**provider_id** | **str** | The GCP project ID of the provider. | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_private_offer_migration_metadata import GcpMarketplacePrivateOfferMigrationMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplacePrivateOfferMigrationMetadata from a JSON string
gcp_marketplace_private_offer_migration_metadata_instance = GcpMarketplacePrivateOfferMigrationMetadata.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplacePrivateOfferMigrationMetadata.to_json())

# convert the object into a dict
gcp_marketplace_private_offer_migration_metadata_dict = gcp_marketplace_private_offer_migration_metadata_instance.to_dict()
# create an instance of GcpMarketplacePrivateOfferMigrationMetadata from a dict
gcp_marketplace_private_offer_migration_metadata_from_dict = GcpMarketplacePrivateOfferMigrationMetadata.from_dict(gcp_marketplace_private_offer_migration_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


