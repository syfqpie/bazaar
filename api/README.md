# Bazaar - Marketplace API 🛒

> A bazaar (Persian: بازار) or souk (Arabic: سوق, romanized: sūq; also transliterated as souq)
> is a marketplace consisting of multiple small stalls or shops, especially in the Middle East,
> North Africa, and India.

## Installation

Create virtual environment

```bash
  virtualenv env --python=python3 --copies
```

Get into your created virtual environment - Windows

```bash
  env\Scripts\activate
```

Get into your created virtual environment - Mac / Ubuntu

```bash
  source env/bin/activate
```

Install all packages from requirements.txt

```bash
  pip install -r requirements.txt
```

Make migrations

```bash
  python manage.py makemigrations
```

Migrate the migrations

```bash
  python manage.py migrate
```

Create superuser

```bash
  python manage.py createsuperuser
```

Run the django rest framework

```bash
  python manage.py runserver
```

## References

- [Django REST Framework](https://www.django-rest-framework.org)
- [Postdrop](https://app.postdrop.io)
- [MailHog](https://github.com/mailhog/MailHog)
- [Flaticon](https://www.flaticon.com)