# GcpMarketplaceResellerPrivateOfferPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceptance_deadline_time** | **datetime** |  | [optional] 
**agreement** | **str** | The resource name of agreement(entitlement) In format of \&quot;projects/{projectNumber}/agreements/{agreementId}\&quot; | [optional] 
**agreement_documents** | [**GcpMarketplaceResellerPrivateOfferPlanAgreementDocuments**](GcpMarketplaceResellerPrivateOfferPlanAgreementDocuments.md) |  | [optional] 
**amendment_context** | **object** |  | [optional] 
**display_name** | **str** |  | [optional] 
**duration_config** | [**GcpMarketplaceResellerPrivateOfferPlanDurationConfig**](GcpMarketplaceResellerPrivateOfferPlanDurationConfig.md) |  | [optional] 
**features** | [**List[GcpMarketplaceProductFeatureValue]**](GcpMarketplaceProductFeatureValue.md) |  | [optional] 
**installment_timeline_template** | [**GcpMarketplaceResellerPrivateOfferPlanInstallmentTimelineTemplate**](GcpMarketplaceResellerPrivateOfferPlanInstallmentTimelineTemplate.md) |  | [optional] 
**isv_info** | [**GcpMarketplaceIsvInfo**](GcpMarketplaceIsvInfo.md) |  | [optional] 
**margin** | [**GcpMarketplaceResellerPrivateOfferPlanMargin**](GcpMarketplaceResellerPrivateOfferPlanMargin.md) |  | [optional] 
**meta_info** | [**GcpMarketplaceResellerPrivateOfferPlanMetainfo**](GcpMarketplaceResellerPrivateOfferPlanMetainfo.md) |  | [optional] 
**name** | **str** | In format of \&quot;projects/{projectNumber}/partnerAccounts/{partnerAccountId}/resellerPrivateOfferPlans/{resellerPrivateOfferPlanId}\&quot; | [optional] 
**offer_template_policies** | [**GcpMarketplaceOfferTemplatePolicies**](GcpMarketplaceOfferTemplatePolicies.md) |  | [optional] 
**offer_term_template** | [**GcpMarketplacePrivateOfferTermTemplate**](GcpMarketplacePrivateOfferTermTemplate.md) |  | [optional] 
**payment_schedule** | [**PaymentScheduleType**](PaymentScheduleType.md) |  | [optional] 
**price_model_template** | [**GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplate**](GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplate.md) | Nill if this reseller private offer plan has installmentTimelineTemplate (payment installments). | [optional] 
**product_info** | [**GcpMarketplaceProductInfo**](GcpMarketplaceProductInfo.md) |  | [optional] 
**replacement_metadata** | **object** |  | [optional] 
**resell_offer_template** | **str** | in format of \&quot;resellOfferTemplates/{resellOfferTemplateId}\&quot; | [optional] 
**reseller_info** | [**GcpMarketplaceResellerInfo**](GcpMarketplaceResellerInfo.md) |  | [optional] 
**reuse_policy** | [**GcpMarketplaceResellerPrivateOfferPlanReusePolicy**](GcpMarketplaceResellerPrivateOfferPlanReusePolicy.md) |  | [optional] 
**start_policy** | [**GcpMarketplaceStartPolicy**](GcpMarketplaceStartPolicy.md) |  | [optional] 
**state** | [**GcpMarketplaceResellerPrivateOfferPlanState**](GcpMarketplaceResellerPrivateOfferPlanState.md) |  | [optional] 
**state_transitions** | [**List[GcpMarketplaceResellerPrivateOfferPlanStateTransition]**](GcpMarketplaceResellerPrivateOfferPlanStateTransition.md) |  | [optional] 
**update_time** | **datetime** |  | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_reseller_private_offer_plan import GcpMarketplaceResellerPrivateOfferPlan

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceResellerPrivateOfferPlan from a JSON string
gcp_marketplace_reseller_private_offer_plan_instance = GcpMarketplaceResellerPrivateOfferPlan.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceResellerPrivateOfferPlan.to_json())

# convert the object into a dict
gcp_marketplace_reseller_private_offer_plan_dict = gcp_marketplace_reseller_private_offer_plan_instance.to_dict()
# create an instance of GcpMarketplaceResellerPrivateOfferPlan from a dict
gcp_marketplace_reseller_private_offer_plan_from_dict = GcpMarketplaceResellerPrivateOfferPlan.from_dict(gcp_marketplace_reseller_private_offer_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


