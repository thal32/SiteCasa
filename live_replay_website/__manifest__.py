{
    "name": "Live Replay Website",
    "version": "1.0",
    "depends": ["website", "website_sale","product"],
    "author": "Matthieu",
    "category": "Website",
    "data": [
        "security/ir.model.access.csv",
        "views/live_replay_views.xml",
        "views/website_templates.xml",
    ],
    "views": [
        "views/replay_detail_template.xml",
    ],
    "installable": True,
}
