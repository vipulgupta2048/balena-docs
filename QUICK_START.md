# GitBook Quick Start Guide

## 🚀 Getting Started in 5 Minutes

### Step 1: Create GitBook Space (2 min)

1. Go to [GitBook](https://www.gitbook.com/)
2. Sign in or create account
3. Click **"New Space"**
4. Select **"Import from Git"**

### Step 2: Connect Repository (2 min)

1. Choose your Git provider (GitHub/GitLab)
2. Select `balena-docs` repository
3. Choose branch: `master` (or your preferred branch)
4. Set Project directory: `.` (root)
5. Click **"Import"**

### Step 3: Verify (1 min)

GitBook will automatically:
- ✅ Detect `.gitbook.yaml` configuration
- ✅ Parse `SUMMARY.md` for navigation
- ✅ Import all 59 documentation pages
- ✅ Build your documentation site

**That's it!** Your documentation is now live on GitBook.

---

## 📝 Making Changes

### Edit in Git (Recommended for Developers)

```bash
# 1. Edit any .mdx file
vim learn/welcome/introduction.mdx

# 2. Commit and push
git add .
git commit -m "Update introduction"
git push

# 3. GitBook auto-syncs in ~30 seconds
```

### Edit in GitBook UI (Recommended for Writers)

1. Open your space in GitBook
2. Click **"Edit"** button
3. Make changes in the editor
4. Click **"Merge"** when done
5. GitBook commits back to Git automatically

---

## 📚 Common Tasks

### Add a New Page

1. Create new `.mdx` file:
   ```bash
   touch learn/develop/new-feature.mdx
   ```

2. Add to `SUMMARY.md`:
   ```markdown
   ### DEVELOP
   * [New Feature](learn/develop/new-feature.mdx)
   ```

3. Commit and push

### Move a Page

1. Move the file:
   ```bash
   git mv learn/develop/old.mdx learn/deploy/new.mdx
   ```

2. Update path in `SUMMARY.md`:
   ```markdown
   - * [Page](learn/develop/old.mdx)
   + * [Page](learn/deploy/new.mdx)
   ```

3. Commit and push

### Add a Redirect

Edit `.gitbook.yaml`:
```yaml
redirects:
  old/path/page: new/path/page.mdx
```

---

## 🔍 Need More Help?

- **Full Setup Guide**: [GITBOOK_SETUP.md](GITBOOK_SETUP.md)
- **Migration Details**: [GITBOOK_MIGRATION_SUMMARY.md](GITBOOK_MIGRATION_SUMMARY.md)
- **GitBook Docs**: https://docs.gitbook.com/

---

## ⚡ Pro Tips

1. **Two-way sync**: Edit in Git OR GitBook UI - both work!
2. **Preview changes**: GitBook shows live preview as you edit
3. **Search works**: GitBook indexes everything automatically
4. **Mobile ready**: Documentation is responsive out of the box
5. **Analytics included**: Track page views in GitBook dashboard

---

## 🆘 Troubleshooting

**Changes not showing?**
- Wait 30-60 seconds for sync
- Check Git Sync status in GitBook settings
- Verify you pushed to the correct branch

**Page not in navigation?**
- Check it's listed in `SUMMARY.md`
- Verify file path is correct
- Ensure file exists in repository

**Build error?**
- Check `.gitbook.yaml` syntax
- Verify all paths in `SUMMARY.md` exist
- Look for duplicate page references

---

**Ready to deploy?** Follow Step 1 above to get started! 🎉
