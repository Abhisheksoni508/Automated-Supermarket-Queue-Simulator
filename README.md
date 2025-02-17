# Automated Supermarket Queue Simulator

The Automated Supermarket Queue Simulator is a Python-based simulation tool designed to manage and optimize supermarket checkout lanes. It simulates customer behavior and lane management to ensure efficient processing of customers in both regular and self-checkout lanes.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Authors](#authors)
- [License](#license)

## Introduction

This project is divided into three main parts:
- **Part A**: Manages lanes, adds/removes customers, and displays lane status.
- **Part B**: Generates random customers and items, calculates checkout time, and integrates with Part A.
- **Part C**: Combines Part A and Part B to run the entire simulation for a specified duration.

## Features

- Simulates customer behavior in a supermarket.
- Manages multiple checkout lanes (regular and self-checkout).
- Generates random customers and items in their baskets.
- Calculates checkout times and manages lane queues.
- Prints detailed lane status and customer details.
- Reports lane saturation when the number of customers exceeds a threshold.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Abhisheksoni508/Automated-Supermarket-Queue-Simulator.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Automated-Supermarket-Queue-Simulator
    ```
3. Install the required dependencies (if any). This project does not have external dependencies, but ensure you have Python installed.

## Usage

To run the simulation, execute the `main.py` file:
```sh
python main.py
```

The simulation will run for a default duration of 600 seconds (10 minutes). Adjust the `cfg_simulation_duration` variable in `main.py` to change the simulation duration.

## File Descriptions

### `main.py`
This file combines Parts A and B to run the entire simulation. It initializes the lane and customer classes, manages timers, and controls the simulation's main loop.

### `f1.py`
Manages lanes and customers:
- **LaneResult**: Prints lane status and customer details.
- **LaneManagement**: Manages lane operations such as adding/removing customers, opening/closing lanes, and moving customers between lanes.

### `f2.py`
Generates random customers and items:
- **CustomerDetail**: Processes customer data and prints basket details.
- **CustomerLayout**: Integrates with `LaneManagement` to manage customer queues and checkout times.

## Authors

- Shiyon Suresh
- Abhishek Soni

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
