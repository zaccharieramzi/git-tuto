# Git Tutorial

This repository will help you practice the basics of the GitHub flow and how to work on open source projects.

Here is a link to a presentation to git in general: https://docs.google.com/presentation/d/1vfsG__2-T7xJYGKFs9HfPKmaoMN1Je0V0h7gLyiY1AU/edit?usp=sharing

## Steps
These steps assume that you [have installed git locally](https://www.atlassian.com/fr/git/tutorials/install-git), that you [have created a GitHub account](https://github.com/join), and [have added your local ssh key](https://help.github.com/en/enterprise/2.15/user/articles/adding-a-new-ssh-key-to-your-github-account) to it.

1. Fork this repo, using the fork button in the top right corner.

2. Clone your forked repo locally. `git clone git@github.com:<your-github-handle>/git-tuto.git`

3. Add the original project as a distant repo. `git remote add https://github.com/zaccharieramzi/git-tuto.git`

4. Create a new branch to add your name to the list of people who have participated to the tutorial. `git checkout -b <your-name-or-pseudonym>`

5. Add your name to the `participants.csv` file. `echo '<your-name-or-pseudonym>,\n' >> participants.csv`

6. Push your local branch to your distant repo. `git push origin <the-name-of-your-branch>`

7. Open a new Pull Request (PR): https://github.com/zaccharieramzi/git-tuto/compare

8. Iterate with feedback.

9. Once the PR is (squashed and) merged, don't forget to update your local repo (`git checkout master && git pull upstream master`) and your distant repo (`git push origin master`).
