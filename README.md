[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/sel6/Datawarehouse_change">
  </a>
  <h1 align="center">Data Warehouse Change and Automation</h1>
  <p align="center">
    A fully dockerized ELT pipeline using PostgreSQL, Airflow, DBT, Redash and Superset.
    <br />
    <a href="https://sensordataelt.herokuapp.com/index.html"><strong>Explore the docs »</strong><a>
    <br />
    <br />
    ·
    <a href="https://github.com/sel6/Datawarehouse_change/issues">Report Bug</a>
    ·
    <a href="https://github.com/sel6/Datawarehouse_change/issues">Request Feature</a>
    .
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
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
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)
The objective of this project was to migrate an ELT pipeline developed for the week 11 challenge using(MYSQL, DBT, Apache Airflow, and Redash) to a more scalable and robust ELT pipeline. This was accomplished by changing the two main components, namely the MySQL data warehouse to Postgres and the Redash dashboard to Superset.

### Built With

Tech Stack used in this project
* [PostgreSQL](https://www.postgresql.org/)
* [Apache Airflow](https://jquery.com)
* [dbt](https://laravel.com)
* [Redash](https://laravel.com)
* [Superset](https://superset.apache.org/)



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Make sure you have docker installed on local machine.
* Docker
* DockerCompose
  
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/sel6/Datawarehouse_change
   ```
2. Run
   ```sh
    docker-compose up
   ```
3 Can access and Modefy the default configrations for each tool using the `.env` files.


<!-- USAGE EXAMPLES -->
## Usage

### Adminer: 
Adminer (formerly phpMinAdmin) is a full-featured database management tool written in PHP. Used to access MYSQL and Postgres Databases.
- Postgress:
   ```sh
   Navigate to `http://localhost:5243 in the browser
   use `postgres-dbt` server
   use `dbtdb` database
   use `dbtuser` for username
   use `pssd` for password
   ```
### Airflow: 
  Airflow is used for aurchestration and automation.
   ```sh
   Navigate to `http://localhost:8080/` on the browser
   use `admin` for username
   use `admin` for password
   ```
### DBT:
DBT is used for cleaning and transforming the data in the warehouses. 
- Airflow is used for automation of running and testing dbt models
- navigate to `https://sensordataelt.herokuapp.com/index.html` to access dbt docs

### Superset
- navigate to `localhost:8088` to access Airflow 



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Selam Ayehubirhan - kabodshekinah@gmail.com

Project Link: [https://github.com/sel6/Datawarehouse_change](https://github.com/sel6/Datawarehouse_change)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [10 Academy](https://www.10academy.org/)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/sel6/Datawarehouse_change.svg?style=for-the-badge
[contributors-url]: https://github.com/sel6/Datawarehouse_change/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/sel6/Datawarehouse_change.svg?style=for-the-badge
[forks-url]: https://github.com/sel6/Datawarehouse_change/network/members
[stars-shield]: https://img.shields.io/github/stars/sel6/Datawarehouse_change.svg?style=for-the-badge
[stars-url]: https://github.com/sel6/Datawarehouse_change/stargazers
[issues-shield]: https://img.shields.io/github/issues/sel6/Datawarehouse_change.svg?style=for-the-badge
[issues-url]: https://github.com/sel6/Datawarehouse_change/issues
[license-shield]: https://img.shields.io/github/license/sel6/Datawarehouse_change.svg?style=for-the-badge
[license-url]: https://github.com/sel6/Datawarehouse_change/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/selam-ayehubirhan-42909617a//

