<h1><b>Git Secret Prevention(GSP)</b></h1>

Git Secret Prevention(GSP) is a pre-commit security gate that prevents developers from accidentally pushing API keys, tokens, and passwords to Git repositories.

It works on rule-based detection which is fast and reliable with its regex patterns. 
It has smart decision making program which blocks and warns the user about the API Keys, tokens, private keys etc.

## Why It Matters?

- Oftenly, Secrets leaks to public repositories by the developers and they can be exploited within minutes, leading to unauthorized API usage, data breaches, cloud credentials, database passwords and financial loss. Attackers, bots, and automated scanners continuously monitor platforms like GitHub and GitLab for exposed secrets.

- As we know that, Git history is immutable by design: once a secret is pushed, it is stored in every clone and mirror of the repo, backup, and cache, which makes complete removal tedious and error-prone.

- Tools exist to rewrite history, but they are complex, can break forks or integrations, and still may not guarantee that the secret isn’t archived somewhere; in practice, teams often have to revoke and rotate every exposed credential.

- If the repo is public or briefly made public, scanning services and mirrors may already have captured the secret, so even rewriting history cannot “un-leak” it.

## Solution

