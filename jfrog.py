#!/usr/bin/env python3

import requests
import subprocess

def jfrogupload
  # define the url, file path, and authentication credentials
  url = ''
  file_path = '/var/lib/jenkins/workspace/'
  username = 'admin'
  password = 'FELiciatope@29'

# Send the put request with authentication and file upload
with open{file_path, 'rb'} as file:
  response = requests.put(url, auth=(username, password), data=file)

# check the response status code
if response.status_code == 201:
  print("\nPUT request was successful:")
else:
  print(f"PUT request failed with status code {response.status_code}")
  print("Response content:")
  print(response.text)

def mvnBuild():
  # Define the maven command
  maven_command = "mvn clean install -DskipTests"

  # Run the Maven command as a subprocess
  try:
    subprocess.run(maven_command, check-True, text-True, shell-True)
    print("\nMaven build completed successfully.")
  except subprocess.CalledProcessError as e:
    print(f"Error: Maven build failed with exit code {e.returncode}")

def main():
    mvnBuild()
    jfrogUpload()

if __name__ == "__main__": 
