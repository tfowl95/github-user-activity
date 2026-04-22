# GitHub Activity CLI

A lightweight Python CLI tool that fetches and displays recent public activity for any GitHub user using the GitHub Events API. The output is formatted into readable, human-friendly summaries for quick inspection directly from the terminal.

---

## Overview

This program retrieves a user's recent activity from GitHub and categorizes each event (e.g., pushes, pull requests, comments) into concise descriptions.

---

## Concepts Demonstrated

* REST API consumption using `urllib`
* JSON parsing
* Dispatcher pattern for clean event routing

---

## Features

* Fetches recent public activity for a given GitHub username
* Supports multiple event types:

  * Push events
  * Pull requests (opened/merged)
  * Branch creation/deletion
  * Issue comments
* Modular event handling via dispatcher pattern
* Clean, readable terminal output
* Basic argument validation and error handling

---

## Project Structure

```
github-activity.py   # Main CLI entry point and API fetch logic
handlers.py          # Event dispatcher and event-specific handlers
```

---

## Requirements

* Python 3.7+
* Internet connection (to access GitHub API)

---

## Installation

Clone the repository:

```
git clone https://github.com/tfowl95/github-activity-cli.git
cd github-activity-cli
```

(Optional) Make executable (macOS/Linux):

```
chmod +x github-activity.py
```

---

## Usage

Run the script with a GitHub username:

```
python github-activity.py <username>
```

Example:

```
python github-activity.py torvalds
```

---

## Example Output

```
- Pushed a commit to 'repo-name'
- Opened a pull request to merge 'feature-branch' into 'main' in repo 'repo-name'
- Deleted branch 'old-branch' within repo 'repo-name'
- Added a comment to 'repo-name'
- Created branch 'new-feature' in 'repo-name'
```

---

## How It Works

1. The CLI accepts a GitHub username via command-line argument.
2. It sends a request to:

   ```
   https://api.github.com/users/<username>/events
   ```
3. The JSON response is parsed into Python objects.
4. Each event is passed to a dispatcher function.
5. The dispatcher routes the event to a specific handler based on its type.
6. The handler prints a formatted summary of the event.

---

## Error Handling

* Missing username argument
* Too many arguments
* Network/API request failures
* Unknown event types (fallback handler)

---

## Notes

* Only public GitHub activity is accessible via this API
* Output is limited to the most recent events returned by GitHub
* Unhandled event types fall back to a generic display

---

## License

No license specified.
