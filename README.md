# BTS World: Magic Shop Calculator

## Description

This tool allows players of the BTS World mobile game manage their card collection and find optimal card combinations for different mission types within the game. Initially built to solve regular missions, it was later expanded to handle the missions from the Another Story Season 2 (Magic Shop) game mode using a dynamic programming approach.

## Features

cardsconverter.py: a script that takes the cards data from the BTS World Calculator and converts it into a text file containing human-readable cards data for the main script (magicshop_solver.py).

gems.py: a script that calculates the number of gems required to obtain an event card based on mission bonuses, days remaining, current items, and target items. The script assumes optimal play, with replaying the best mission on the last day to reach the target, where each replay costs 15 gems.

magicshop_solver.py: a script containing the logic for card management, BTS member management and mission solving.

## Motivation

I started this project in July 2019, the summer before I started my undergraduate studies in Statistics and Computer Science at McGill University. It was the month after BTS World has come out and I wanted to use it as an opportunity to practice Object-Oriented Programming (OOP) in Python. While the design may not reflect polished software engineering, it helped me deepen my understanding of algorithms and Python fundamentals. By analyzing the components of BTS World, such as cards, members, and missions, I learned how to design classes and implement methods to reflect the game's mechanics. This approach enabled me to model the problem effectively, enhancing my understanding of software design.

In an April 2020 update, the game introduced the Another Story Season 2 game mode, also known as Magic Shop. Solving missions in this game mode requires a dynamic programming approach. I was introduced to dynamic programming during my Fall 2020 Algorithms and Data Structures course at McGill. Shortly after learning the concept, I began implementing this algorithm in my project.

My biggest motivation for implementing this algorithm is that the [BTS World Calculator](https://btsworldcalculator.netlify.app/), which helps players evaluate their performance, requires users to manually test different card combinations for Magic Shop missions until they find a suitable one. The main issue with manually testing combinations is that players can't feasibly brute force through every possible card combination—it would take far too long. My algorithm provides a solution that not only finds an optimal combination more quickly but does so with greater accuracy, streamlining the process and improving efficiency for the player.
