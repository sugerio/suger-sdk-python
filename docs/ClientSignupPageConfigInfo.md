# ClientSignupPageConfigInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cc_emails** | **List[str]** | The cc email contacts of the new client signup notification. | [optional] 
**company_logo_url** | **str** | The company logo url of the seller/ISV. | [optional] 
**company_name** | **str** | The company name of the seller/ISV to show in the client signup page. | [optional] 
**landing_image_url** | **str** | The signup landing image aws url of the organization | [optional] 
**notification_email_subject** | **str** | The email subject of the new client signup notification. | [optional] 
**public_notes** | **str** | The public notes to append in new client signup notification email. | [optional] 
**signup_id** | **str** | The signup ID for the new client signup page url. It is populated by Suger service when creating the new client signup page. | [optional] 
**video_link** | **str** | The video link of the product. Optional. | [optional] 

## Example

```python
from openapi_client.models.client_signup_page_config_info import ClientSignupPageConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClientSignupPageConfigInfo from a JSON string
client_signup_page_config_info_instance = ClientSignupPageConfigInfo.from_json(json)
# print the JSON string representation of the object
print ClientSignupPageConfigInfo.to_json()

# convert the object into a dict
client_signup_page_config_info_dict = client_signup_page_config_info_instance.to_dict()
# create an instance of ClientSignupPageConfigInfo from a dict
client_signup_page_config_info_form_dict = client_signup_page_config_info.from_dict(client_signup_page_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


