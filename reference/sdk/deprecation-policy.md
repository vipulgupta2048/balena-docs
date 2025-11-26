# SDK deprecation policy

Balena SDKs follow [semantic versioning](https://semver.org/) for every officially supported language. Understanding the deprecation window helps you plan upgrades and keep production fleets compatible with balenaCloud.

## Policy highlights

- We guarantee that the final release of a major version remains compatible with balenaCloud services for **one year** after the subsequent major version ships. Example: if v13.0.0 is released today, the most recent v12.x build remains supported for twelve more months.
- After that period, older major versions are considered deprecated and may lose functionality that depends on cloud-side changes.
- Six months after the new major version appears, the older CLI and SDK releases begin printing deprecation warnings during interactive use.
- Once the one-year window elapses, those releases exit with an error unless the `--unsupported` flag (CLI) or equivalent override is supplied.

## Recommended actions

- Pin to the latest major release that your application supports and schedule periodic dependency reviews.
- Watch the [balena SDK release notes](https://github.com/balena-io/balena-sdk/releases) and [balena CLI releases](https://github.com/balena-io/balena-cli/releases) to stay ahead of breaking changes.
- Include SDK upgrades in staging or integration tests so you can adopt new backend features without service interruptions.
