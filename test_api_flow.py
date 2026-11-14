from utils.api_client import APIClient

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user_successful():
    # 1. კლიენტის ინიციალიზაცია
    client = APIClient(BASE_URL)
    
    # 2. GET მოთხოვნის გაგზავნა (მაგ: მე-1 იუზერი)
    response = client.get_user(1)
    
    # 3. Assert-ები (შემოწმებები)
    assert response.status_code == 200, f"მოსალოდნელი იყო 200, მივიღეთ: {response.status_code}"
    
    data = response.json()
    assert data["id"] == 1
    assert "username" in data, "პასუხში არ იძებნება 'username' ველი"


def test_create_post_successful():
    client = APIClient(BASE_URL)
    
    # POST მოთხოვნა მონაცემების შესაქმნელად
    response = client.create_post(
        title="Playwright & API Testing", 
        body="Learning full-cycle QA automation in Linux/WSL", 
        user_id=1
    )
    
    # შემოწმება, რომ რესურსი წარმატებით შეიქმნა (REST სტანდარტით არის 201)
    assert response.status_code == 201, f"მოსალოდნელი იყო 201, მივიღეთ: {response.status_code}"
    
    data = response.json()
    assert data["title"] == "Playwright & API Testing"
    assert data["userId"] == 1

    