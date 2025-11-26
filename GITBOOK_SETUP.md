# GitBook Setup Guide

This repository has been migrated from Mintlify to GitBook. This guide explains the setup and how to work with GitBook.

## What Changed

### Files Added
- `.gitbook.yaml` - GitBook configuration file
- `SUMMARY.md` - Table of contents structure
- `README.md` - Updated to serve as the GitBook introduction page
- `GITBOOK_SETUP.md` - This setup guide

### Files Removed
- `docs.json` - Mintlify configuration (no longer needed)
- Mintlify-specific frontmatter from all `.mdx` files (kept only `title` field)
- Mintlify CLI dependencies from `package.json`

### Files Modified
- All `.mdx` files - Simplified frontmatter to only include `title` (GitBook compatible)
- `package.json` - Removed Mintlify dependencies, updated description
- `README.md` - Rewritten as GitBook introduction

## GitBook Configuration

### .gitbook.yaml

The `.gitbook.yaml` file tells GitBook how to parse the repository:

```yaml
root: ./

structure:
  readme: README.md
  summary: SUMMARY.md

redirects:
```

**Key settings:**
- `root: ./` - Documentation files are at the repository root
- `structure.readme` - Points to the introduction page
- `structure.summary` - Points to the table of contents
- `redirects` - Can be used to redirect old URLs to new ones

### SUMMARY.md

The `SUMMARY.md` file defines the documentation structure and navigation. It uses a simple markdown list format:

```markdown
# Summary

## Section Name

### Group Name

* [Page Title](path/to/page.mdx)
  * [Child Page](path/to/child.mdx)
```

**Important notes:**
- Use `##` for top-level sections (Learn, FAQ, Reference)
- Use `###` for groups within sections
- Use `*` for pages and nested `*` for child pages
- All paths are relative to the repository root
- Each page can only appear once in the structure

## Setting Up GitBook Sync

### 1. Create a GitBook Account

