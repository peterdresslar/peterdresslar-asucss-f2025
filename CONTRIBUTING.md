# Contributing

Note that this repo is turning into a bit of a personal test-bed for GitHub-specific workflows, among other things. While it is not expected that other people will typically contribute, the author will attempt to follow these guidelines with some rigor.

## How to Contribute Issues

* Each issue should have a description at least 2 sentences explaining what the issue is about.
* Please review existing issues before filing a new one.

## How to Contribute Code

We are using a feature branch workflow with a protected main branch. This workflow has a few enforcing rules, but is generally relaxed due to the team of one.

Please work on a feature branch with a name that indicates the issue number you are addressing. Note that if you are working on an issue you should include the name of the issue in the branch you are working with. An excellent way to very quickly start contributing code and other data for an issue is to use the [GitHub Command Line Tool](https://cli.github.com/). If you have it installed, here's what you can do:

```bash
# These commands should all be run from the command line from within the local repo.
#
# You will want to ideally make sure that you are on branch main and that you have no untracked or tracked changes.
gh status

# A list of open issues (unless you add an additional flag to include closed ones). New issues are first.
gh issue list

# Make sure there is not already a branch for this issue (example: #123)
gh issue develop --list 123
# Should say "no linked branches found..."

# Now we can go ahead and run this command to develop on issue #123. 
# A branch will be created on the remote with automatic naming and checked out on your local environment.
gh issue develop 123 --checkout
```

You are ready to code, add, and commit as you prefer. Please note, when you commit: each commit message should be a full sentence describing what the commit changes.

When you are finished with improvements on the branch, you are ready to issue a pull request (PR). While the GitHub website offers a strong user interface for PRs, you can also very rapidly generate one using

```bash
# Create a PR (interactive)
gh pr create
```

If you have any questions, the website listed above can be useful, or you can try `gh pr create --help` for detailed information about options. Note that the interactive mode defaults should generally be fine for PRs in this repo.

## Merging

When your PR is ready to merge, the admin will handle acceptance and merging. **In general, they should usually choose the "Squash and Merge" option.**

- On the Web: Click the arrow next to the "Merge pull request" button and select "Squash and merge".
- cli:  `gh pr merge --squash`.

## More about Branch Rules & Workflow

Added from [https://github.com/peterdresslar/rulesets](https://github.com/peterdresslar/rulesets).

So that we can protect our work from major disruptions, this repository uses the "**Solo-to-Small**" ruleset to enforce the following:

### The "PR First" Policy
Even for solo work or small fixes, **direct commits to the main branch are blocked.**
*   Why? It prevents accidental history rewrites and ensures every change—no matter how small—gets a "self-review" via a Pull Request diff.
*   How to Merge: Open a Pull Request. You do **not** need to wait for an approval or a code review. Once you are happy with your own changes, you can merge immediately.

These rules will automatically be applied, even for solo authors.

### Main Branch Safety.
*   No Force Pushes: The main branch history is immutable.
*   No Deletions: The main branch cannot be deleted.

> If you are collaborating with others, approvals are welcome but not strictly enforced by the software. Please communicate with the team if you want a second pair of eyes before merging. Or, see `README.md` about possibly tweaking the rules.


--

This guide uses information from a lesson module authored by Julia Damerow (@damerow) at Arizona State University, 2026.