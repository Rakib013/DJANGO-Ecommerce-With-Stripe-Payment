from django.contrib import admin
from . models import Order, OrderItem, Item, Address, Payment, Coupon, Refund



def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount_price',]
    list_editable = ['price', 'discount_price']
    list_filter = ['category', 'label', 'price']
    prepopulated_fields = {"slug": ("title", )}


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['item', 'quantity']
    list_editable = ['quantity']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered', 'being_delivered', 'refund_requested', 'refund_granted', 'billing_address', 'payment', 'coupon', 'ordered_date']
    list_display_links = ['user', 'billing_address', 'payment', 'coupon',]
    search_fields = ['user__username', 'ref_code']
    list_editable = ['ordered']
    list_filter = ['ordered', 'being_delivered', 'refund_requested', 'refund_granted',]
    actions = [make_refund_accepted]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'street_address', 'apartment_address', 'country', 'zip', 'address_type', 'default']


admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)