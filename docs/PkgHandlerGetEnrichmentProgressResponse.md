# PkgHandlerGetEnrichmentProgressResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cycle_progress_percent** | **int** | CycleProgressPercent is the percentage of the cycle completed (0-100). | [optional] 
**cycle_started_at** | **str** | CycleStartedAt is when the current refresh cycle began. | [optional] 
**estimated_runs_remaining** | **int** | EstimatedRunsRemaining is the estimated number of runs to complete the cycle. | [optional] 
**last_cycle_completed_at** | **str** | LastCycleCompletedAt is when the previous cycle was completed. | [optional] 
**last_run_at** | **str** | LastRunAt is the timestamp of the most recent enrichment run. | [optional] 
**last_run_records_processed** | **int** | LastRunRecordsProcessed is the number of records processed in the most recent run. | [optional] 
**next_cycle_starts_at** | **str** | NextCycleStartsAt is when the next cycle will start (only set when status is \&quot;waiting\&quot;). | [optional] 
**records_processed_in_cycle** | **int** | RecordsProcessedInCycle is the count of records processed in the current cycle. | [optional] 
**status** | **str** | Status indicates the current state of enrichment. Values: \&quot;active\&quot;, \&quot;not_started\&quot;, \&quot;in_progress\&quot;, \&quot;waiting\&quot; - \&quot;active\&quot;: Enrichment is running but refresh cycles are disabled (RefreshAfterDays &#x3D; -1) - \&quot;not_started\&quot;: No enrichment cycle has run yet - \&quot;in_progress\&quot;: Currently processing records in a cycle - \&quot;waiting\&quot;: Cycle completed, waiting for next scheduled run | [optional] 
**total_matching_records** | **int** | TotalMatchingRecords is the cached count of records matching the query. | [optional] 

## Example

```python
from suger_sdk_python.models.pkg_handler_get_enrichment_progress_response import PkgHandlerGetEnrichmentProgressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkgHandlerGetEnrichmentProgressResponse from a JSON string
pkg_handler_get_enrichment_progress_response_instance = PkgHandlerGetEnrichmentProgressResponse.from_json(json)
# print the JSON string representation of the object
print(PkgHandlerGetEnrichmentProgressResponse.to_json())

# convert the object into a dict
pkg_handler_get_enrichment_progress_response_dict = pkg_handler_get_enrichment_progress_response_instance.to_dict()
# create an instance of PkgHandlerGetEnrichmentProgressResponse from a dict
pkg_handler_get_enrichment_progress_response_from_dict = PkgHandlerGetEnrichmentProgressResponse.from_dict(pkg_handler_get_enrichment_progress_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


