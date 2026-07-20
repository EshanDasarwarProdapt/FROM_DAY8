from fastapi.testclient import TestClient
from app.main import app, home

client = TestClient(app)


def test_home_returns_expected_payload():
    response = home()

    assert response["Model"]["title"] == "Python Dev"
    assert response["Model"]["company"] == "ABC Technologies"
    assert response["Schema"]["salary"] == 750000.0


def test_create_and_get_job():
    # 1. Create a job
    job_data = {
        "title": "Software Engineer",
        "description": "Develop high-quality software",
        "salary": 95000.0,
        "company": "Tech Corp"
    }
    response = client.post("/jobs", json=job_data)
    assert response.status_code == 201
    created_job = response.json()
    assert created_job["title"] == job_data["title"]
    assert created_job["company"] == job_data["company"]
    assert "id" in created_job
    job_id = created_job["id"]

    # 2. Get the specific job
    response = client.get(f"/jobs/{job_id}")
    assert response.status_code == 200
    fetched_job = response.json()
    assert fetched_job["title"] == job_data["title"]
    assert fetched_job["id"] == job_id

    # 3. Get all jobs
    response = client.get("/jobs")
    assert response.status_code == 200
    all_jobs = response.json()
    assert len(all_jobs) >= 1
    assert any(j["id"] == job_id for j in all_jobs)

    # 4. Update the job
    updated_data = {
        "title": "Senior Software Engineer",
        "salary": 110000.0
    }
    response = client.put(f"/jobs/{job_id}", json=updated_data)
    assert response.status_code == 200
    updated_job = response.json()
    assert updated_job["title"] == "Senior Software Engineer"
    assert updated_job["salary"] == 110000.0
    assert updated_job["company"] == "Tech Corp"  # should remain unchanged

    # 5. Delete the job
    response = client.delete(f"/jobs/{job_id}")
    assert response.status_code == 204

    # 6. Verify job is deleted
    response = client.get(f"/jobs/{job_id}")
    assert response.status_code == 404
