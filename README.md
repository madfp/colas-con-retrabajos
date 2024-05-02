# Queues with rework

This project is a model of a queuing system that allows customer rework.
The objective is to create a minimalistic GUI, which allows the user to create queues, with rework (if the customer is randomly not well served, he will return to the queue).

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a simulation of a queuing system that incorporates the concept of rework. It can be used to study and analyze the performance of queuing systems in scenarios involving rework.

## Installation

To get started with this project, you can clone it by running the following command:

```sh
 git clone https://github.com/madfp/colas-con-retrabajos.git
```

This project was built using a virtual environment, to ensure dependencies and versioning, as well as to run the virtual environment:

Create your own virtual environment:

```sh
  python -m virtualenv venv
```

Activate it (on Windows):

```sh
  ./venv/Scripts/activate
```

Install all dependencies:

```sh
  pip install -r requirements.txt
```

## Usage

To run the project, you can use the following commands:

```sh
  python ./src/main.py
```

Or using flet:

```sh
  flet run ./src/main.py
```

The project will start and you will see a window with the queuing system GUI. You can create a simulation by entering the desired data for the queuing system parameters, or you can generate a simulation using random data.

## Contributing

If you want to contribute to this project, you can make a fork and create a pull request with your changes. I will review it and merge it if necessary. If you have any questions, you can contact me by email.
