import pytest
import subprocess
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 302
    page_output = res.get_data(as_text=True)
    res2 = client.get('/fortune/')
    page_output2 = res.get_data(as_text=True)
    assert page_output == page_output2
    

def test_cowsay(app, client):
    message = 'hello'
    res = client.get("/cowsay/%s/" % message)
    assert res.status_code == 200
    page_output = res.get_data(as_text=True)
    assert message in page_output
    assert '(oo)' in page_output
    errMes = "hello ' hello"
    erres = client.get("/cowsay/%s/" %errMes)
    page_err = erres.get_data(as_text=True)
    assert page_err == 'type valid text'
    

def test_fortune(app, client):
    res = client.get('/fortune/')
    assert res.status_code == 200
    page_output = res.get_data(as_text=True)
    chek = subprocess.run(['fortune'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if len(chek.stderr.decode("utf-8")) != 0:
        assert page_output == 'fail to use fortune'
    else:
        assert '</pre>' in page_output


def test_cowfortune(app, client):
    res = client.get('/cowfortune/')
    assert res.status_code == 200
    page_output = res.get_data(as_text=True)
    chek = subprocess.run(['fortune'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if len(chek.stdout.decode("utf-8")) == 0:
        assert page_output == 'fail to use fortune'
    else:
        assert '</pre>' in page_output
