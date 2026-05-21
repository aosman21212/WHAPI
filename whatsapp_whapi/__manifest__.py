{
    'name': 'WhatsApp Whapi',
    'version': '19.0.1.0.0',
    'category': 'Productivity',
    'summary': 'WhatsApp integration via Whapi.Cloud API',
    'description': """
WhatsApp Whapi — Full WhatsApp Integration for Odoo 19
======================================================

Standalone WhatsApp inbox powered by Whapi.Cloud (gate.whapi.cloud).

Features
--------
* Real-time inbox: send and receive all message types (text, image, video,
  audio, document, location, poll, interactive, carousel, sticker)
* Multi-channel support: manage multiple WhatsApp numbers from one Odoo instance
* Contacts & Groups: sync contacts, validate phone numbers, manage group participants
* Business Catalog: sync products, collections, and orders from WhatsApp Business
* Newsletters: manage WhatsApp Channels (subscribe / unsubscribe)
* Media Library: upload and reuse media files; attach Odoo ir.attachments
* Webhooks: real-time incoming message delivery via Whapi.Cloud webhook
* Auto-sync: scheduled cron jobs to keep chats and contacts up-to-date
* QR Code Login: link your WhatsApp number by scanning a QR code from Odoo
* API Logs: full audit trail of every Whapi.Cloud API call
* Role-based access: WhatsApp User and WhatsApp Manager security groups

Author: leapai.ai — https://leapai.ai/en/
Support: abdzoro89@gmail.com
Maintainer: a.osman@bab.com.sa
    """,
    'author': 'leapai.ai',
    'website': 'https://leapai.ai/en/',
    'support': 'abdzoro89@gmail.com',
    'maintainer': 'a.osman@bab.com.sa',
    'license': 'LGPL-3',
    'images': [
        'static/description/banner.png',
        'static/description/icon.png',
        'static/description/screenshot_inbox.png',
        'static/description/screenshot_features.png',
        'static/description/screenshot_channels.png',
    ],
    'depends': ['base', 'web', 'mail'],
    'external_dependencies': {
        'python': ['requests'],
    },
    'data': [
        'security/whatsapp_security.xml',
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'views/whatsapp_channel_views.xml',
        'views/whatsapp_chat_views.xml',
        'views/whatsapp_message_views.xml',
        'views/whatsapp_contact_views.xml',
        'views/whatsapp_group_views.xml',
        'views/whatsapp_media_views.xml',
        'views/whatsapp_newsletter_views.xml',
        'views/whatsapp_product_views.xml',
        'views/whatsapp_collection_views.xml',
        'views/whatsapp_order_views.xml',
        'views/whatsapp_api_log_views.xml',
        'views/whatsapp_menus.xml',
        'views/whatsapp_inbox_action.xml',
        'wizards/whatsapp_qr_login_views.xml',
        'wizards/whatsapp_send_message_views.xml',
        'wizards/whatsapp_check_phones_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'whatsapp_whapi/static/src/components/whapi_inbox/whapi_inbox.js',
            'whatsapp_whapi/static/src/components/whapi_inbox/whapi_inbox.xml',
            'whatsapp_whapi/static/src/components/whapi_inbox/whapi_inbox.scss',
        ],
    },
    'installable': True,
    'application': True,
}
