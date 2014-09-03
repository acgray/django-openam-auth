django-openam-auth
==================

OpenAM authentication backend for Django

Requirements
------------

* [python-openam](https://github.com/acgray/python-openam)

Installation
------------

Install the `python-openam` package (you have to do this manually as it's not on PyPI yet)

Add `django_openam_auth.authentication_backends.OpenAMJSONBackend` to your `AUTHENTICATION_BACKENDS` setting, e.g.

    AUTHENTICATION_BACKENDS = ('django_openam_auth.authentication_backends.OpenAMJSONBackend', )

Set `OPENAM_ENDPOINT` to the location of your OpenAM installation, e.g.

    OPENAM_ENDPOINT = "https://openam.your.domain.com/openam"

That's it!
