import os

def _get_aws_secret():
    try:
        return os.environ["AWS_SECRET_KEY"]
    except KeyError:
        raise EnvironmentError("AWS_SECRET_KEY not set")

def connect():
    s = _get_aws_secret()
    masked = s[:4] + "*" * max(0, len(s) - 8) + s[-4:] if len(s) > 8 else "*" * len(s)
    print(f"Connecting with: {masked}")
