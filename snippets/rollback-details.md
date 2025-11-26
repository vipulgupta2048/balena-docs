# Rollback Details

Below are sample configurations and diagnostic logs for both rollback mechanisms:

```bash
# rollback-health service configuration example
# File: /etc/systemd/system/rollback-health.service
[Unit]
Description=Toggle rollback based on health checks

[Service]
Type=oneshot
ExecStart=/usr/bin/rollback-health --timeout $ROLLBACK_HEALTH_TIMEOUT

# rollback-altboot bootloader check logs
# Example output from U-Boot environment
# bootcount=2
# upgrade_available=1
```

```bash
# Diagnostic log snippet after rollback-altboot
Sep 01 12:00:00 kernel: [    0.000000] Bootloader: Switching to alternate boot partition
Sep 01 12:00:02 systemd[1]: rollback-altboot.service: Completed
```
