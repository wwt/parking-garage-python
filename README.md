# Parking Garage

Thank you for your interest in WWT and for spending your time on this code exercise.
This project has been started, but the requirements defined in the unit tests have not been implemented. Your task is to complete the project by making all tests pass.

## Setup

1. Use [Visual Studio Code](https://code.visualstudio.com/) or the IDE of your choice.
1. Install [Pipenv](https://pipenv.pypa.io/en/latest/) in order to manage dependencies and virtual environment.

    Install Pipenv with pip:

    ```bash
    pip install --user pipenv
    ```

    or with Homebrew:

    ```bash
    brew install pipenv
    ```

1. Create a virtual environment for the project.

    ```bash
    pipenv install
    ```
  
1. Activate the project virtual environment.

    ```bash
    pipenv shell
    ```

1. As needed, install dependencies.

    ```bash
    pipenv install <package>
    ```

## Run Tests

This project uses the [pytest](https://docs.pytest.org/en/stable/usage.html) framework for unit testing. Tests can be executed by running the pytest module.

```bash
pytest
```

The package [pytest-watch](https://github.com/joeyespo/pytest-watch) has been included as an optional convenience. Use the following command to run all tests and have them automatically run again each time you make a change to the app code.

```bash
ptw
```

## The Problem

You will take in a batch of vehicles. Your task is to process these vehicles, according to the constraints below, and either park or reject individual vehicles from the garage. Do this by working through the tests in the ***test*** directory and implement code in the ***src*** directory to make these tests pass.

### Constraints

A parking garage is made up of parking levels. These levels can contain any number of parking spaces.

Parking spaces have the below restrictions on vehicle:

1. Compact parking spaces.
   - Only compact vehicles may park in compact parking spaces.
1. Permit requirements.
    - Parking spaces may have disability, premium, or no permit requirements.
    - Vehicles must possess all permits required by a parking space in order to access the space.

In addition, the parking garage imposes the following prioritization on parking:

1. Vehicles with disability permits must be parked in available disability parking spaces before they may be placed in non-disability parking spaces.
1. Vehicles with premium permits must be parked in available premium parking spaces before they may be placed in non-permitted parking spaces.
1. Vehicles with dual disability and premium permits are prioritized into disability parking spaces before premium parking spaces.
1. Vehicles with premium permits are prioritized for non-permitted parking spaces.
1. Vehicles with dual disability and premium permits are prioritized for premium parking spaces.
1. Compact vehicles must first be parked in available compact parking spaces with respect to the vehicle permits.

## Submitting Results

Please fork this project and implement your solution. Send us a link to your repo, or send us a zip file of your implementation.

Feel free to add dependencies or modify any part of the code base except the tests.

At WWT we value clean, readable code that passes requirements. If you can make it efficient and easy to read, even better!

>***Note:*** If you need to look something up, that's absolutely allowed, but don't copy another solution, or collaborate on this problem with others. Normally we encourage teamwork, but today we want to see what you can do.
