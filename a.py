import os

# اسم المشروع
project_name = "dhallati_project"

# هيكل المجلدات والملفات
structure = {
    project_name: {
        "manage.py": "",
        "requirements.txt": "",
        project_name: {
            "__init__.py": "",
            "settings.py": "",
            "urls.py": "",
            "wsgi.py": "",
            "asgi.py": "",
            "routing.py": ""
        },
        "accounts": {
            "__init__.py": "",
            "admin.py": "",
            "apps.py": "",
            "models.py": "",
            "views.py": "",
            "urls.py": "",
            "forms.py": "",
            "migrations": {}
        },
        "items": {
            "__init__.py": "",
            "admin.py": "",
            "apps.py": "",
            "models.py": "",
            "views.py": "",
            "urls.py": "",
            "forms.py": "",
            "ai_matching.py": "",
            "migrations": {}
        },
        "admin_panel": {
            "__init__.py": "",
            "views.py": "",
            "urls.py": "",
            "forms.py": "",
            "decorators.py": ""
        },
        "notifications": {
            "__init__.py": "",
            "models.py": "",
            "consumers.py": "",
            "routing.py": "",
            "migrations": {}
        },
        "templates": {
            "base.html": "",
            "index.html": "",
            "accounts": {
                "login.html": "",
                "register.html": "",
                "profile.html": ""
            },
            "items": {
                "report_item.html": "",
                "search.html": "",
                "item_detail.html": "",
                "my_items.html": ""
            },
            "admin_panel": {
                "dashboard.html": "",
                "users.html": "",
                "reports.html": "",
                "verify_report.html": "",
                "system_logs.html": ""
            }
        },
        "static": {
            "css": {
                "style.css": ""
            },
            "js": {
                "main.js": "",
                "notifications.js": "",
                "admin.js": ""
            },
            "images": {}
        },
        "media": {
            "items": {}
        }
    }
}

def create_structure(base_path, structure_dict):
    for name, content in structure_dict.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

# إنشاء المشروع
create_structure(".", structure)

print(f"تم إنشاء مشروع {project_name} وهيكله بالكامل.")
