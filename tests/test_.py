from rateflix.app import app

def test_page_setup():
    #page setup testing as done in TDD development by https://github.com/mjhea0/flaskr-tdd
    tester= app.test_client()
    response = tester.get("/", content_type = "html/text")
    assert response.status_code ==200
    assert response.data == b"Hello, World!"