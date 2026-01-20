# CAS 502 Module Three: Git Exercise II

For this assignment I decided to clean up a repository that I have been working on since my graduate school application. It had turned into a bit of a mess when I later used the repository for other uses. So, for this exercise I have begun to get it into better working order.

Please see the `README.md` for more information.

## Discussion

So that the reviewer can experience a "before and after" comparison, I have left a [branch open](https://github.com/peterdresslar/peterdresslar-asucss-f2025/tree/prior-state) called `prior-state`, before which I had been developing in an *ad hoc* fashion, to say the least.

As part of this assignment I spent quite a bit of time on `CONTRIBUTING.md` as well as a base rulesets repository at `peterdresslar/rulesets`. **I would be very interested in feedback on these, as we plan to use them for our final project.**

I am genuinely pleased that I went through this exercise---I put a lot of effort into it, but I also learned quite a bit. I would look forward to discussing some of the details of the project, since the objective of a *robust but friction-free* development workflow for scientific computing is a non-trivial endeavor.

## Commits
**There are 3 well-scoped commits.**

- 3865177 Added the contributors guide to accompany the new rulesets. Re #8
- 28d96b2 Sync pyproject to requirements.txt. Keeping reqirements.txt for unlikely but possible notebook pip users. Bump requirements.txt requests version. Downgrade pinned python version. This should clear #3
- 8653e8c Applies significant reorganization of files. Fixes broken imports caused by reorganization.  Updated readme with Organization. Note: some opportunistic fixes in src/. Re: #3

### More information (optional)

The easiest way to communicate these commits is through pull requests. Following are four pull requests. During my conversion of the repo I implemented the branch ruleset, so the very first commits for this exercise are not covered by pull requests.

Showing 4 of 4 pull requests in peterdresslar/peterdresslar-asucss-f2025 that match your search

| ID  | Title                                                                                | Branch                                              | Created At          |
|-----|--------------------------------------------------------------------------------------|-----------------------------------------------------|---------------------|
| #12 | Updates portfolio by removing dead links. More work will be needed in the future...  | 2-update-the-streamlit-text-with-links-to-projects  | about 9 hours ago   |
| #11 | Updates both links for content and target values. Re: #10.                           | 10-readme-links-are-brokenodd                       | about 10 hours ago  |
| #9  | Added the contributors guide to accompany the new rulesets. Re #8                    | 8-apply-a-ruleset-and-document                      | about 13 hours ago  |
| #6  | Cleans up the README.md file. Opportunistically renames the Streamlit app. Re: #1    | 1-update-the-readmemd-to-mention-the-streamlit-app  | about 18 hours ago  |

## Issues
**There are 3 well-described issues.**

#4  | Update rule110 processing to search binary indexes
- At the moment the rule110 processing in src/ uses an index, which is workable but not maximally elegant (or, possibly, fast). We should be able to upgrade the processing to use a trick based on the ruleʻs name: with the binary encoding of the rule (110 decimal --> 1101110 binary), we have a way to search each neighborhood state encoded at each index of that binary encoding. Employ this method.
#5  | Generate rule110 datasets for tests
- In order to test the validity of a given respondantʻs manual processing of rule110, generate a number of random rule110 datasets and store them in a new data/ folder. Consider generating bundles of 32, 128, and 512 bits, or use your own judgement to vary lengths. The tool that generates the data should be reusable in the future and testable. Tests would be nice to have.
#13 | Add temporary file for assignment
- Add a text file communicating details of what has changed. Don't forget to align with rubric.

### More information (optional)

Showing 9 of 9 issues in peterdresslar/peterdresslar-asucss-f2025 that match your search

| ID  | Title                                               | Labels        | Updated                |
|-----|-----------------------------------------------------|---------------|------------------------|
| #13 | Add temporary file for assignment                   | documentation | about 6 minutes ago    |
| #10 | README links are broken/odd                         | bug           | about 9 hours ago      |
| #8  | Apply a ruleset and document                        | enhancement   | about 12 hours ago     |
| #7  | Add a contributing guide                            | wontfix       | about 12 hours ago     |
| #5  | Generate rule110 datasets for tests                 | enhancement   | about 19 hours ago     |
| #4  | Update rule110 processing to search binary indexes  | enhancement   | about 19 hours ago     |
| #3  | Clean up file organization                          | enhancement   | about 19 hours ago     |
| #2  | Update the Streamlit text with links to projects    | enhancement   | about 8 hours ago      |
| #1  | Update the README.md to mention the Streamlit app   | enhancement   | about 17 hours ago     |

## Description and rationale
**The submission includes a short project description and brief explanation of commits and issues.**

Please see above.

## See also

- Created companion repository (peterdresslar/rulesets) with reusable GitHub ruleset configurations
- Applied a ruleset from that repository to protect the main branch and enforce PR strategy in this repo.
- Added custom descriptive labels to the repository
