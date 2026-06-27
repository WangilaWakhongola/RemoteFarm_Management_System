"""
api_client.py
A simple HTTP client for interacting with the Remote Farm Management System REST API.
Wraps common endpoints for farms, crops, livestock, and alerts.
"""

import json
import urllib.request
import urllib.error
from typing import Any, Optional


class FarmAPIClient:
    """Lightweight client for the Remote Farm Management System API."""

    def __init__(self, base_url: str = "http://localhost:8000", token: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.token = token

    def _headers(self) -> dict:
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def _request(self, method: str, path: str, data: Optional[dict] = None) -> Any:
        url = f"{self.base_url}{path}"
        body = json.dumps(data).encode() if data else None
        req = urllib.request.Request(url, data=body, headers=self._headers(), method=method)
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                return json.loads(response.read().decode())
        except urllib.error.HTTPError as e:
            print(f"[HTTP {e.code}] {method} {url}: {e.reason}")
            return None
        except urllib.error.URLError as e:
            print(f"[Connection Error] {method} {url}: {e.reason}")
            return None

    # --- Auth ---

    def login(self, username: str, password: str) -> bool:
        """Authenticate and store the JWT token."""
        result = self._request("POST", "/api/auth/login/", {"username": username, "password": password})
        if result and "token" in result:
            self.token = result["token"]
            print(f"[Auth] Logged in as '{username}'.")
            return True
        print("[Auth] Login failed.")
        return False

    # --- Farms ---

    def list_farms(self) -> list:
        """Return a list of all farms."""
        return self._request("GET", "/api/farms/") or []

    def get_farm(self, farm_id: int) -> Optional[dict]:
        """Return details of a specific farm."""
        return self._request("GET", f"/api/farms/{farm_id}/")

    # --- Crops ---

    def list_crops(self, farm_id: Optional[int] = None) -> list:
        """Return crop records, optionally filtered by farm."""
        path = f"/api/crops/?farm={farm_id}" if farm_id else "/api/crops/"
        return self._request("GET", path) or []

    def create_crop(self, farm_id: int, name: str, planted_date: str, expected_harvest: str) -> Optional[dict]:
        """Create a new crop record."""
        payload = {
            "farm": farm_id,
            "name": name,
            "planted_date": planted_date,
            "expected_harvest_date": expected_harvest,
        }
        return self._request("POST", "/api/crops/", payload)

    # --- Livestock ---

    def list_livestock(self, farm_id: Optional[int] = None) -> list:
        """Return livestock records, optionally filtered by farm."""
        path = f"/api/livestock/?farm={farm_id}" if farm_id else "/api/livestock/"
        return self._request("GET", path) or []

    def update_animal_health(self, animal_id: int, health_status: str) -> Optional[dict]:
        """Update the health status of a livestock animal."""
        return self._request("PATCH", f"/api/livestock/{animal_id}/", {"health_status": health_status})

    # --- Alerts ---

    def list_alerts(self, resolved: bool = False) -> list:
        """Return alerts, filtered by resolved status."""
        path = f"/api/alerts/?resolved={str(resolved).lower()}"
        return self._request("GET", path) or []

    def create_alert(self, farm_id: int, message: str, severity: str = "medium") -> Optional[dict]:
        """Create a new alert for a farm."""
        payload = {"farm": farm_id, "message": message, "severity": severity}
        return self._request("POST", "/api/alerts/", payload)

    # --- Analytics ---

    def get_analytics(self, farm_id: int) -> Optional[dict]:
        """Fetch analytics data for a farm."""
        return self._request("GET", f"/api/analytics/?farm={farm_id}")


# --- Demo (dry run, no live server needed) ---
if __name__ == "__main__":
    client = FarmAPIClient(base_url="http://localhost:8000")

    print("=== Remote Farm API Client Demo ===\n")
    print("Attempting login (will fail without a running server — expected in demo):")
    client.login("admin", "password123")

    print("\nAttempting to list farms:")
    farms = client.list_farms()
    if farms:
        for farm in farms:
            print(" ", farm)
    else:
        print("  No farms returned (server not running).")

    print("\nAttempting to create an alert:")
    alert = client.create_alert(farm_id=1, message="Soil moisture critically low in Field B1", severity="high")
    if alert:
        print("  Alert created:", alert)
    else:
        print("  Alert not created (server not running).")

    print("\nDemo complete. Connect to a running backend to use this client for real.")
