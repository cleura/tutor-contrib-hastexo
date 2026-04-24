from .__about__ import __version__
from glob import glob
import os
# When Tutor drops support for Python 3.8, we'll need to update this to:
# from importlib import resources as importlib_resources
# See: https://github.com/overhangio/tutor/issues/966#issuecomment-1938681102
import importlib_resources
from tutor import hooks


config = {
    "unique": {
        "XBLOCK_SETTINGS": {},
        "SECRET_KEY": "{{ 50|random_string }}",
    },
    "defaults": {
        "VERSION": __version__,
        "GUACD_VERSION": "1.5.5",
        "GUACD_BASE_IMAGE": "guacamole/guacd:{{ STACKAMOLE_GUACD_VERSION }}",
        "GUACD_DOCKER_IMAGE": "{{ STACKAMOLE_GUACD_BASE_IMAGE }}",
        "BASE_IMAGE": "docker.io/python:3.11",
        "DOCKER_IMAGE": "{{ DOCKER_REGISTRY }}stackamole:{{ STACKAMOLE_VERSION }}",  # noqa: E501
        "XBLOCK_VERSION": "stable",
        "DEBUG": False,
        "REPLICA_COUNT": 1,
        "ENABLE_REAPER": True,
        "ENABLE_SUSPENDER": True,
    }
}

image_tags = {
    "stackamole": "{{ STACKAMOLE_DOCKER_IMAGE }}",
    "guacd": "{{ STACKAMOLE_GUACD_DOCKER_IMAGE }}",
}

for image, tag in image_tags.items():
    hooks.Filters.IMAGES_BUILD.add_item((
        image,
        ("plugins", "stackamole", "build", image),
        tag,
        (),
    ))
    hooks.Filters.IMAGES_PULL.add_item((image, tag))
    hooks.Filters.IMAGES_PUSH.add_item((image, tag))

# Add the "templates" folder as a template root
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    str(importlib_resources.files("tutorstackamole") / "templates")
)
# Render the "build" and "apps" folders
hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("stackamole/build", "plugins"),
        ("stackamole/apps", "plugins"),
    ],
)
# Load patches from files
for path in glob(str(
        importlib_resources.files("tutorstackamole") / "patches" / "*")):

    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item(
            (os.path.basename(path), patch_file.read())
        )
# Add configuration entries
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        (f"STACKAMOLE_{key}", value)
        for key, value in config.get("defaults", {}).items()
    ]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [
        (f"STACKAMOLE_{key}", value)
        for key, value in config.get("unique", {}).items()
    ]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(
    list(config.get("overrides", {}).items())
)
