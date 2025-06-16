{
    "name": "Image Comparator",
    "version": "1.0",
    "depends": ["base"],
    "category": "Tools",
    "description": "Compare two images and compute similarity.",
    "data": [
        "security/ir.model.access.csv",
        "views/image_gallery_views.xml",
        "views/image_comparator_views.xml",
        "views/gallery_comparaison_views.xml",
        "views/image_comparator_menus.xml",
        "views/assets.xml",
    ],
    'external_dependencies': {
        'python': ['Pillow', 'ImageHash', ],
    },
    'assets': {
        'web.assets_backend': [
        
        ],
    },
    "installable": True,
    "application": True,
    "auto_install": False
}