# Prompt: publish the showcase

Paste everything below the line into Claude Code (or another CLI agent), started in your local clone (`~/workdir/guided-coding-workshop`). It merges this branch into `main`, publishes the dashboard on GitHub Pages, checks the live site, and removes the GitHub branches you no longer need. It asks you before deleting anything.

---

You are publishing the Weather Dashboard showcase of the repo `Delta-43/guided-coding-workshop` as a permanent live site on GitHub Pages. Work in the local clone in the current directory. Report briefly after each step and stop to ask me if anything doesn't match what's described here.

## Context

- Remotes: `origin` = GitHub (public, SSH). `gitea` = my Gitea at `https://gitea.dchaudhury.com/delta-43/guided-coding-workshop.git` (backup + instructor kit).
- Branches: `main` (GitHub and Gitea), `showcase` (GitHub only: adds `output/index.html`, `output/README.md`, this `output/PUBLISH.md`, `.github/workflows/pages.yml`, and a README link), `ready` (**Gitea only**, the instructor kit).
- `output/index.html` is fully static: it calls Open-Meteo and the AWS terrain tiles from the browser. `.github/workflows/pages.yml` deploys it to Pages on pushes to `main`.
- Live URL: `https://delta-43.github.io/guided-coding-workshop/`

## Rules

- **Never push `ready` to GitHub, and never delete or rewrite anything on Gitea.** Only GitHub branches get cleaned up.
- Commit as `Delta_43 <Delta-43@users.noreply.github.com>` (GitHub rejects my private email). Check `git config user.email` first.
- No force-pushes, no history rewriting. Show me the list and **ask before deleting any branch**.
- Use `gh` for GitHub API calls. Check `gh auth status` first; if it isn't logged in, ask me to run `gh auth login`.

## Steps

1. **Pre-flight.** `git status` must be clean (if not, stop and show me). Run `git fetch origin` and `git fetch gitea`. List the branches on both remotes (`git ls-remote --heads origin` / `gitea`). Confirm that `origin/showcase` exists and is ahead of `origin/main`.

2. **Test locally.** Check out `origin/showcase` (detached is fine) and serve `output/` with `python3 -m http.server 8030`. Confirm `http://localhost:8030/?city=Paris` returns 200 and contains `Weather Dashboard`. If you can drive a headless browser, also check that a weather card and 7 day tiles render. Stop the server.

3. **Merge.** `git switch main && git pull --ff-only origin main`, then `git merge --no-ff origin/showcase -m "Merge showcase: static Weather Dashboard on GitHub Pages"`. Afterwards `output/index.html` and `.github/workflows/pages.yml` exist on `main`. On conflicts: stop and show me.

4. **Enable Pages (before pushing, so the first run can deploy).**
   `gh api -X POST repos/Delta-43/guided-coding-workshop/pages -f build_type=workflow`
   If it answers that Pages already exists (409), run the same call with `-X PUT` instead. Check with `gh api repos/Delta-43/guided-coding-workshop/pages --jq '{status, html_url, build_type}'`: `build_type` must be `workflow`.

5. **Push.** `git push origin main`, then `git push gitea main`. Then bring the kit up to date: `git switch ready && git pull && git merge main && git push gitea ready`, then `git switch main`. If Gitea asks for credentials: username `delta-43`, and the password is my Gitea token. Ask me for it; don't guess.

6. **Watch the deploy.** Find the "Publish showcase to GitHub Pages" run (`gh run list --workflow pages.yml --limit 1`) and wait for it (`gh run watch <id> --exit-status`). If it didn't start, trigger it with `gh workflow run pages.yml --ref main`. If it fails, show me the failing step's log (`gh run view <id> --log-failed`).

7. **Verify the live site.** Retry for up to 5 minutes (Pages can take a moment): `https://delta-43.github.io/guided-coding-workshop/` and `…/?city=Innsbruck` must return 200 and contain `Weather Dashboard`. Also check that the repo README's showcase link points to that URL.

8. **Clean up GitHub branches.** List every branch on `origin` except `main` (expected: just `showcase`). Show me the list and ask for confirmation. Then delete each with `git push origin --delete <branch>`, run `git fetch --prune origin`, and delete the local `showcase` branch if there is one (`git branch -d showcase`). **Don't touch `ready`**, locally or on Gitea.

9. **Report.** The live URL; the merge commit; the Pages workflow result; branches now on GitHub (should be only `main`) and on Gitea (`main` + `ready`).