1. Go to [GitBook](https://www.gitbook.com/)
2. Sign up or log in
3. Create a new organization (if needed)

### 2. Create a Space

1. In GitBook, click "New Space"
2. Choose "Import from Git"
3. Select your Git provider (GitHub, GitLab, etc.)

### 3. Configure Git Sync

1. Select this repository
2. Choose the branch to sync (typically `master` or `main`)
3. Set the "Project directory" to `.` (root)
4. GitBook will automatically detect the `.gitbook.yaml` configuration

### 4. Initial Sync

GitBook will:
- Read the `.gitbook.yaml` configuration
- Parse the `SUMMARY.md` file to build the navigation
- Import all referenced `.mdx` files
- Create the documentation site

## Working with GitBook

### Making Changes

**Option 1: Edit in Git (Recommended for developers)**
1. Make changes to `.mdx` files in your repository
2. Commit and push to the configured branch
3. GitBook automatically syncs and updates the documentation

**Option 2: Edit in GitBook UI**
1. Make changes in the GitBook editor
2. GitBook commits changes back to your repository
3. Changes appear in Git as commits from GitBook

### Adding New Pages

1. Create a new `.mdx` file in the appropriate directory
2. Add the page to `SUMMARY.md` in the correct location
3. Commit and push changes
4. GitBook will automatically include the new page

### Reorganizing Content

1. Edit `SUMMARY.md` to change the navigation structure
2. Move/rename files as needed
3. Update paths in `SUMMARY.md` to match
4. Commit and push changes

### Adding Redirects

If you need to redirect old URLs to new locations, add them to `.gitbook.yaml`:

```yaml
redirects:
  old/path/page: new/path/page.mdx
  another/old/path: another/new/path.mdx
```

**Important:** Don't include leading slashes in redirect paths.

## File Format

### MDX Files

GitBook supports standard Markdown and MDX. The frontmatter has been simplified:

```markdown
---
title: "Page Title"
---

# Page Heading

Content goes here...
```

**Supported frontmatter:**
- `title` - Page title (optional, can also use H1 heading)

**Markdown features:**
- Standard Markdown syntax
- Code blocks with syntax highlighting
- Tables
- Images
- Links (internal and external)
- Lists (ordered and unordered)

### Images

Images should be placed in appropriate directories and referenced with relative paths:

```markdown
![Alt text](../path/to/image.png)
```

## GitBook Features

### MCP Server (Model Context Protocol)

<cite index="21-12,21-13">Every published GitBook site automatically includes a Model Context Protocol (MCP) server that allows AI assistants to access your documentation content directly</cite>, making it easy for tools like Claude Desktop, Cursor, and VS Code extensions to answer questions using your docs.

**How it works:**
- <cite index="21-14,21-15">The MCP server is available at your site's URL with /~gitbook/mcp appended</cite>
- Example: If your docs are at `https://docs.balena.io`, the MCP server is at `https://docs.balena.io/~gitbook/mcp`
- Users can add this URL to their AI tools to access your documentation

**Enable MCP Server:**
1. Go to your site's Customization > Configure menu
2. Under "Page actions", enable the MCP server option
3. Users will see a "Copy MCP URL" option in the page actions menu

**Benefits:**
- AI assistants can answer questions using your documentation
- Developers can access docs directly in their IDE
- No additional setup required - automatically generated

### Search

GitBook provides built-in full-text search across all documentation.

### Versioning

GitBook supports multiple versions by syncing different branches:
1. Create a new branch for each version
2. Set up Git Sync for each branch
3. GitBook creates separate spaces for each version

### Custom Domain

You can configure a custom domain in GitBook:
1. Go to Space Settings → Domain
2. Add your custom domain
3. Configure DNS records as instructed
4. GitBook will handle SSL certificates

### Analytics

GitBook provides built-in analytics:
- Page views
- Search queries
- User engagement
- Popular pages

### Integrations

GitBook supports various integrations:
- Slack - Notifications and search
- Intercom - Customer support
- Google Analytics - Advanced analytics
- GitHub/GitLab - Enhanced Git sync

## Troubleshooting

### Sync Issues

**Problem:** Changes not appearing in GitBook
- Check that you pushed to the correct branch
- Verify the branch is configured in Git Sync settings
- Check GitBook sync status in Space Settings

**Problem:** Pages not showing in navigation
- Verify the page is listed in `SUMMARY.md`
- Check that the file path is correct
- Ensure the file exists in the repository

### Build Errors

**Problem:** GitBook shows sync errors
- Check `.gitbook.yaml` syntax
- Verify all paths in `SUMMARY.md` are correct
- Ensure all referenced files exist
- Check for duplicate page references

### Formatting Issues

**Problem:** Content not rendering correctly
- Verify MDX syntax is valid
- Check for unclosed code blocks
- Ensure images paths are correct
- Validate markdown table syntax

## Migration Notes

### From Mintlify

This repository was migrated from Mintlify. Key differences:

**Mintlify → GitBook:**
- `docs.json` → `.gitbook.yaml` + `SUMMARY.md`
- Rich frontmatter → Simplified frontmatter (title only)
- Mintlify components → Standard Markdown
- Automatic navigation → Explicit `SUMMARY.md` structure

### Content Structure

The navigation structure has been preserved:
- Learn section with subsections (Welcome, Accounts, Develop, Deploy, Manage, Masterclasses)
- FAQ section with troubleshooting guides
- Reference section with API, SDK, CLI, and hardware documentation

All 59 documentation pages have been successfully migrated and verified.

## Additional Resources

- [GitBook Documentation](https://docs.gitbook.com/)
- [Git Sync Guide](https://docs.gitbook.com/getting-started/git-sync)
- [Content Configuration](https://docs.gitbook.com/getting-started/git-sync/content-configuration)
- [Markdown Guide](https://docs.gitbook.com/creating-content/formatting)

## Support

For GitBook-specific issues:
- [GitBook Support](https://www.gitbook.com/support)
- [GitBook Community](https://github.com/GitbookIO/community)

For balena documentation issues:
- Create an issue in this repository
- Contact the documentation team
