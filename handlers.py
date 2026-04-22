def dispatch(event):
    handlers = {
        "PushEvent": handle_push,
        "DeleteEvent": handle_delete,
        "PullRequestEvent": handle_pull_request,
        "IssueCommentEvent": handle_issue_comment,
        "CreateEvent": handle_create_event
    }
    handlers.get(event["type"], default_handler)(event)

def handle_push(event):
    print(f"- Pushed a commit to '{event['repo']['name']}'")

def handle_delete(event):
    print(f"- Deleted branch '{event['payload']['ref']}' within repo '{event['repo']['name']}'")

def handle_pull_request(event):
    pull_type = event['payload']['action']
    head = event['payload']['pull_request']['head']['ref']
    base = event['payload']['pull_request']['base']['ref']
    if pull_type == "opened":
        print(f"- Opened a pull request to merge '{head}' into '{base}' in repo '{event['repo']['name']}'")
    elif pull_type == "merged":
        print(f"- Completed a pull request to merge '{head}' into '{base}' in repo '{event['repo']['name']}'")

def handle_issue_comment(event):
    print(f"- Added a comment to '{event['repo']['name']}'")

def handle_create_event(event):
    print(f"- Created branch '{event['payload']['ref']}' in '{event['repo']['name']}'")

def default_handler(event):
    print(f"Event Type: {event['type']}, Repo: '{event['repo']['name']}")