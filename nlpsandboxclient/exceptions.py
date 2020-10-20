"""NLP client exceptions"""
import requests


class NlpError(Exception):
    """Generic exception thrown by the client."""


class ClinicalNoteNotFound(NlpError, requests.exceptions.HTTPError):
    """Clinical note not found"""


class DataNodeServerError(NlpError, requests.exceptions.HTTPError):
    """Server error"""


def _raise_for_status(response):
    """
    Replacement for requests.response.raise_for_status().
    Catches and wraps NLP HTTP errors with appropriate text.
    """
    if response.status_code == 404:
        raise ClinicalNoteNotFound(response.json()['title'], response)
    if response.status_code == 500:
        raise DataNodeServerError(response.json()['title'], response)