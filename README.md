🎲 Dice Game (Python OOP)

A simple Dice Game built using Object-Oriented Programming (OOP) principles in Python. 
The game is played between a user and the computer. 
Both roll a die, and the one with the higher number wins the round.
The first to reach "0 points" wins the game!

---

OOP Concepts Used

This project uses the following Object-Oriented Programming concepts:

✅ 1. Classes and Objects
- Dice, Player, and DiceGame are all implemented as classes.
- Instances of these classes represent real game entities.

✅ 2. Encapsulation
- Internal state is managed using private variables (e.g., _value, _counter).
- Access to data is controlled through getter methods and @property.

✅ 3. Composition
- A Player contains a Dice object.
- The DiceGame class is composed of two Player objects.

✅ 4. Abstraction
- Methods like roll_dice(), play_round(), and update_counters() hide internal logic and simplify usage.

---

🚀 How to Run the Game

Step 1: Clone the Repository

git clone https://github.com/siva-sankari-n/Dice_Game.git
cd Dice_Game
