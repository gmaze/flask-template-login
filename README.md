# Flask-app template: Authentication with Flask-Login

Largely inspired by https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login#step-2-creating-the-main-app-file with bug fixes

# Installation

```bash
mamba env create -f environment.yml
```

```python
from recovery_webapp import db, create_app, models
app = create_app()
with app.app_context():
    db.create_all()
```