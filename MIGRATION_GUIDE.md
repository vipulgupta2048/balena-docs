# Migration Guide

This guide tracks the ongoing migration from the Metalsmith-based documentation to Mintlify. Update this file as pages move through the workflow.

## Process Checklist
- Audit the Metalsmith source content listed in `local-repo-converted.txt`.
- Prioritize straightforward pages first; defer complex or automation-heavy content.
- Recreate the content in Mintlify MDX, adopting Mintlify components (callouts, frames, code groups, tabs) where they improve clarity.
- Verify navigation entries in `docs.json` and cross-links after migrating.
- Log progress and blockers here so remaining work is obvious.

## Status Table
| Source Path | Target Path | Complexity | Status | Notes |
| --- | --- | --- | --- | --- |
| docs/pages/faq/troubleshooting.md | faq/troubleshooting/index.mdx | Moderate | Done | Replaced dynamic switcher with curated sections and device-specific callouts. |
| docs/pages/learn/deploy/deploy-with-balena-button.md | learn/deploy/deploy-with-balena-button.mdx | Straightforward | Done | Added Mintlify callouts, frames, and refreshed links. |
| docs/pages/learn/deploy/build-optimization.md | learn/deploy/build-optimization.mdx | Straightforward | Done | Reframed caching tips with Mintlify callouts and examples. |
| docs/pages/learn/deploy/delta.md | learn/deploy/delta.mdx | Straightforward | Done | Documented binary deltas with Info & Note callouts. |
| docs/pages/learn/deploy/offline-updates.md | learn/deploy/offline-updates.mdx | High | Deferred | Relies on download automation & multiple diagrams. |
| docs/pages/learn/develop/cloud-iot-provisioning.md | TBD | High | Deferred | Relies on dynamic templating for multiple cloud providers; needs new architecture. |
| docs/pages/reference/base-images/balena-base-images.md | reference/base-images/overview.mdx | Moderate | Done | Reframed base-image selection guidance, architecture mapping, and maintenance tips. |
| docs/pages/reference/api/overview.md | reference/api/overview.mdx | Moderate | Done | Introduced versioning, authentication, and OData patterns with updated curl examples. |
| docs/pages/reference/diagnostics.md | reference/diagnostics/index.mdx | Moderate | Done | Reworked dashboard diagnostics guide with per-check remediation steps and Mintlify callouts. |
| docs/pages/reference/balena-cli.md | reference/balena-cli/index.mdx | High | Done | Replaced dynamic CLI version switcher with a consolidated overview and links to hosted references. |
| docs/pages/reference/sdk/deprecation-policy.md | reference/sdk/deprecation-policy.mdx | Straightforward | Done | Captured deprecation timeline and recommended upgrade cadence. |
| docs/pages/reference/sdk/node-sdk.md | reference/sdk/node-sdk.mdx | High | Done | Summarized installation, auth, and common workflows with links to generated API docs. |
| docs/pages/reference/sdk/python-sdk.md | reference/sdk/python-sdk.mdx | High | Done | Documented installation patterns, configuration, and core workflows with references to the full API guide. |
| docs/templates/_devices.html | templates/components/devices.mdx | High | Deferred | Metalsmith template; determine Mintlify replacement later. |
| docs/pages/learn/deploy/release-strategy/update-strategies.md | learn/deploy/release-strategy/update-strategies.mdx | Straightforward | Done | Migrated strategy breakdown with table and callouts. |
| docs/pages/learn/deploy/release-strategy/update-locking.md | learn/deploy/release-strategy/update-locking.mdx | Straightforward | Done | Added tables plus code samples for lock acquisition. |
| docs/pages/learn/develop/apps.md | learn/develop/apps.mdx | Straightforward | Done | Refreshed overview with callouts, frames, and CLI examples. |
| docs/pages/learn/develop/blocks.md | learn/develop/blocks.mdx | Straightforward | Done | Converted block workflow with structured sections and versioning notes. |
| docs/pages/learn/develop/hardware.md | learn/develop/hardware/index.mdx | Straightforward | Done | Created Mintlify overview with warning and YAML example. |
| docs/pages/learn/develop/multicontainer.md | learn/develop/multicontainer.mdx | Straightforward | Done | Reworked compose guide with requirement tables and callouts. |
| docs/pages/learn/develop/runtime.md | learn/develop/runtime.mdx | Moderate | Done | Consolidated host, supervisor, network, and storage guidance with updated examples. |
| docs/pages/learn/develop/dockerfile.md | learn/develop/dockerfile.mdx | Straightforward | Done | Summarized Dockerfile usage, templates, and Node package workflows. |
| docs/pages/learn/manage/actions.md | learn/manage/actions.mdx | Moderate | Done | Consolidated device, fleet, and release controls with Mintlify callouts. |
| docs/pages/learn/manage/configuration.md | learn/manage/configuration.mdx | Moderate | Done | Documented fleet and device configuration workflows with updated terminology. |
| docs/pages/learn/manage/device-logs.md | learn/manage/device-logs.mdx | Straightforward | Done | Clarified dashboard logging, persistent journals, and streaming guidance. |
| docs/pages/learn/manage/device-statuses.md | learn/manage/device-statuses.mdx | Moderate | Done | Explained connectivity indicators and Supervisor update states with tables. |
| docs/pages/learn/manage/filters-tags.md | learn/manage/filters-tags.mdx | Straightforward | Done | Combined filtering, saved views, and tagging workflows with screenshots. |
| docs/pages/learn/manage/ssh-access.md | learn/manage/ssh-access.mdx | Moderate | Done | Consolidated web terminal, CLI, tunneling, and key management guidance. |
| docs/pages/learn/manage/variables.md | learn/manage/variables.mdx | Straightforward | Done | Rewrote variable precedence and workflows with scoped guidance. |
| docs/pages/learn/accounts/account.md | learn/accounts/account.mdx | Moderate | Done | Centralized signup, tokens, 2FA, and account deletion guidance. |
| docs/pages/learn/accounts/billing.md | learn/accounts/billing.mdx | Moderate | Done | Documented plan management, credits, dynamic billing, and device freezing. |
| docs/pages/learn/accounts/enterprise-sso.md | learn/accounts/enterprise-sso.mdx | High | Done | Detailed SAML setup, user onboarding, and troubleshooting for enterprise SSO. |
| docs/pages/learn/accounts/fleet-members.md | learn/accounts/fleet-members.mdx | Straightforward | Done | Updated member roles table and invitation workflow. |
| docs/pages/learn/accounts/fleet-types.md | learn/accounts/fleet-types.mdx | Straightforward | Done | Explained legacy fleet types and Microservices conversion steps. |
| docs/pages/learn/accounts/organizations.md | learn/accounts/organizations.mdx | Moderate | Done | Reorganized organization roles, teams, and access management content. |
| docs/pages/learn/accounts/idp-setup/microsoft-entra-saml-setup.md | learn/accounts/idp-setup/microsoft-entra-saml-setup.mdx | Moderate | Done | Step-by-step Entra ID SSO integration with updated wording and callouts. |
| docs/pages/learn/accounts/idp-setup/google-workspace-saml-setup.md | learn/accounts/idp-setup/google-workspace-saml-setup.mdx | Straightforward | Done | Documented Google Workspace SAML setup with clarified identifiers. |

## Deferred Items
- Any page that depends on Metalsmith dynamic variables (`{{$device}}`, `{{import ...}}`) until we define Mintlify data replacements.
- Shell scripts in `docs/tools/` pending content migration; plan build process changes once doc structure settles.

## Next Up
1. Identify similarly structured FAQ pages for batching now that the troubleshooting hub pattern is established.
2. Plan an approach for `learn/deploy/offline-updates.md` and other deferred high-complexity pages (diagram replacements, download automation notes).
