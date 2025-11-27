#!/usr/bin/env python3
import os
import re

files_to_fix = [
    '/Users/vipulgupta2048/work/balena-docs/learn/develop/dockerfile.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/develop/local-mode.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/develop/multicontainer.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/develop/blocks.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/develop/runtime.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/develop/apps.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/develop/hardware/index.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/deploy/delta.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/deploy/build-optimization.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/deploy/deployment.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/deploy/deploy-with-balena-button.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/deploy/release-strategy/release-policy.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/deploy/release-strategy/update-strategies.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/welcome/introduction.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/welcome/primer.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/welcome/production-plan.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/welcome/security.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/getting-started/raspberrypi5/nodejs.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/accounts/organizations.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/accounts/fleet-types.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/accounts/enterprise-sso.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/accounts/account.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/accounts/billing.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/accounts/fleet-members.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/accounts/support-access.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/accounts/idp-setup/microsoft-entra-saml-setup.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/accounts/idp-setup/google-workspace-saml-setup.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/manage/device-statuses.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/manage/ssh-access.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/manage/filters-tags.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/manage/device-logs.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/manage/configuration.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/manage/actions.md',
    '/Users/vipulgupta2048/work/balena-docs/learn/manage/variables.md',
    '/Users/vipulgupta2048/work/balena-docs/faq/debugging-device-gateway.md',
    '/Users/vipulgupta2048/work/balena-docs/faq/debugging-storage-media.md',
    '/Users/vipulgupta2048/work/balena-docs/faq/troubleshooting/raspberrypi5.md',
    '/Users/vipulgupta2048/work/balena-docs/faq/troubleshooting/test-page.md',
    '/Users/vipulgupta2048/work/balena-docs/faq/troubleshooting/index.md',
    '/Users/vipulgupta2048/work/balena-docs/reference/hardware/versioning.md',
    '/Users/vipulgupta2048/work/balena-docs/reference/hardware/devices.md',
    '/Users/vipulgupta2048/work/balena-docs/reference/hardware/wifi-dongles.md',
    '/Users/vipulgupta2048/work/balena-docs/reference/base-images/overview.md',
    '/Users/vipulgupta2048/work/balena-docs/reference/sdk/python-sdk.md',
    '/Users/vipulgupta2048/work/balena-docs/reference/api/overview.md',
    '/Users/vipulgupta2048/work/balena-docs/reference/OS/overview.md',
    '/Users/vipulgupta2048/work/balena-docs/reference/OS/updates/self-service.md',
    '/Users/vipulgupta2048/work/balena-docs/reference/OS/updates/time-sync.md',
    '/Users/vipulgupta2048/work/balena-docs/reference/supervisor/configuration-list.md',
    '/Users/vipulgupta2048/work/balena-docs/reference/supervisor/device-metrics.md',
]

def title_from_filename(filepath):
    """Generate a title from the filename"""
    basename = os.path.basename(filepath)
    name = basename.replace('.md', '').replace('-', ' ').replace('_', ' ')
    # Special cases
    if name == 'index':
        parent = os.path.basename(os.path.dirname(filepath))
        name = parent.replace('-', ' ').replace('_', ' ')
    return name.title()

def fix_file(filepath):
    """Add H1 heading and remove leading empty lines"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        
        # Remove leading empty lines
        while lines and lines[0].strip() == '':
            lines.pop(0)
        
        # Check if first line is H1
        if not lines or not lines[0].strip().startswith('# '):
            # Generate title from filename
            title = title_from_filename(filepath)
            lines.insert(0, f'# {title}')
            lines.insert(1, '')  # Add blank line after heading
        
        # Write back
        new_content = '\n'.join(lines)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f'Fixed: {filepath}')
        return True
    except Exception as e:
        print(f'Error fixing {filepath}: {e}')
        return False

# Fix all files
fixed_count = 0
for filepath in files_to_fix:
    if os.path.exists(filepath):
        if fix_file(filepath):
            fixed_count += 1

print(f'\nFixed {fixed_count} files')
