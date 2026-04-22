def dispatch(event):
    handlers = {
        "PushEvent": handle_push_event
    }
    handlers.get(event["type"], default_handler)(event)

def handle_push_event(event):
    print(f"- Pushed a commit to {event['repo']['name']}")

def default_handler(event):
    print("in default")