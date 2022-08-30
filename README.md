# Restaurant - Django Demo

# What is this project? (TBD)

# How to run the project from scratch
1. Create virtual environment:
> python -m venv venv  

2. Activate virtual environment:
> source venv/bin/activate

3. Install project dependencies:
> pip install -r requirements.txt

4. Apply the migrations
> python manage.py migrate
 
5. Run the project on port 8080:
> python manage.py runserver

# Endpoints (TBD)

# Branch patterns
> [type] / [task-id] / [objective_of_the_task]

#### Example:
> docs/RDD-123/create_branch_pattern

# Pull Request patterns
The title of the PR is almost like the commit message pattern:
- **type** of the code modification
- **scope** showing where the modification were done
- **task-id** showing why you're doing this PR
- **objective of the task** summarize the objective of the task 

#### Example:
> [type] (scope): [task-id] [objective of the task]

### ⚠️ Always link the trello task on the PR description and vice versa!!⚠️


# Commit message pattern

A properly formed Git commit message line should always be able to complete the following sentence:
#### Example:
> [type] (scope): [task-id] [message]


## Types
- **fix**: a commit of the type fix patches a bug in your codebase.
- **feat**: a commit of the type feat introduces a new feature to the codebase.
- **BREAKING CHANGE**: a commit that has a footer BREAKING CHANGE:, or appends a "!" after the type/scope, introduces a breaking API change (correlating with MAJOR in Semantic Versioning). A BREAKING CHANGE can be part of commits of any type.
- **chore**: Build process or auxiliary tool changes
- **ci**: CI related changes
- **docs**: Documentation only changes
- **style**: Markup, white-space, formatting, missing semicolons
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **test**: Adding, removing or refactoring tests

## Scope
A scope may be provided to a commit’s type, to provide additional contextual information and is contained within parenthesis, e.g., feat(parser): add the ability to parse arrays.

## Message
The message contains a succinct description of the change:

Use the imperative, present tense: "change" not "changed" nor "changes"
No dot (.) at the end.
#### Example:
> [feat] (products.builders): [RDD-001] create sub-products build method 

## The 7 rules of a great commit message:
1. Use the message to explain what and why vs. how
3. Limit the message to 50 characters
4. Summary in the present tense. Not capitalized.
5. Do not end the message with a period
6. Use the imperative mood in the message

## Reference
- https://dev.to/helderberto/patterns-for-writing-better-git-commit-messages-4ba0
