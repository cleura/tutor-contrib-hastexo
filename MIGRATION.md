# Migrating from the hastexo plugin to the stackamole plugin

This project was renamed to `tutor-contrib-stackamole` in May 2026.

To migrate your project, using Tutor, do the following:
1. Install and enable `git+https://github.com/cleura/tutor-contrib-stackamole@v3.0.0` (`v3.0.0` or higher) in your Tutor environment.
2. In the Tutor `config.yml` file, add `stackamole-xblock>=9.0.0` to the `OPENEDX_EXTRA_PIP_REQUIREMENTS` list.
3. Rename all your `HASTEXO_*` settings in `config.yml` to `STACKAMOLE_*`.
4. Update the `terminal_url` in your `STACKAMOLE_XBLOCK_SETTINGS` to `/stackamole-xblock/`.
5. Run `tutor config save`.
6. Rebuild the `openedx` and `stackamole` images.
7. Run `tutor local/k8s launch`.
   This includes running the migration script to rename the data tables.
8. (Optional) Depending on your deployment setup, you might need to delete the `hastexo` deployments once all other steps are completed.
   For example, in a `k8s` environment, run:
   ```bash
    kubectl -n <namespace> delete deployment hastexo-xblock
    kubectl -n <namespace> delete deployment hastexo-xblock-reaper
    kubectl -n <namespace> delete deployment hastexo-xblock-suspender
   ```
