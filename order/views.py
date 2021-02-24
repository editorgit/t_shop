from django.shortcuts import render


from order.models import Order

SQL = """SELECT c.customer_id, c.first_name,
        c.last_name,
        e.email_address, e.email_id,
        o.order_number, o.order_id,
        ARRAY_AGG(
            CASE
                WHEN cp.product_id IS NOT NULL THEN
                    JSONB_BUILD_OBJECT(
                        'product_name', cp.product_name,
                        'price', cp.price
                    )
                ELSE
                    JSONB_BUILD_OBJECT(
                        'product_name', ncp.product_name,
                        'price', ncp.price
                    )
            END
        ) products
    FROM orders o
    INNER JOIN order_status os ON os.status_id = o.status_id
    INNER JOIN customers c ON c.customer_id = o.customer_id
    INNER JOIN emails e ON e.email_id = c.email_id
    INNER JOIN order_items oi ON oi.order_id = o.order_id
    LEFT JOIN custom_products cp ON cp.product_id = oi.product_id
    LEFT JOIN non_custom_products ncp ON ncp.p_id = oi.p_id
    WHERE os.paid IS TRUE
    GROUP BY c.first_name,c.last_name, c.customer_id, e.email_id,
        e.email_address,
        o.order_number, o.order_id"""


def test_view(request):
    orders = Order.objects.raw(SQL)
    context = {
        'orders': orders
    }
    return render(request, 'test_view.html', context=context)
