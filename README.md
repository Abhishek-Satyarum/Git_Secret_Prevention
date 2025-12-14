<h1><b>🔐 Git Secret Prevention(GSP)</b></h1>

Git Secret Prevention(GSP) is a pre-commit security gate that prevents developers from accidentally pushing API keys, tokens, and passwords to Git repositories.

It works on rule-based detection which is fast and reliable with its regex patterns. 
It has smart decision making program which blocks and warns the user about the API Keys, tokens, private keys etc.

CLI for this tool is fantastic mainly because it fits naturally into how Git and developers already work, while staying fast, simple, and secure. Also it uses Standard Library Modules which are built into Python and available without extra installation. 

<br>

## 😤 Technologies

**BackEnd**: [Python](https://www.python.org/)

Libraries used are:

- [Pathlib](https://docs.python.org/3/library/pathlib.html)
- [PyFiglet](https://pypi.org/project/pyfiglet/)
- [re (RegEx)](https://docs.python.org/3/library/re.html)

**IDEA**: ` Python + Git Hooks + Regex + JSON = Real-time secret leak prevention at commit time `

<br>

## 🤔 Why It Matters?

- Oftenly, Secrets are leaked to public repositories by the developers and they can be exploited within minutes, leading to unauthorized API usage, data breaches, cloud credentials, database passwords and financial loss. Attackers, bots, and automated scanners continuously monitor platforms like [GitHub](https://github.com/) and GitLab for exposed secrets.

- As we know that, [Git](https://git-scm.com/) history is immutable by design: once a secret is pushed, it is stored in every clone and mirror of the repo, backup, and cache, which makes complete removal tedious and error-prone.

- Tools exist to rewrite history, but they are complex, can break forks or integrations, and still may not guarantee that the secret isn’t archived somewhere; in practice, teams often have to revoke and rotate every exposed credential.

- If the repo is public or briefly made public, scanning services and mirrors may already have captured the secret, so even rewriting history cannot “un-leak” it.

<br>

<h1><b>👨‍🏫 Instructions</b></h1>

This hook can be copied into any Git repository in seconds in your system.

→ Steps Required:

1. Open [VS Code](https://code.visualstudio.com/) or System Terminal type ```git clone https://github.com/Abhishek-Satyarum/Git_Secret_Prevention```
2. Then type ```cd Git_Secret_Prevention```
3. And lastly `cp hooks/pre-commit .git/hooks/`
4. After task is completed, its time to commit. Type ` git add .`
5. Then type ` git commit -m "Done" `

<br>

<h1><b>🎯 Solution</b></h1>

- Catching secrets before they enter the repository is the only reliable way to ensure they never appear in history, never replicate to other clones, and never reach external scanners.

- A pre‑commit check becomes a small safety net that runs in milliseconds on the developer’s machine, turning an easy human mistake (copy‑pasting a key during debugging) into a harmless, fixable warning.

- GSP shifts security from reactive firefighting (rotate keys, investigate logs, notify users) to proactive hygiene that quietly protects every commit, every day, with almost no friction.

- Also the scanner supports multiple file types by checking staged file extensions using tuple-based matching. We detect secrets independent of language syntax which means we support any programming language available.

- GSP is **lightweighted, fast, developer-friendly, and integrates directly into existing Git workflows** without requiring cloud services or dashboards.

<br>

<table>
  <tr>
    <td align="center"><b>If Secret is Absent👍 </b></td>
    <td align="center"><b>If Secret is Detected‼️</b></td>
  <tr>
    <td><img src="docs/Success.jpg" width="600"></td>
    <td><img src="docs/block.jpg" width="600"></td>
  </tr>
</table>   

<br>

## 😁 Benefits Of GSP

- It is a secret aware Git workflow that reduces the cognitive load on developers as they dont have to manually remember that "Not to commit this file". This tool enforces it consistently across the team.

- As organisation grows larger, there are more and more repos with confidential contracts, so manual control and code review cannot reliably catch every secret, but automated pre‑commit protection scales linearly without depending on reviewer vigilance.

- Over time, this fosters a secure‑by‑default culture where developers internalize best practices (env vars, secret managers, .gitignore) because the tools repeatedly reinforce the right patterns at the moment they code.

- We deliberately avoid detecting random strings as passwords to prevent false positives. We only flag credentials when they are contextually assigned.

- Also our tool blocks commits when secrets are detected. If a developer intentionally wants to proceed, Git provides a secure override using --no-verify, ensuring accountability.

- GSP scans comments as well, because commented secrets are still leaked in Git history.

<br>

## 🎥 Video 

<br>

![Demo](https://github.com/Abhishek-Satyarum/Git_Secret_Prevention/blob/main/docs/Video%20Proof%20(2).gif)




<h1 align="center"><b>❤️Thank You❤️</b></h1>






