"""1. Gestiona diferentes tipos de archivos."""

import json
import csv


class JsonDataHandler:
    def load_data(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
        

class CsvDataHandler:
    def load_data(self, file_path):
        with open(file_path, newline='') as file:
            return list(csv.DictReader(file))