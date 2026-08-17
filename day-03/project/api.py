# api.py
import requests
import json
from typing import Optional, Dict, List
from models import Student

class APIManager:
    """Class untuk handle API dengan requests"""

    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com"):
        self.base_url = base_url
        self.session = requests.Session()

    def get_sample_data(self) -> Optional[List[Dict]]:
        """Ambil sample data dari API"""
        try:
            response = self.session.get(f"{self.base_url}/users")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Error fetching from API: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"⚠️ Error parsing JSON: {e}")
            return None

    def create_student_from_api(self, user_data: Dict) -> Optional[Student]:
        """Buat student dari data API"""
        try:
            # Mapping data API ke format student
            student = Student(
                student_id=f"API{user_data['id']:03d}",
                name=user_data['name'],
                age=20 + (user_data['id'] % 10),  # Random age
                gender="Laki-laki" if user_data['id'] % 2 == 0 else "Perempuan",
                grade=70 + (user_data['id'] % 30),
                major=f"Major {user_data['id'] % 5 + 1}"
            )
            return student
        except KeyError as e:
            print(f"⚠️ Missing key in API data: {e}")
            return None

    def post_data_to_api(self, student: Student) -> bool:
        """Kirim data ke API (simulasi)"""
        try:
            data = student.to_dict()
            response = self.session.post(
                f"{self.base_url}/posts",
                json=data,
                headers={'Content-Type': 'application/json'}
            )
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Error posting to API: {e}")
            return False

    def get_public_apis(self) -> List[Dict]:
        """Dapatkan list public APIs (demo)"""
        try:
            response = self.session.get("https://api.publicapis.org/entries")
            response.raise_for_status()
            data = response.json()
            return data.get('entries', [])[:5]  # Ambil 5 sample
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Error fetching public APIs: {e}")
            return []
