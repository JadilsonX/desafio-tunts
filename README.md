<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->




<!-- TABLE OF CONTENTS -->
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
      </ul>
    </li>  
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



Basic application that reads a spreadsheet in Google Sheets and updates it from
calculations made with the data received.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With
* [[!Python][Python.org]]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This application uses Google Sheets API, therefore, it needs to configure a Google Account Service and get its credentials in order to establish connection to the API.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* pip
  ```sh
  $ pip install -r requirements.txt
  ```

### Installation

1. Create a Googleproject [https://developers.google.com/workspace/guides/get-started](https://developers.google.com/workspace/guides/get-started)
2. Clone the repo
   ```sh
   git clone https://github.com/JadilsonX/desafio-tunts
   ```
3. Install packages
   ```sh
   $ pip install -r requirements.txt
   ```
4. Edit the `.env.example` file and enter your Google Service Account
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


[Python.py]: https://www.python.org/static/img/python-logo.png
[Python-url]: https://www.python.org/ 

