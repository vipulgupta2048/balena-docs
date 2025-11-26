# GitBook Deployment Checklist

Use this checklist to ensure a smooth deployment of the migrated documentation to GitBook.

## Pre-Deployment Checklist

### Repository Verification
- [x] `.gitbook.yaml` configuration file exists
- [x] `SUMMARY.md` table of contents exists
- [x] `README.md` serves as introduction
- [x] All 59 pages verified to exist
- [x] Mintlify configuration removed (`docs.json`)
- [x] Frontmatter cleaned in all MDX files
- [x] Package.json updated (Mintlify deps removed)

### Documentation Review
- [ ] Review README.md content
- [ ] Verify SUMMARY.md structure is correct
- [ ] Check that all page titles are appropriate
- [ ] Ensure internal links are working
- [ ] Verify images are accessible

## GitBook Setup Checklist

### Account & Space Setup
- [ ] GitBook account created
- [ ] Organization created (if needed)
- [ ] New space created
- [ ] Space name chosen (e.g., "balena Documentation")

### Git Sync Configuration
- [ ] Git provider connected (GitHub/GitLab)
- [ ] Repository selected: `balena-docs`
- [ ] Branch configured: `master` (or preferred branch)
- [ ] Project directory set to: `.` (root)
- [ ] Initial import completed successfully

### Post-Import Verification
- [ ] All 59 pages imported
- [ ] Navigation structure matches SUMMARY.md
- [ ] README.md appears as introduction
- [ ] Search functionality works
- [ ] All sections visible (Learn, FAQ, Reference)

## Configuration Checklist

### Basic Settings
- [ ] Space visibility set (Public/Private)
- [ ] Space description added
- [ ] Space icon/logo uploaded (if desired)
- [ ] Default branch configured

### Advanced Settings
- [ ] Git Sync direction configured (Two-way recommended)
- [ ] Sync frequency set (Automatic recommended)
- [ ] Merge strategy configured

### Custom Domain (Optional)
- [ ] Custom domain decided
- [ ] Domain added in GitBook settings
- [ ] DNS records configured (CNAME)
- [ ] SSL certificate verified (automatic)
- [ ] Domain verified and active

## Integration Checklist (Optional)

### Analytics
- [ ] GitBook analytics reviewed
- [ ] Google Analytics integrated (if needed)
- [ ] Tracking goals configured

### Communication
- [ ] Slack integration configured (if needed)
- [ ] Notification channels set up
- [ ] Team members notified

### Support
- [ ] Intercom integration (if needed)
- [ ] Support widget configured
- [ ] Help articles linked

## Content Review Checklist

### Page-by-Page Review
- [ ] Learn → Welcome (4 pages)
- [ ] Learn → Accounts (9 pages)
- [ ] Learn → Getting Started (1 page)
- [ ] Learn → Develop (7 pages)
- [ ] Learn → Deploy (7 pages)
- [ ] Learn → Manage (7 pages)
- [ ] Learn → Masterclasses (7 pages)
- [ ] FAQ → Questions (1 page)
- [ ] FAQ → Troubleshooting (2 pages)
- [ ] FAQ → Device Gateway (1 page)
- [ ] FAQ → Storage Media (1 page)
- [ ] Reference → Hardware (2 pages)
- [ ] Reference → API (1 page)
- [ ] Reference → Host OS (2 pages)
- [ ] Reference → Base Images (1 page)
- [ ] Reference → Supervisor (1 page)
- [ ] Reference → Diagnostics (1 page)
- [ ] Reference → SDKs (3 pages)
- [ ] Reference → CLI (1 page)

### Content Quality
- [ ] All code blocks render correctly
- [ ] All images display properly
- [ ] All tables format correctly
- [ ] All links work (internal and external)
- [ ] All headings render properly
- [ ] All lists display correctly

## Testing Checklist

### Functionality Testing
- [ ] Search returns relevant results
- [ ] Navigation works on all levels
- [ ] Breadcrumbs display correctly
- [ ] Page transitions smooth
- [ ] Table of contents (TOC) works

### Cross-Browser Testing
- [ ] Chrome/Edge
- [ ] Firefox
- [ ] Safari
- [ ] Mobile browsers

### Responsive Testing
- [ ] Desktop (1920x1080)
- [ ] Laptop (1366x768)
- [ ] Tablet (768x1024)
- [ ] Mobile (375x667)

### Performance Testing
- [ ] Page load times acceptable
- [ ] Search response time good
- [ ] Images load properly
- [ ] No broken resources

## Migration Cleanup Checklist

### Repository Cleanup
- [ ] Remove Mintlify CLI from CI/CD (if applicable)
- [ ] Update deployment workflows (if needed)
- [ ] Archive old deployment configs
- [ ] Update repository README (if needed)

### Documentation Updates
- [ ] Update links to docs in main website
- [ ] Update links in other repositories
- [ ] Update links in blog posts
- [ ] Update links in support docs
- [ ] Update links in marketing materials

### Team Communication
- [ ] Notify team of new documentation URL
- [ ] Share GitBook access with team members
- [ ] Provide training on GitBook editing (if needed)
- [ ] Update documentation contribution guide

## Post-Deployment Checklist

### Monitoring
- [ ] Set up uptime monitoring
- [ ] Monitor sync status daily (first week)
- [ ] Review analytics weekly
- [ ] Check for broken links weekly

### Maintenance
- [ ] Schedule regular content reviews
- [ ] Plan for version management (if needed)
- [ ] Set up backup strategy
- [ ] Document maintenance procedures

### Optimization
- [ ] Review search analytics
- [ ] Optimize popular pages
- [ ] Add missing content based on searches
- [ ] Improve navigation based on usage

## Rollback Plan (Just in Case)

If issues arise, you can rollback:

1. **Keep Mintlify backup** (optional):
   ```bash
   git checkout -b mintlify-backup
   git revert <migration-commit>
   ```

2. **GitBook issues**:
   - Disable Git Sync temporarily
   - Fix issues in repository
   - Re-enable sync

3. **Critical issues**:
   - Contact GitBook support
   - Use GitBook's export feature
   - Deploy static HTML as fallback

## Sign-Off

### Technical Review
- [ ] Developer review completed
- [ ] QA testing completed
- [ ] Security review completed (if required)

### Content Review
- [ ] Technical writer review completed
- [ ] Product manager approval
- [ ] Stakeholder approval

### Deployment Approval
- [ ] All checklist items completed
- [ ] No blocking issues identified
- [ ] Team notified of go-live
- [ ] Deployment scheduled

**Deployment Date**: _______________  
**Deployed By**: _______________  
**Verified By**: _______________

---

## Quick Reference

- **Setup Guide**: [QUICK_START.md](QUICK_START.md)
- **Full Documentation**: [GITBOOK_SETUP.md](GITBOOK_SETUP.md)
- **Migration Summary**: [GITBOOK_MIGRATION_SUMMARY.md](GITBOOK_MIGRATION_SUMMARY.md)
- **GitBook Support**: https://www.gitbook.com/support

---

**Status**: Ready for deployment ✅  
**Last Updated**: November 26, 2024
