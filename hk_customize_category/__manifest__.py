{
    "name": "HK Customize Category",
    "version": "1.0",
    "summary": "Personnalise les catégories par défaut sur le site web",
    "author": "matthieu",
    "category": "Website",
    "depends": ["website_sale"],
    "data": [
        "views/category_template.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "/hk_customize_category/static/src/scss/style.scss",
        ],
    },
    "installable": True,
    "application": False,
}
