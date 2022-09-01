# Robot Framework CI

## Overview
- This project implements a GitLab CI for [Robot Framework](https://robotframework.org/).

## Setup
- create project directory
- download and extract [template](https://git.fligno.com/QA/robot-framework/template/robot-framework-pipeline/-/archive/main/robot-framework-pipeline-main.zip) to created project directory
- apply development scripts
- **push** or upload scripts to your project repository

## Structure
    
    ├── actions - constains the all the actions
    │   ├── common-env.robot - needed app url
    │   ├── common-creds.robot -  app credentials
    │   ├── common.robot - reusable components
    │   └── _<module-1>
    │       └── <feature>.robot
    │       └── *.robot
    │   └── _<module-2>
    │       └── <feature>.robot
    │       └── *.robot
    ├── test-cases
    │   └── 1-<suite-name>.robot
    │   └── 2-<suite-name>.robot
    │   └── *-*.robot
    ├── test-data (usage for jsonlibrary)
    │   └── <data-name>.json


 - **test case file formatting**
    ```
    1-<suite-name>.robot
    2-<suite-name>.robot
    3-<suite-name>.robot
    ...
    ```
    - Use numerical sequence to specify which will run first.

## Requirements

- Add `.gitlab-ci.yml` in you project repository.

    ```
    include:
    - project: 'site-reliability/delivery-sre/pylon'
        ref: main
        file: '/.gitlab-ci/templates/robot-framework-pipeline.yml'
    ```

- Add `.gitignore` in you project repository.

    ```
        reports/
        **/reports
    ```


- Enable **CI/CD Runner**
    - go to repository, **Settings > CI/CD**
    - under **Runners > Enable shared runners for this project**

## Stages

**full-pass-test**

Performs a full pass testing that will run all the test suite under the `test-case/` directory

- Usage
    - push changes on `main/master` branch

**regression-test**

Performs a regression testing that will test run a specific suite.

- Usage
    - push a branch named from one of ***.robot** file under the `test-case/` directory
        ```
        git checkout -b 1-<suite-name>
        git push origin 1-<suite-name>
        ```


## Note

- Avoid **[Dialogs](https://robotframework.org/robotframework/latest/libraries/Dialogs.html)** - is Robot Framework's standard library that provides means for pausing the test or task execution and getting input from users.
- `Pause, Wait Until *` - set value to **min 2s - max 5s**
- Run the test suites on both `non-headless` and `headless` mode.

**Re Run a Test**

- go to repository, **CI/CD > Run pipeline**
- select the specific **branch** and click **Run pipeline**

**Non Headless**

    Open Browser   ${url}   chrome

