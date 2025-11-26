# balena CLI

The balena CLI is the command-line companion to balenaCloud. Use it to push releases, configure devices, automate workflows, and interact with the balenaCloud API from scripts or CI pipelines.

## Installation

Check the [INSTALL.md](https://github.com/balena-io/balena-cli/blob/master/INSTALL.md) guide for platform-specific steps. Package managers and standalone binaries are available for macOS, Windows, and Linux.

:::info Upgrading from v21 or earlier?
Review the [v22 migration guide](https://github.com/balena-io/balena-cli/blob/master/MIGRATIONS.md) if you are moving from a standalone install. The release introduces a new packaging model.
:::

## Logging in

Authenticate with your balenaCloud account before running commands that act on fleets or devices:

```sh
balena login
```

You can log in with username/password, web authorization, tokens, or SSH keys. For CI environments, generate a user or fleet token and use `balena login --token <TOKEN>`.

## Common commands

- **Releases:** `balena push`, `balena deploy`, `balena build`
- **Fleet management:** `balena fleet ls`, `balena fleet rename`, `balena fleet purge`
- **Device lifecycle:** `balena device register`, `balena device os-update`, `balena device public-url`
- **Local workflows:** `balena local configure`, `balena local flash`, `balena env set`
- **Diagnostics:** `balena logs -f <uuid>`, `balena ssh <uuid>`, `balena tunnel <uuid> 22222`

Use `balena help <command>` for detailed syntax and options.

## Proxy support

The CLI honours the following environment variables in precedence order:

1. `BALENARC_PROXY` — URL with optional credentials (`https://user:pass@proxy.company.com:12345`)
2. `proxy` entry in the [CLI config file](https://www.npmjs.com/package/balena-settings-client#documentation)
3. `HTTPS_PROXY` / `HTTP_PROXY`

To exclude hosts from proxying, set `BALENARC_NO_PROXY` with a comma-separated list such as `*.local,192.168.*`. SSH tunnelling behind proxies requires the [`proxytunnel`](http://proxytunnel.sourceforge.net/) utility and proxy rules that allow port 22.

## Troubleshooting

- Consult the [CLI troubleshooting guide](https://github.com/balena-io/balena-cli/blob/master/TROUBLESHOOTING.md) for platform-specific quirks.
- Ask questions in the [balena forums](https://forums.balena.io/c/product-support).
- File issues or feature requests on the [balena CLI GitHub repository](https://github.com/balena-io/balena-cli/issues).

## Command reference by version

Complete generated command docs are published per release. Pick the version that matches your installation:

- [Latest release](https://balena-cli.readme.io/)
- [v21.1.14](https://balena-cli-v21.readme.io/)
- [v20.2.10](https://balena-cli-v20.readme.io/)
- [v19.16.0](https://balena-cli-v19.readme.io/)

Older releases remain available through the [balena-cli-versions repository](https://github.com/balena-io/balena-cli/tree/master/docs).