# EcommerceV1WebhookUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | HTTPS receiver on port 443, without credentials or a fragment. Omit to preserve. A changed URL must be a public destination under the same rules as creation; resending the saved URL unchanged is accepted. | [optional] 
**events** | **List[str]** | Replacement event types. Omit to preserve.  - &#x60;order.placed&#x60;: a customer places an order, before any online payment is completed. Orders paid online   may not have an order number yet. - &#x60;order.paid&#x60;: an order becomes fully paid: an online payment is captured, a free order is placed or the   merchant marks it as paid. Partial payments don&#39;t send it. - &#x60;order.cancelled&#x60;: an unpaid order is canceled, for example by the merchant, a connected sales channel or   after a delayed payment fails. Paid orders can&#39;t be canceled, so a cancellation never involves a refund. - &#x60;order.refunded&#x60;: each time a full or partial refund is recorded, through the payment provider or   manually. - &#x60;order.fulfilled&#x60;: a fulfillment leaves every item in the order fulfilled. Partial fulfillments send   &#x60;fulfillment.created&#x60; instead. - &#x60;fulfillment.created&#x60;: each time items in an order are fulfilled, including partial fulfillments and   digital items fulfilled automatically after payment. - &#x60;fulfillment.updated&#x60;: a fulfillment&#39;s tracking details change, or a connected shipping service or sales   channel reports progress such as delivery. - &#x60;fulfillment.cancelled&#x60;: a fulfillment is canceled before it ships, for example when it is canceled or   its shipping label is voided. - &#x60;product.created&#x60;: a product is added to the store, including drafts and products created in bulk. - &#x60;product.updated&#x60;: a product changes, including its details, variants, prices, stock, visibility or   collections. Stock changes from orders also send it, so expect frequent events. - &#x60;product.deleted&#x60;: a product is deleted, individually or in bulk. | [optional] 
**sales_channel_ids** | **List[str]** | Omit to preserve; null restores store-wide delivery. Empty or foreign-store IDs are invalid. | [optional] 
**enabled** | **bool** | Merchant-disabled endpoints can be enabled again; lifecycle-revoked endpoints cannot. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_webhook_update_request import EcommerceV1WebhookUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1WebhookUpdateRequest from a JSON string
ecommerce_v1_webhook_update_request_instance = EcommerceV1WebhookUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1WebhookUpdateRequest.to_json())

# convert the object into a dict
ecommerce_v1_webhook_update_request_dict = ecommerce_v1_webhook_update_request_instance.to_dict()
# create an instance of EcommerceV1WebhookUpdateRequest from a dict
ecommerce_v1_webhook_update_request_from_dict = EcommerceV1WebhookUpdateRequest.from_dict(ecommerce_v1_webhook_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


