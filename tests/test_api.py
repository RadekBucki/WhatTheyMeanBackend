from io import BytesIO
from unittest.mock import patch

import pytest
from flask import Flask

from backend.app import api
from backend.exceptions.illegal_argument_exception import IllegalArgumentException
from backend.model.analysis import Analysis


@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(api)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_register_file(client):
    with patch('backend.database.database_service.DataBaseService.create_analysis') as mock_create_analysis:
        mock_create_analysis.return_value = 'mocked_uuid'

        mock_file = BytesIO(b"Mocked file content")

        response = client.post('/register/file', data={'file': (mock_file, 'test.txt')})

        assert response.status_code == 200
        assert response.json == {'analysis_uuid': 'mocked_uuid'}
        mock_create_analysis.assert_called_once()


def test_register_file_without_file(client):
    with patch('backend.database.database_service.DataBaseService.create_analysis') as mock_create_analysis:
        mock_create_analysis.return_value = 'mocked_uuid'

        with pytest.raises(IllegalArgumentException) as exc_info:
            client.post('/register/file')

        assert 'No file part' in str(exc_info.value)

        mock_create_analysis.assert_not_called()

def test_register_url(client):
    with patch('backend.database.database_service.DataBaseService.create_analysis') as mock_create_analysis:
        mock_create_analysis.return_value = 'mocked_uuid'

        response = client.post('/register/url', query_string={'url': 'http://example.com'})

        assert response.status_code == 200
        assert response.json == {'analysis_uuid': 'mocked_uuid'}
        mock_create_analysis.assert_called_once()

def test_register_url_without_url(client):
    with patch('backend.database.database_service.DataBaseService.create_analysis') as mock_create_analysis:
        mock_create_analysis.return_value = 'mocked_uuid'

        with pytest.raises(IllegalArgumentException) as exc_info:
            client.post('/register/url')

        assert 'No url part' in str(exc_info.value)

        mock_create_analysis.assert_not_called()


def test_get_analyse(client):
    with patch('backend.database.database_service.DataBaseService.get_analysis_by_uuid') as mock_get_analysis_by_uuid:
        analysis = Analysis()
        mock_get_analysis_by_uuid.return_value = analysis

        response = client.get('/analyse/65566381471b14ac7707cc2e')

        assert response.status_code == 200
        mock_get_analysis_by_uuid.assert_called_once()

def test_get_analyse_list(client):
    with patch('backend.database.database_service.DataBaseService.get_analyses_by_uuids') as mock_get_analyses_by_uuids:
        analysis = Analysis()
        mock_get_analyses_by_uuids.return_value = [analysis]

        response = client.get('/analyse', query_string={'uuids': ['65566381471b14ac7707cc2e']})

        assert response.status_code == 200
        mock_get_analyses_by_uuids.assert_called_once()

if __name__ == '__main__':
    pytest.main()
