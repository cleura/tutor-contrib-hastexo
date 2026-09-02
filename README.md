# Tutor plugin for the [Stackamole Guacamole Client](https://github.com/cleura/stackamole-xblock/tree/master/stackamole_guacamole_client)


This is a plugin for [Tutor](https://docs.tutor.overhang.io) that deploys the [stackamole Guacamole Client](https://github.com/cleura/stackamole-xblock/tree/master/stackamole_guacamole_client) application alongside Open edX.
Using this plugin is neccessary for running the [Stackamole XBlock](https://github.com/cleura/stackamole-xblock) in your Tutor Open edX platform.

This repository was previously named `tutor-contrib-hastexo`, and renamed to `tutor-contrib-stackamole` in May 2026. See [`MIGRATION.md`](MIGRATION.md) for migration notes.

## Version compatibility matrix

You must install a supported release of this plugin to match the Open edX and Tutor version you are deploying.
If you are installing this plugin from a branch in this Git repository, you must select the appropriate one:

| Open edX release | Tutor version     | Stackamole XBlock version   | Plugin branch | Plugin release |
|------------------|-------------------|-----------------------------|---------------|----------------|
| Lilac            | `>=12.0, <13`     | Not supported               | Not supported | Not supported  |
| Maple            | `>=13.2, <14`[^1] | `hastexo-xblock>=6.0, <7.0` | `maple`       | 0.3.x          |
| Nutmeg           | `>=14.0, <15`     | `hastexo-xblock>=7.0, <8.0` | `quince`      | `>=1.0, <2`    |
| Olive            | `>=15.0, <16`     | `hastexo-xblock>=7.5, <8.0` | `quince`      | `>=1.0, <2`    |
| Palm             | `>=16.0, <17`     | `hastexo-xblock>=7.5, <8.0` | `quince`      | `>=1.0, <2`    |
| Quince           | `>=17.0, <18`     | `hastexo-xblock>=7.9, <8.0` | `quince`      | `>=1.0, <2`    |
| Redwood          | `>=18.0, <19`     | `hastexo-xblock>=8.0, <9.0` | `ulmo`        | `>=2`          |
| Sumac            | `>=19.0, <20`     | `hastexo-xblock>=8.4, <9.0` | `ulmo`        | `>=2.1`        |
| Teak             | `>=20.0, <21`     | `hastexo-xblock>=8.5, <9.0` | `ulmo`        | `>=2.3`        |
| Ulmo             | `>=21.0, <22`     | `hastexo-xblock>=8.6, <9.0` | `ulmo`        | `>=2.4`        |
| Ulmo             | `>=21.0, <22`     | `stackamole-xblock>=9.0.0`  | `main`        | `>=3.0`        |
| Verawood         | `>=22.0, <23`     | `stackamole-xblock>=9.0.0`  | `main`        | `>=3.3`        |

[^1]: For Open edX Maple and Tutor 13, you must run version 13.2.0 or later.
      That is because this plugin uses the Tutor v1 plugin API, [which was introduced with that release](https://github.com/overhangio/tutor/blob/master/CHANGELOG.md#v1320-2022-04-24).

## Installation

First of all, before installing this plugin, make sure you have installed the [Stackamole XBlock](https://github.com/cleura/stackamole-xblock) to your Open edX platform running with Tutor.
For that, add the XBlock to your `OPENEDX_EXTRA_PIP_REQUIREMENTS` in `config.yml`:

```yaml
OPENEDX_EXTRA_PIP_REQUIREMENTS:
- git+https://github.com/cleura/stackamole-xblock.git
```

Rebuild the `openedx` docker image:

```bash
tutor images build openedx
```

Then upload the image to the registry of your choice, and set `DOCKER_IMAGE_OPENEDX` in your `config.yml` to reference that image.

For more information about installing XBlocks, please refer to the [Tutor documentation for installing XBlocks](https://docs.tutor.overhang.io/configuration.html#installing-extra-xblocks-and-requirements).

Then, to install this plugin, run:

```bash
pip install git+https://github.com/cleura/tutor-contrib-stackamole@v3.3.0
```

To enable this plugin, run:

```bash
tutor plugins enable stackamole
```

Before starting Tutor, build the docker image for the `stackamole`
service:

```bash
tutor images build stackamole
```

then (as with the `openedx` image) upload the image to your preferred registry, and set `STACKAMOLE_DOCKER_IMAGE` to point to that image.

## Configuration

* `STACKAMOLE_XBLOCK_SETTINGS`: The Stackamole XBlock settings, examples and details provided in the [XBlock README](https://github.com/cleura/hastexo-xblock#deployment). (default: `{}`)
* `STACKAMOLE_XBLOCK_VERSION`: The Stackamole XBlock version. (default: `stable`)
* `STACKAMOLE_GUACD_VERSION`: [guacd version](https://guacamole.apache.org/releases/) (default: `1.5.2`)
* `STACKAMOLE_GUACD_DOCKER_IMAGE`: [guacd](https://hub.docker.com/r/guacamole/guacd) Docker image version. (default: `guacamole/guacd:1.5.2`)
* `STACKAMOLE_REPLICA_COUNT`: Number of replicas for the `stackamole-xblock` service. (default: `1`)
* `STACKAMOLE_ENABLE_SUSPENDER`: If `True`, run 1 pod in the `stackamole-xblock-suspender` deployment.
  If `False`, run 0 pods, effectively disabling the deployment. (Default: `True`).
* `STACKAMOLE_ENABLE_REAPER`: If `True`, run 1 pod in the `stackamole-xblock-reaper` deployment.
  If `False`, run 0 pods, effectively disabling the deployment. (Default: `True`).

## Using a custom terminal font

When using the `terminal_font_name` setting via `STACKAMOLE_XBLOCK_SETTINGS`, the requested font *must be installed in the guacd container*.
This means that you'll need to build a custom `guacd` image.
For that:

* Define the `STACKAMOLE_GUACD_DOCKER_IMAGE` in your `config.yml` to override using the default upstream image.
* Create a YAML plugin to patch `stackamole-guacd-dockerfile` and add your font installation steps. For example:
  ```yaml
  name: guacdfonts
  version: 1.0.0
  patches:
    stackamole-guacd-dockerfile: |
      USER root
      RUN apt update && apt install -y fonts-hack-ttf
  ```
* Enable the YAML plugin and save your configuration changes (`tutor config save`)
* Build the custom docker image for `guacd`:
  ```bash
  tutor images build guacd
  ```

## License

This software is licensed under the terms of the AGPLv3.
