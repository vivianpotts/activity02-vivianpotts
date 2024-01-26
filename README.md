## Survey

Data Types

## Assigned

Friday, 26 Jan, 2024

## Due

Friday, 26 Jan, 2024

## Project Goals

This assignment invites you to run and observe two Python programs called `compare-variables` and `demonstrate-variable-limitations`. Your source programs are written as scripts, which are program files to be executed using Python interpreter in absence of other dependencies. As you learn a new way to run a Python program, this project offers you the opportunity to ensure that you understand how to (i) understand the representation of float-point variables and (ii) the time and space limitations associated with performing computations with numbers.

## Installations

If you have not yet installed Python, Poetry and GatorGrade, you may find instructions below about how to install this software.

- Install Python. Please see:
  - [Setting Up Python on Windows](https://realpython.com/lessons/python-windows-setup/)
  - [Python 3 Installation and Setup Guide](https://realpython.com/installing-python/)
  - [How to Install Python 3 and Set Up a Local Programming Environment on Windows 10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)
- Install `gatorgrade`
  - First, [install `pipx`](https://pypa.github.io/pipx/installation/)
  - Then, install `gatorgrade` with `pipx install gatorgrade`
- [Install `poetry`](https://python-poetry.org/docs/)
- Install `VSCode` or another editor. See [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)

## Cloning Your Repository

 + Use the link to the project that was given to you in class to _accept_ the assignment and find a link to your personalized project.
 + Once the importing task has completed, click on the created assignment link which will take you to your newly created GitHub repository for this lab.
 + Clone this repository (bearing your name) and work locally with out own installed editor and associated resources.
 + As you are working on your lab, you are to commit and push regularly. The commands are the following.

 ```
git add -A
git commit -m ``Your notes about commit here''
git push
```

After you have pushed your work to your repository, please visit the repository at the GitHub website (you may have to log-in using your browser) to verify that your files were correctly sent.

## Code Survey

If you change into the `source` directory of your GitHub repository, you will see two Python files called `compare-variables.py` and `demonstrate-variable-limitations.py`. You can run the `compare-variables.py` program by typing `python compare-variables.py` in your terminal window. What output does the program produce? Can you explain why it produces this output? The key to understanding this segment of source code is to notice that the conditional logic in lines `1` through `4` use a programmer's decimal approximation of $\frac{1}{3}$ while lines `5` through `8` use the fraction itself.  What does this output tell you about the difference between `.33333` and `(1/3)` in the Python language?

```python linenums="1"
if .33333 + .33333 + .33333 == 1:
    print(".33333 + .33333 + .33333 is equal to 1")
else:
    print(".33333 + .33333 + .33333 is not equal to 1")
if (1/3) + (1/3) + (1/3) == 1:
    print("1/3 + 1/3 + 1/3 is equal 1")
else:
    print("1/3 + 1/3 + 1/3 is not equal 1")
```

The second Python program is called `demonstrate-variable-limitations.py` because it uses the exponentiation operator, written as `**`, to raise different numbers to different powers. As shown on line `1` in the following excerpt from this program, it is feasible to efficiently perform the computation `2**2**8`, written as $2^{2^8}$ using mathematical notation. Line `3` also shows that it is possible to efficiently compute the value of $2^{2^{10}}$ using the Python expression `2**2**10`.

Although not shown in the following source code segment, the `demonstrate-variable-limitations.py` script also has commented-out source code that performs the computation `2**2**100`. If you un-comment this source code and run the program by typing `python floating-point-confusion.py` what does the output tell you about the challenges of efficiently performing exponentiation?

```python linenums="1"
feasible_number = 2**2**8
print(f"The value of a feasible number is {feasible_number}")
another_feasible_number = 2**2**10
print(f"The value of another feasible number is {another_feasible_number}")
```

## Running Checks

Since this project does not use [Poetry](https://python-poetry.org/) to manage project dependencies and virtual environments, it does not support the use of commands like `poetry run task test`. However, You may still check your work using GatorGrade. To implement this testing procedure use the command, `gatorgrade --config config/gatorgrade.yml` which will run GatorGrader to check your work. You may also use the output from running GatorGrader in GitHub Actions.

## Project Reflection

Once you have finished all of the previous technical tasks, you can use a text editor to answer all of the questions in the `writing/reflection.md` file. Since this is a source code survey, you should provide output from running each of the provided Python programs on your own laptop and then explain how the program's source code produced that output. A specific goal for this project is to ensure that you can explain how Python programs should use integer numbers and exponentiation in an efficient and correct fashion.


## Project Deliverables

Your assignment comprises the following:
  + Writing in Markdown: `writing/reflection.md`

 To help you write using Markdown, the following references may be helpful to you.
  + [Markdown Tidbits](https://www.youtube.com/watch?v=s-oSuHFVnR4)
  + [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)


## Project Assessment

The grade that a student receives on this assignment will have the following components.

- **Mastery of Technical Writing [up to 75%]:**: Students will also receive a checkmark grade when the responses to the writing questions presented in the `reflection.md` reveal a proficiency of both writing skills and technical knowledge. To receive a checkmark grade, the submitted writing should have correct spelling, grammar, and punctuation in addition to following the rules of Markdown and providing conceptually and technically accurate answers.

- **Mastery of Technical Knowledge and Skills [up to 25%]**: Students will receive a portion of their assignment grade when their program implementation reveals that they have mastered all of the technical knowledge and skills developed during the completion of this assignment. As a part of this grade, the instructor will assess aspects of the programming including, but not limited to, the completeness and the correctness of the program and the use of effective source code comments.

---

## GatorGrade Checking

You can also use `gatorgrade` to check the baseline requirements of this assignment by running the following command in your terminal:

`gatorgrade --config config/gatorgrade.yml`

If `gatorgrade` shows that all checks pass, you will know that you have met baseline requirements of this project.

## Submission

As you are working, you are to commit and push regularly. The commands are the following.

```bash
git add -A
git commit -m ``Your notes about commit here''
git push
```

After you have pushed your work to your repository, please visit the repository at the GitHub website (you may have to log-in using your browser) to verify that your files were correctly sent.

## Project Assessment

This is a check mark grade.

