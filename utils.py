import requests

def validate_url(url: str) -> bool:
    """Check whether a URL is reachable."""
    try:
        response = requests.get(
            url,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        return response.status_code == 200
    except Exception:
        return False
