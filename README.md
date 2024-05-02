# Queues with rework

This project is a model of a queue system that allows for rework.
The objective is to create a minimalistic GUI, that allows the user to create queues (following FIFO or LIFO metodologies), with rework (if the client is randomnly not well attended, will be right back at the queue).

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a simulation of a queue system that incorporates the concept of rework. It can be used to study and analyze the performance of queue systems in scenarios where rework is involved.

## Installation

To get started with this project, you can clone it by running the following command:

```sh
 git clone https://github.com/madfp/colas-con-retrabajos.git
```

This project was build using a virtual environment, to ensure the dependencies and the versionings, so, to run the virtual environment:

Create your own virtual environment:

```sh
  python -m virtualenv venv
```

Activate it (on Windows):

```sh
  ./venv/Scripts/activate
```

Install all the dependencies of the project:

```sh
  pip install -r requirements.txt
```

## Usage

To run the project, you can use the following command:

```sh
  python main.py
```

Or using flet:

```sh
  flet run ./src/main.py
```

The project will start and you will see a window with the GUI of the queue system. You can create a simulation by entering the data you want for the queue system parameters, or you can generate a simulation using random data.

## Contributing

If you want to contribute to this project, you can fork it and create a pull request with your changes. I will review it and merge it if it is necessary. If you have any questions, you can contact me by email.
