# BTS World: Magic Shop Calculator

## Description

This tool allows players of the BTS World mobile game manage their card collection and find optimal card combinations for different mission types within the game. Initially built to solve regular missions, it was later expanded to handle the missions from the Another Story Season 2 (Magic Shop) game mode using a dynamic programming approach.

## Game Overview

BTS World is a mobile game where players collect and level up cards to complete missions. Each mission has a required score that players must meet or exceed to successfully complete it. Missions have multiple star ratings, with higher scores needed to earn more stars.

**Missions**

Each mission applies a multiplier to the four card stats: Empathy, Passion, Stamina, and Wisdom. These multipliers affect how much each stat contributes to the final mission score. For example, if a mission has a 200% multiplier for Empathy and Passion, a 100% multiplier for Stamina, and a 50% multiplier for Wisdom, the contribution of each stat is adjusted accordingly.

Given a card with 100 points in each stat, the final score calculation for that mission would be:
(200% × 100) + (200% × 100) + (100% × 100) + (50% × 100) = 350 points.

Note that if a multiplier applied to a stat results in a **non-integer value**, the decimal part is **truncated** (not rounded). For example, if a 50% multiplier is applied to a stat of 75, the result would be 37 instead of 37.5.

**Cards**

Each card in the game belongs to a BTS member (the members are RM, Jin, Suga, J-Hope, Jimin, V and Jungkook) and is categorized by star ratings ranging from 1-star to 5-star. The number of stars determines a card’s overall strength, with 5-star cards being the most powerful and 1-star cards being the most basic. Higher-star cards generally have better stats and provide higher scores in missions, making them more valuable for progression.

The stats of a card increase as the card levels up, with the maximum level determined by its star rating. The highest possible level for a card is 10 × its star rating. For example, a 5-star card can be leveled up to 50, while a 4-star card can reach level 40, and so on. However, there are some 5-star cards that can be leveled up to 60.

## Features

- `cardsconverter.py` — a script that takes the cards data from the BTS World Calculator and converts it into a .txt file containing human-readable cards data for the main script (`magicshop_solver.py`).

- `gems.py` — a script that calculates the number of gems required to obtain an event card based on mission bonuses, days remaining, current items, and target items. The script assumes optimal play, with replaying the best mission on the last day to reach the target, where each replay costs 15 gems.

- `magicshop_solver.py` — a script containing the logic for card management, BTS member management and mission solving. 

## Motivation

I started this project in July 2019, the summer before I started my undergraduate studies in Statistics and Computer Science at McGill University. It was the month after BTS World has come out and I wanted to use it as an opportunity to practice Object-Oriented Programming (OOP) in Python. While the design may not reflect polished software engineering, it helped me deepen my understanding of algorithms and Python fundamentals. By analyzing the components of BTS World, such as cards, members, and missions, I learned how to design classes and implement methods to reflect the game's mechanics. This approach enabled me to model the problem effectively, enhancing my understanding of software design.

In an April 2020 update, the game introduced the Another Story Season 2 game mode, also known as Magic Shop. Solving missions in this game mode requires a dynamic programming approach. I was introduced to dynamic programming during my Fall 2020 Algorithms and Data Structures course at McGill. Shortly after learning the concept, I began implementing this algorithm in my project.

My biggest motivation for implementing this algorithm is that the [BTS World Calculator](https://btsworldcalculator.netlify.app/), which helps players evaluate their performance, requires users to manually test different card combinations for Magic Shop missions until they find a suitable one. The main issue with manually testing combinations is that players can't feasibly brute force through every possible card combination—it would take far too long. My algorithm provides a solution that not only finds an optimal combination more quickly but does so with greater accuracy, streamlining the process and improving efficiency for the player.
