# restaurant_demo

# Oque é o repo

# Como rodar o repo
Criar virtual environment:
> python -m venv venv  

Ativar virtual environment:
> source venv/bin/activate

Instalar dependencias do projeto:
> pip install -r requirements.txt

Rodar o projeto:
> python manage.py runserver

# Funcionalidades e endpoints

# Commit message patterns

A properly formed Git commit subject line should always be able to complete the following sentence:
#### Example:
> [type] (scope): [subject]


## Types
- **fix**: a commit of the type fix patches a bug in your codebase.
- **feat**: a commit of the type feat introduces a new feature to the codebase.
- **BREAKING CHANGE**: a commit that has a footer BREAKING CHANGE:, or appends a ! after the type/scope, introduces a breaking API change (correlating with MAJOR in Semantic Versioning). A BREAKING CHANGE can be part of commits of any type.
- **chore**: Build process or auxiliary tool changes
- **ci**: CI related changes
- **docs**: Documentation only changes
- **style**: Markup, white-space, formatting, missing semi-colons
- **refactor**: A code change that neither fixes a bug or adds a feature
- **test**: Adding, removing or refactoring tests

## Scope
A scope may be provided to a commit’s type, to provide additional contextual information and is contained within parenthesis, e.g., feat(parser): add the ability to parse arrays.

## Subject
The subject contains a succinct description of the change:

Use the imperative, present tense: "change" not "changed" nor "changes"
No dot (.) at the end.

## The 7 rules of a great commit message:
1. Use the body to explain what and why vs. how
2. Separate subject from the body with a blank line
3. Limit the subject line to 50 characters
4. Summary in the present tense. Not capitalized.
5. Do not end the subject line with a period
6. Use the imperative mood in the subject line
7. Wrap the body at 72 characters

## Reference
- https://dev.to/helderberto/patterns-for-writing-better-git-commit-messages-4ba0
