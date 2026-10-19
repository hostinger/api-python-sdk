# WordPressV1InstallationsInstallWordPressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain of the existing website where WordPress will be installed | 
**site_title** | **str** | Title of the WordPress site | 
**language** | **str** | WordPress locale. Defaults to en_US when omitted. | [optional] 
**type** | **str** | Installation kind; &#x60;default&#x60; when omitted. &#x60;headless&#x60; installs WordPress into the &#x60;cms&#x60; directory with the Hostinger headless MU plugin and marks the website as a headless WordPress website. Accepted only for a website that is already headless, e.g. one created by &#x60;POST /api/hosting/v1/orders/{order_id}/onboardings&#x60; (&#x60;hosting_websites_start-setup&#x60;) with &#x60;type: headless_empty&#x60;; any other website is rejected with 422. | [optional] 
**directory** | **str** | Installation subdirectory relative to the document root; omit for the root. Not allowed with &#x60;type: headless&#x60;, which always installs into &#x60;cms&#x60;. | [optional] 
**overwrite** | **bool** | When false (default), does not replace an existing installation. If WordPress is already installed on the domain/path, the async install job fails unless true. | [optional] 
**auto_updates** | **str** | WordPress core auto-update policy | [optional] 
**version** | **str** | WordPress core version to install. If omitted, the latest core version compatible with the account vhost PHP version is selected. | [optional] 
**credentials** | [**WordPressV1InstallationsInstallWordPressRequestCredentials**](WordPressV1InstallationsInstallWordPressRequestCredentials.md) |  | 
**database** | [**WordPressV1InstallationsInstallWordPressRequestDatabase**](WordPressV1InstallationsInstallWordPressRequestDatabase.md) |  | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_installations_install_word_press_request import WordPressV1InstallationsInstallWordPressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1InstallationsInstallWordPressRequest from a JSON string
word_press_v1_installations_install_word_press_request_instance = WordPressV1InstallationsInstallWordPressRequest.from_json(json)
# print the JSON string representation of the object
print(WordPressV1InstallationsInstallWordPressRequest.to_json())

# convert the object into a dict
word_press_v1_installations_install_word_press_request_dict = word_press_v1_installations_install_word_press_request_instance.to_dict()
# create an instance of WordPressV1InstallationsInstallWordPressRequest from a dict
word_press_v1_installations_install_word_press_request_from_dict = WordPressV1InstallationsInstallWordPressRequest.from_dict(word_press_v1_installations_install_word_press_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


