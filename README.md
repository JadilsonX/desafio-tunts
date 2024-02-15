<a name="readme-top"></a>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
      </ul>
    </li>  
  </ol>
</details>



## About The Project



Basic application using Python and Flask that reads and render a spreadsheet from Google Sheets and updates it from
calculations made with the data received.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With
* [![Python][Python.py]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Getting Started

This application uses Google Sheets API, therefore, it needs to configure a Google Account Service and get its credentials in order to establish connection to the API.

### Prerequisites

To install all required packages run the following command:
* pip
  ```sh
  $ pip install -r requirements.txt
  ```

### Installation

1. Create a Google Cloud project [https://developers.google.com/workspace/guides/get-started](https://developers.google.com/workspace/guides/get-started)
2. Clone the repo
   ```sh
   git clone https://github.com/JadilsonX/desafio-tunts
   ```
3. Install packages
   ```sh
   $ pip install -r requirements.txt
   ```
4.  Rename the `.env.example` file to `.env`,  and enter your Google Service Account crendentials.
   ```js
    TYPE = "service_account"
    PROJECT_ID = "PROJECT_ID"
    PROJECT_ID = "PROJECT_ID"
    PRIVATE_KEY_ID = "KEY_ID"
    PRIVATE_KEY = "-----BEGIN PRIVATE KEY-----\nPRIVATE_KEY\n-----END PRIVATE KEY-----\n"
    CLIENT_EMAIL = "SERVICE_ACCOUNT_EMAIL"
    CLIENT_ID = "CLIENT_ID"
    AUTH_URI = "https://accounts.google.com/o/oauth2/auth"
    TOKEN_URI = "https://accounts.google.com/o/oauth2/token"
    AUTH_PROVIDER_URL = "https://www.googleapis.com/oauth2/v1/certs"
    CLIENT_URL = "https://www.googleapis.com/robot/v1/metadata/x509/SERVICE_ACCOUNT_EMAIL"
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage
To run the application run the following command:
* pip
  ```sh
  $ flask --app main run
  ```


[Python.py]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/ 

