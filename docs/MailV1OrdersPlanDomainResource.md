# MailV1OrdersPlanDomainResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mailbox_quota** | **int** | Maximum number of mailboxes per domain | [optional] 
**forwarder_quota** | **int** | Maximum number of forwarders per domain | [optional] 
**alias_quota** | **int** | Maximum number of aliases per domain | [optional] 
**is_catchall_enabled** | **bool** | Whether catch-all mailboxes are available | [optional] 
**is_imap_enabled** | **bool** | Whether IMAP access is available | [optional] 
**is_pop3_enabled** | **bool** | Whether POP3 access is available | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_orders_plan_domain_resource import MailV1OrdersPlanDomainResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1OrdersPlanDomainResource from a JSON string
mail_v1_orders_plan_domain_resource_instance = MailV1OrdersPlanDomainResource.from_json(json)
# print the JSON string representation of the object
print(MailV1OrdersPlanDomainResource.to_json())

# convert the object into a dict
mail_v1_orders_plan_domain_resource_dict = mail_v1_orders_plan_domain_resource_instance.to_dict()
# create an instance of MailV1OrdersPlanDomainResource from a dict
mail_v1_orders_plan_domain_resource_from_dict = MailV1OrdersPlanDomainResource.from_dict(mail_v1_orders_plan_domain_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


