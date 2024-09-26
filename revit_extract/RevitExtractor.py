"""
Copyright (C) 2024  chuongmep.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import os
import os.path as op
import olefile
import re
import subprocess
from aps_toolkit import ProDbReaderRevit as prodb


class RevitExtractor:
    def __init__(self, rvt_path):
        self.rvt_path = rvt_path
        self.version = None

    def read_prob_data(self) -> prodb.PropDbReaderRevit:
        """
        Read property data from the extracted SVF file.
        :return:
        """
        resource_path = self.extract_svf("output")
        propdb = prodb.PropDbReaderRevit.read_from_resource(resource_path)
        return propdb

    def extract_svf(self, output_path="output"):
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        rvt_version = RevitExtractor.get_version(self.rvt_path)
        self.version = rvt_version
        if not rvt_version:
            raise Exception("Failed to extract Revit model version.")
        exe_path = fr"C:\Program Files\Autodesk\Revit {rvt_version}\RevitExtractor\RevitExtractor.exe"
        if not os.path.exists(exe_path):
            raise Exception("RevitExtractor.exe not found, please install Revit {rvt_version} in your computer.")
        arguments = [
            output_path,
            self.rvt_path
            # '-LogPath', output_path,
            # '-journalPath', output_path
        ]
        RevitExtractor.process_file(exe_path, arguments)
        resource_path = os.path.join(output_path, "output", "Resource")
        return resource_path

    @staticmethod
    def get_version(rvt_file):
        if not op.exists(rvt_file):
            print(f"File not found: {rvt_file}")
            return None

        if not olefile.isOleFile(rvt_file):
            print(f"File does not appear to be an OLE file: {rvt_file}")
            return None

        with olefile.OleFileIO(rvt_file) as rvt_ole:
            bfi = rvt_ole.openstream("BasicFileInfo")
            file_info = bfi.read().decode("utf-16le", "ignore")
            pattern = re.compile(r"\d{4}")
            match = re.search(pattern, file_info)
            if match:
                return match.group(0)
            else:
                print("No version found in file info.")
                return None

    @staticmethod
    def process_file(exe_path, arguments):
        try:
            result = subprocess.run(
                [exe_path] + arguments,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(f"Error: {result.stderr}")

            if result.returncode != 0:
                print(f"Process exited with errors: {result.stderr}")
            else:
                print("Process completed successfully.")

        except Exception as e:
            print(f"An error occurred: {e}")
