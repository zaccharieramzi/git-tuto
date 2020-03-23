# Git Tutorial

This repository will help you practice the basics of the GitHub flow and how to work on open source projects.

Here is a link to a presentation to git in general: https://docs.google.com/presentation/d/1vfsG__2-T7xJYGKFs9HfPKmaoMN1Je0V0h7gLyiY1AU/edit?usp=sharing

## Steps
These steps assume that you [have installed git locally](https://www.atlassian.com/fr/git/tutorials/install-git), that you [have created a GitHub account](https://github.com/join), and [have added your local ssh key](https://help.github.com/en/enterprise/2.15/user/articles/adding-a-new-ssh-key-to-your-github-account) to it.

1. Fork this repo, using the fork button in the top right corner.

2. Clone your forked repo locally. `git clone git@github.com:<your-github-handle>/git-tuto.git`

3. Add the original project as a distant repo. `git remote add upstream https://github.com/zaccharieramzi/git-tuto.git`

4. Create a new branch to add your name to the list of people who have participated to the tutorial. `git checkout -b <your-name-or-pseudonym>`

5. Add your name to the `participants.csv` file. `echo '<your-name-or-pseudonym>,\n' >> participants.csv`

6. Stage and commit your changes. `git add participants.csv && git commit -m'Added <your-name-or-pseudonym> to the participants file'`

7. Push your local branch to your distant repo. `git push origin <the-name-of-your-branch>`

8. Open a new Pull Request (PR): https://github.com/zaccharieramzi/git-tuto/compare. You have an example PR [here](https://github.com/zaccharieramzi/git-tuto/pull/1).

9. Iterate with feedback.

10. Once the PR is (squashed and) merged, don't forget to update your local repo (`git checkout master && git pull upstream master`) and your distant repo (`git push origin master`).

## Continuous Integration tutorial

### Overview of Continuous Integration
Once you have understood how the GitHub flow works, you can try to take part in the continuous integration (CI) tutorial.
But first, what is CI?
CI is a process that can be best described as the continuous testing of the code as parts are added to it.
This makes sure that a new addition to the codebase does not alter unexpectedly the behaviour of the code.

Many tools exist but we will here use only Travis CI.
To set it up you just need to register to their website, add your repo to the list of watched repositories, and then add a travis config file to your project.
The travis config file is a [YAML file](.travis.yml) containing a list of instructions on how to run the tests correctly.

### Steps
This assumes you have taken the steps 1-4 of the git tutorial.

1. Add a file <your-name>_function.py to the [functions](ci_tutorial/simple_functions) folder.

2. In this file, write a simple function that can be easily tested.
An example is my [function file](ci_tutorial/simple_functions/zac_function.py).
The function doesn't have to be about numbers but can be about all the built-in data structures python provides.

3. Add a corresponding unit test for this new function.
An example of a corresponding unit test is [mine](ci_tutorial/tests/simple_functions_test/zac_function_test.py).

4. Perform the steps 6-10 of the git-tutorial with the slight exception that you need to have a more suited commit message.

## Contributing

You are free to suggest improvements both on the presentation and on this tutorial using the [Issues of this repo](https://github.com/zaccharieramzi/git-tuto/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc).
A first good contribution might be for example to add the Contributing guidelines.
