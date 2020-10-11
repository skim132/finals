import pytest
from flask import session
def test_register(client):
    # Check that we retrieve the register page.
    response_code = client.get('/auth/register').status_code
    assert response_code == 200
    response = client.post( '/auth/register',data={'username': 'sean', 'password': 'ddowoo22'})
def test_logout(client, auth):
    auth.login()
    with client:
        auth.logout()
        assert 'user_id' not in session
def test_login_required_to_comment(client):
    response = client.post('/review')
    assert response.headers['Location'] == 'http://localhost/auth/login'
def test_review(client, auth):
    auth.login()
    response = client.get('/review?movie_id=10+years2011')
    response = client.post('/review',data={'review': 'I love this movie', 'Rating': 2})
def test_remove(client, auth):
    auth.login()
    response=client.get('/review?movie_id=10+years2011')
    response=client.delete('/delete_review?movie_id=10+years2011&review_id=10+years2011sean1602406596.350616')