# GithubComSugerioMarketplaceServicePkgOrmNotificationMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_time** | **datetime** | CreationTime holds the value of the \&quot;creation_time\&quot; field. | [optional] 
**id** | **str** | ID of the ent. | [optional] 
**info** | [**NotificationMessageInfo**](NotificationMessageInfo.md) | Info holds the value of the \&quot;info\&quot; field. | [optional] 
**organization_id** | **str** | OrganizationID holds the value of the \&quot;organization_id\&quot; field. | [optional] 
**recipient** | **str** | supports multiple recipients as a comma-separated string | [optional] 
**type** | [**GithubComSugerioMarketplaceServicePkgOrmNotificationmessageType**](GithubComSugerioMarketplaceServicePkgOrmNotificationmessageType.md) | Type holds the value of the \&quot;type\&quot; field. | [optional] 

## Example

```python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_orm_notification_message import GithubComSugerioMarketplaceServicePkgOrmNotificationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComSugerioMarketplaceServicePkgOrmNotificationMessage from a JSON string
github_com_sugerio_marketplace_service_pkg_orm_notification_message_instance = GithubComSugerioMarketplaceServicePkgOrmNotificationMessage.from_json(json)
# print the JSON string representation of the object
print(GithubComSugerioMarketplaceServicePkgOrmNotificationMessage.to_json())

# convert the object into a dict
github_com_sugerio_marketplace_service_pkg_orm_notification_message_dict = github_com_sugerio_marketplace_service_pkg_orm_notification_message_instance.to_dict()
# create an instance of GithubComSugerioMarketplaceServicePkgOrmNotificationMessage from a dict
github_com_sugerio_marketplace_service_pkg_orm_notification_message_from_dict = GithubComSugerioMarketplaceServicePkgOrmNotificationMessage.from_dict(github_com_sugerio_marketplace_service_pkg_orm_notification_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


