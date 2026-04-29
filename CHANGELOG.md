# Version 2.4.0 (2026-01-23)

* [Enhancement] Support Tutor 21 and Open edX Ulmo.

# Version 2.3.1 (2026-01-16)

* Point release to mark the GitHub repository move.

# Version 2.3.0 (2025-07-28)

* [Enhancement] Support Tutor 20 and Open edX Teak.

# Version 2.2.0 (2025-04-15)

* [Enhancement] Allow to override the Dockerfile base image.

# Version 2.1.0 (2025-01-03)

* Bump the default `guacd` version.
* Support Tutor 19 and Open edX Sumac.

# Version 2.0.0 (2024-10-07)

* Drop support for Python 3.8.

When updating your plugin to this version, you'll need to rebuild the image.

# Version 1.6.0 (2024-08-07)

* [Enhancement] Support Tutor 18 and Open edX Redwood.

# Version 1.5.1 (2024-04-30)

* [Bug fix] Install the Hastexo XBlock code in the right context (in the current directory).

# Version 1.5.0 (2024-04-05)

* [Enhancement] Support Python 3.12.

# Version 1.4.0 (2024-01-12)

* [Enhancement] Support Tutor 17 and Open edX Quince.

## Version 1.3.0 (2023-08-21)

* [Enhancement] Support Tutor 16 and Open edX Palm, Python 3.10, and Python 3.11.

# Version 1.2.0 (2023-06-28)

* Bump the default guacd version from 1.4.0 to 1.5.2.

# Version 1.1.0 (2023-03-20)

* Add support for Open edX Olive.

# Version 1.0.0 (2022-08-19)

* BREAKING CHANGE: Support Tutor 14 and Open edX Nutmeg.
  This entails a configuration format change from JSON to YAML, meaning that from version 1.0.0 this plugin only supports Tutor versions from 14.0.0 (and with that, only Open edX versions from Nutmeg).

* BREAKING CHANGE: Update the `ASGI_APPLICATION` definition and add `LMS_HOST` to `ALLOWED_HOSTS` to support running the `hastexo_guacamole_client` with Channels 3.

# Version 0.3.0 (2022-06-29)

* Use Tutor v1 plugin API

# Version 0.2.0 (2022-06-28)

* Add `HASTEXO_ENABLE_SUSPENDER` and `HASTEXO_ENABLE_REAPER` to effectively enable/disable the `suspender` and `reaper` deployments (by setting their respective replica counts to 1 or 0).
* Add an option to scale the number of instances via `HASTEXO_REPLICA_COUNT` setting.

# Version 0.1.0 (2022-04-20)

* Refactor the way we add `HASTEXO_XBLOCK_SETTINGS` to the `XBLOCK_SETTINGS`.
  Add the settings under the `hastexo` key without overriding the general definition.
* Fix terminal customisation options.
  Override the default settings module for the `hastexo_guacamole_client` so that the `XBLOCK_SETTINGS` will be present in the `hastexo` container and thus, will make it possible to define custom settings for the terminal window.
* Add support for installing custom fonts for terminal.
  The required font will have to be installed in the `guacd` container.
  Add an option to build a custom `guacd` image while keeping the option of using the upstream base image in case a custom font is not needed.

## Version 0.0.2 (2022-02-25)

* Fix version number as it appears in pip list (previously, all installations would show up as version 0.0.0, including installations from the 0.0.1 tag).

## Version 0.0.1 (2022-02-24)

**Experimental. Do not use in production.**

* Add basic testing via tox
* Initial Git import
