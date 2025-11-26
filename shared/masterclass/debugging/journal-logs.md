
balenaOS uses [systemd](https://www.freedesktop.org/wiki/Software/systemd/) as
its [init system](https://en.wikipedia.org/wiki/Init), and as such almost all
the fundamental components in balenaOS run as systemd services. systemd builds
a dependency graph of all of its unit files (in which services are defined) to
determine the order that these should be started/shutdown in. This is
generated when systemd is run, although there are ways to rebuild this after
startup and during normal system execution.

Possibly the most important command is `journalctl`, which allows you to read
the service's journal entries. This takes a variety of switches, the most
useful being:

- `--follow`/`-f` - Continues displaying journal entries until the command is halted
  (eg. with Ctrl-C)
- `--unit=<unitFile>`/`-u <unitFile>` - Specifies the unit file to read journal
  entries for. Without this, all units entries are read.
- `--pager-end`/`-e` - Jump straight to the final entries for a unit.
- `--all`/`-a` - Show all entries, even if long or with unprintable
  characters. This is especially useful for displaying the service container
  logs from user containers when applied to `balena.service`.

A typical example of using `journalctl` might be following a service to see
what's occuring. Here's it for the Supervisor, following journal entries in
real time:

```shell
root@9294512:~# journalctl --follow --unit=balena-supervisor
-- Journal begins at Fri 2021-08-06 14:40:59 UTC. --
Aug 18 16:56:55 9294512 balena-supervisor[6890]: [info]    Reported current state to the cloud
Aug 18 16:57:05 9294512 balena-supervisor[6890]: [info]    Reported current state to the cloud
Aug 18 16:58:17 9294512 balena-supervisor[6890]: [info]    Reported current state to the cloud
Aug 18 16:58:27 9294512 balena-supervisor[6890]: [info]    Reported current state to the cloud
Aug 18 16:58:37 9294512 balena-supervisor[6890]: [info]    Reported current state to the cloud
Aug 18 16:58:48 9294512 balena-supervisor[6890]: [info]    Reported current state to the cloud
Aug 18 16:58:58 9294512 balena-supervisor[6890]: [info]    Reported current state to the cloud
Aug 18 16:59:19 9294512 balena-supervisor[6890]: [info]    Reported current state to the cloud
Aug 18 16:59:40 9294512 balena-supervisor[6890]: [info]    Reported current state to the cloud
Aug 18 17:00:00 9294512 balena-supervisor[6890]: [info]    Reported current state to the cloud
```

Any systemd service can be referenced in the same way, and there are some common
commands that can be used with services:

- `systemctl status <serviceName>` - Will show the status of a service. This
  includes whether it is currently loaded and/or enabled, if it is currently
  active (running) and when it was started, its PID, how much memory it is
  notionally (and beware here, this isn't always the amount of physical
  memory) using, the command used to run it and finally the last set of
  entries in its journal log. Here's example output from the OpenVPN service:

  ```shell
