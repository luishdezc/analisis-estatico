# -*- coding: utf-8 -*-

"""
Mock up testing examples.
"""
import subprocess
import unittest
from unittest.mock import MagicMock, mock_open, patch

from white_box.mockup_exercises import (
    execute_command,
    fetch_data_from_api,
    perform_action_based_on_time,
    read_data_from_file,
)


class TestFetchDataFromApi(unittest.TestCase):
    """
    Fetch Data From API unittest class.
    """

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api_returns_json(self, mock_get):
        """
        Verifica que fetch_data_from_api retorna el JSON de la respuesta.
        """
        mock_response = MagicMock()
        mock_response.json.return_value = {"key": "value"}
        mock_get.return_value = mock_response

        result = fetch_data_from_api("https://fake-api.com/data")

        mock_get.assert_called_once_with("https://fake-api.com/data", timeout=10)

        self.assertEqual(result, {"key": "value"})


class TestReadDataFromFile(unittest.TestCase):
    """
    Read Data From File unittest class.
    """

    @patch("builtins.open", new_callable=mock_open, read_data="contenido del archivo")
    def test_read_data_from_file_returns_content(self, mock_file):
        """
        Verifica que read_data_from_file retorna el contenido del archivo correctamente.
        """
        result = read_data_from_file("archivo.txt")

        mock_file.assert_called_once_with("archivo.txt", encoding="utf-8")

        self.assertEqual(result, "contenido del archivo")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_data_from_file_raises_file_not_found(self, _mock_file):
        """
        Verifica que read_data_from_file lanza FileNotFoundError si el archivo no existe.
        """
        with self.assertRaises(FileNotFoundError):
            read_data_from_file("archivo_inexistente.txt")


class TestExecuteCommand(unittest.TestCase):
    """
    Execute Command unittest class.
    """

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_returns_stdout(self, mock_run):
        """
        Verifica que execute_command retorna la salida estándar del subproceso.
        """
        mock_result = MagicMock()
        mock_result.stdout = "output del comando"
        mock_run.return_value = mock_result

        result = execute_command(["echo", "hola"])

        mock_run.assert_called_once_with(
            ["echo", "hola"], capture_output=True, check=False, text=True
        )

        self.assertEqual(result, "output del comando")

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_raises_called_process_error(self, mock_run):
        """
        Verifica que execute_command relanza CalledProcessError si subprocess.run lo lanza.
        """
        mock_run.side_effect = subprocess.CalledProcessError(
            returncode=1, cmd=["false"]
        )

        with self.assertRaises(subprocess.CalledProcessError):
            execute_command(["false"])


class TestPerformActionBasedOnTime(unittest.TestCase):
    """
    Perform Action Based On Time unittest class.
    """

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_based_on_time_action_a(self, mock_time):
        """
        Action A.
        """
        mock_time.return_value = 9

        result = perform_action_based_on_time()

        self.assertEqual(result, "Action A")

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_based_on_time_action_b(self, mock_time):
        """
        Action B.
        """
        mock_time.return_value = 11

        result = perform_action_based_on_time()

        self.assertEqual(result, "Action B")
