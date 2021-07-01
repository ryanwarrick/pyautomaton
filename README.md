# pyatuomaton

<!--
<p align="center">
    <img alt="pyautomation logo" src="https://github.com/ryanwarrick/pyautomaton/blob/master/docs/images/pyautomaton.png?raw=true" height="100">
</p>
-->

![license](https://img.shields.io/github/license/ryanwarrick/pyautomaton)
![GitHub last commit](https://img.shields.io/github/last-commit/ryanwarrick/pyautomaton)
[![GitHub issues](https://img.shields.io/github/issues/ryanwarrick/pyautomaton)](https://github.com/ryanwarrick/pyautomaton/issues)
![PyPI](https://img.shields.io/pypi/v/pyautomaton)
/[![code with hearth by ryanwarrick](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-ryanwarrick-ff1414.svg?style=flat-square)](https://github.com/ryanwarrick)

Python utility to automate various repetitive browser tasks with Selenium. Due to the nature of computing, much of our modern lives, both personally and professionally, can get quite repetitive. The goal of this project is to develop my BPA (Business Process Automation) skills so that I can efficiently and effectively automate away various tasks via python scripting.

For example...
* In a personal capacity, you may regularly open a handful of online banking sites to check the current balances for a set of accounts. Besides passing basic credentials, and MFA, these procedures involve time-intensive, "busy work" actions ripe for automation.
* In a professional cybersecurity context, you will likely find yourself repeatedly performing the same basic administrative tasks. For example, you may check admin console A for X alert. Then, you may take remedial action against X alert by executing action Y within admin console B. Completing this task loop may be required multiple times daily. In this example, the human actor has effectively become an overpaid and unecessarily complicated webhook to link the two cybersecurity administrative consoles.

Whenever human workloads begin to resemble the functionality of a webhooks or browser macros, one could benefit from the short-term injection of automation efforts into these tasks to reduce long-term human time costs.

To pay respects to the topic of automation, I must acknowledge its potential pitfalls including improper project scoping, over-engineering, and code fragility leading to increased development time. My goal is for this project to serve as a learning opportunity so that I can improve the value proposition of my BPA efforts and overcome the common automation pitfalls. I'd be  remiss of me to not include this XKCD comic commenting on these very pitfalls and their effects:

<p align="center">
    <img alt="XKCD #1319 - Automation" src="https://imgs.xkcd.com/comics/automation.png" height="250">
</p>

  
## Installation

Prerequisite: System must have Python 3.6+ installed (and pip - included with Python). See [Python docs here](https://wiki.python.org/moin/BeginnersGuide/Download) for help installing.

Next, run the following pip command in the terminal to install the package from the Python Package Index:
```
python -m pip install pyautomaton
```

<!--See gif illustrating pip install of the package:
![Install Demo](docs/images/install_demo.gif)
-->

## Setup/Configuration

This script interacts with various secured websites via the [Selenium](https://github.com/SeleniumHQ/selenium) open-source Python library. Therefore, we must provide some key credential information to the application via a configuration file.

### Steps: 
1) Create a customized configuration file for use by the package's 'pyautomation' console command:
    * Download a copy of the [template configuration file ('config.ini') ](https://github.com/ryanwarrick/pyautomation/blob/master/config.ini) found  at the project root.
        * (Note: If you are working from source, you can grab the same file from your clone of the repo)
    * Edit the file to overwrite the placeholder values with the appropriate values.

<!--	
See example below...

```
[DEFAULT]
email = ABCDEFGHI
username = XYZJKL
```
-->

## Usage/Examples

For help, execute the following in the console
```
pyautomation --help
```
### Package Primary Function 1
```
pyautomation <config_ini_file_path> ......
```
![Demo 1](docs/images/demo_1.gif)

### Package Primary Function 2
```
pyautomation <config_ini_file_path> .....
```
![Demo 2](docs/images/demo_2.gif)

  
## Contributors

- Development: [@ryanwarrick - Github](https://www.github.com/ryanwarrick)