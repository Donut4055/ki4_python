{
    'name': 'Hotel Management',
    'version': '1.0',
    'category': 'Services',
    'summary': 'Quản lý khách sạn - Phòng và Booking',
    'description': """
        Module quản lý khách sạn bao gồm:
        - Quản lý phòng và loại phòng
        - Quản lý khách hàng
        - Quản lý đặt phòng (Booking)
        - Quản lý dịch vụ đi kèm
    """,
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/hotel_security.xml',
        'security/ir.model.access.csv',
        
        'views/hotel_room_type_views.xml',
        'views/hotel_service_views.xml',
        'views/hotel_customer_views.xml',
        'views/hotel_room_views.xml',
        'views/hotel_booking_views.xml',
        'views/hotel_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
