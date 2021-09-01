![license](https://img.shields.io/github/license/ryanwarrick/pyautomaton)
![GitHub last commit](https://img.shields.io/github/last-commit/ryanwarrick/pyautomaton)
[![code with hearth by ryanwarrick](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-ryanwarrick-ff1414.svg?style=flat-square)](https://github.com/ryanwarrick)


# Summary
This repository is a sort of playground to gain experience with Python Selenium. Currently, this is not a complete project, rather just scratch work.

## Motivation
Despite advancements in modern computing, many computer tasks today are still quite repetitive, especially in IT. Considering the need to automate these repetitive tasks, I'm learning Selenium with an ultimate goal of increasing the efficiency of my BPA development work.

##  Goal
To give my learning efforts direction, I aim to automate away some 'low-hanging fruit' repetitive web tasks in my personal life. The intended result is to free up the user for more human-based tasks. Let bots do bot things, let humans do human things.

## Current Status
This project is currently on my back burner. Time permitting, additional development work and documentation is planned for this project.

# Functionality

## Credit Karma
### Description
At this time, the sole function offered by the project is to fetch credit scores and score details from a Credit Karma user's profile. The 'credit_karma_bot' will:
- log into Credit Karma
- navigate to the appropriate pages
- capture X from from each of the reporting agencies:
  - score
  - score details
- log out
- print captured results to console
  
### Usage
From the project root directory, execute the following command: `python -m pyautomaton -k '<credit_karma_username_email>'`
