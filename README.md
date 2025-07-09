Tutor plugin for the [Hastexo Guacamole Client](https://github.com/hastexo/hastexo-xblock/tree/master/hastexo_guacamole_client)
===============================================


This is a plugin for [Tutor](https://docs.tutor.overhang.io) that
deploys the [Hastexo Guacamole
Client](https://github.com/hastexo/hastexo-xblock/tree/master/hastexo_guacamole_client)
application alongside Open edX.  Using this plugin is neccessary for
running the [Hastexo
XBlock](https://github.com/hastexo/hastexo-xblock) in your Tutor Open
edX platform.

Version compatibility matrix
----------------------------

You must install a supported release of this plugin to match the Open
edX and Tutor version you are deploying. If you are installing this
plugin from a branch in this Git repository, you must select the
appropriate one:

| Open edX release | Tutor version     | Hastexo XBlock version | Plugin branch | Plugin release |
|------------------|-------------------|------------------------|---------------|----------------|
| Lilac            | `>=12.0, <13`     | Not supported          | Not supported | Not supported  |
| Maple            | `>=13.2, <14`[^1] | `>=6.0, <7.0`          | `maple`       | 0.3.x          |
| Nutmeg           | `>=14.0, <15`     | `>=7.0, <7.12`         | `quince`      | `>=1.0, <2`    |
| Olive            | `>=15.0, <16`     | `>=7.0, <7.12`         | `quince`      | `>=1.0, <2`    |
| Palm             | `>=16.0, <17`     | `>=7.0, <7.12`         | `quince`      | `>=1.0, <2`    |
| Quince           | `>=17.0, <18`     | `>=7.0, <7.12`         | `quince`      | `>=1.0, <2`    |
| Redwood          | `>=18.0, <19`     | `>=7.12.0`             | `main`        | `>=2`          |
| Sumac            | `>=19.0, <20`     | `>=7.12.0`             | `main`        | `>=2.1`        |
| Teak             | `>=20.0, <21`     | `>=7.12.0`             | `main`        | `>=2.3`        |

[^1]: For Open edX Maple and Tutor 13, you must run version 13.2.0 or
    later. That is because this plugin uses the Tutor v1 plugin API,
    [which was introduced with that
    release](https://github.com/overhangio/tutor/blob/master/CHANGELOG.md#v1320-2022-04-24).

Installation
------------

First of all, before installing this plugin, make sure you have
installed the [Hastexo
XBlock](https://github.com/hastexo/hastexo-xblock) to your Open edX
platform running with Tutor. For that, add the XBlock to your
`OPENEDX_EXTRA_PIP_REQUIREMENTS` in `config.yml`:

```
OPENEDX_EXTRA_PIP_REQUIREMENTS:
- git+https://github.com/hastexo/hastexo-xblock.git
```

rebuild the `openedx` docker image:

```
tutor images build openedx
```

then upload the image to the registry of your choice, and set
`DOCKER_IMAGE_OPENEDX` in your `config.yml` to reference that image.

For more information about installing XBlocks, please refer to the
[Tutor documentation for installing
XBlocks](https://docs.tutor.overhang.io/configuration.html#installing-extra-xblocks-and-requirements)


Then, to install this plugin, run:

```
pip install git+https://github.com/hastexo/tutor-contrib-hastexo@v2.2.0
```

To enable this plugin, run:

```
tutor plugins enable hastexo
```

Before starting Tutor, build the docker image for the `hastexo`
service:

```
tutor images build hastexo
```

then (as with the `openedx` image) upload the image to your preferred
registry, and set `HASTEXO_DOCKER_IMAGE` to point to that image.

Configuration
-------------

* `HASTEXO_XBLOCK_SETTINGS`: The Hastexo XBlock settings, examples and
  details provided in the [XBlock
  README](https://github.com/hastexo/hastexo-xblock#deployment). (default:
  `{}`)
* `HASTEXO_XBLOCK_VERSION`: The Hastexo XBlock version. (default:
  `stable`)
* `HASTEXO_GUACD_VERSION`: [guacd version](https://guacamole.apache.org/releases/) (default: `1.5.2`)
* `HASTEXO_GUACD_DOCKER_IMAGE`:
  [guacd](https://hub.docker.com/r/guacamole/guacd) Docker image version. (default:
  `guacamole/guacd:1.5.2`)
* `HASTEXO_REPLICA_COUNT`: Number of replicas for the `hastexo-xblock` service.
  (default: `1`)
* `HASTEXO_ENABLE_SUSPENDER`: If `True`, run 1 pod in the `hastexo-xblock-suspender` deployment. 
  If `False`, run 0 pods, effectively disabling the deployment. (Default: `True`).
* `HASTEXO_ENABLE_REAPER`: If `True`, run 1 pod in the `hastexo-xblock-reaper` deployment. 
  If `False`, run 0 pods, effectively disabling the deployment. (Default: `True`).

Using a custom terminal font
----------------------------

When using the `terminal_font_name` setting via `HASTEXO_XBLOCK_SETTINGS`,
the requested font *must be installed in the guacd container*. This means that you'll
need to build a custom `guacd` image. For that:
* Define the `HASTEXO_GUACD_DOCKER_IMAGE` in your `config.yml` to override using the
  default upstream image.
* Create a YAML plugin to patch [hastexo-guacd-dockerfile]() and add your font installation
  steps. For example:
  ```
  name: guacdfonts
  version: 1.0.0
  patches:
    hastexo-guacd-dockerfile: |
      USER root
      RUN apt update && apt install -y fonts-hack-ttf
  ```
* Enable the YAML plugin and save your configuration changes (`tutor config save`)
* Build the custom docker image for `guacd`:
  ```
  tutor images build guacd
  ```

License
-------

This software is licensed under the terms of the AGPLv3.
