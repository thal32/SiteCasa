{
    'name': 'HK Website Front',
    'description': '...',
    'category': '',
    'version': '17.0.0.0.0',
    'author': 'Kael Andria',
    'license': 'LGPL-3',
    'depends': ['website', 'website_sale', 'website_sale_wishlist'],
    'data': [
        'views/home.xml',
        'views/layout.xml',
        'views/shop.xml',
        'views/fields_shop.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/hk_front_website/static/src/js/hk_js.js',
            '/hk_front_website/static/src/scss/hk_style.scss',
        ],
    },
}
