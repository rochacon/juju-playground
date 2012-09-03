JuJu Playground
===============

Some fun with Ubuntu's JuJu.

Usage example:
```bash
juju deploy --repository=charms hello <name for the hello app service>
juju deploy gunicorn
juju add-relation gunicorn <name for the hello app service>
juju expose gunicorn
```

