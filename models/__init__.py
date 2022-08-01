#!/usr/bin/python3
"""reloads FileStorage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
