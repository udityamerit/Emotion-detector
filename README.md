# Guess the Emotion Game 🎮

## Introduction
**Guess the Emotion** is a fun and interactive game where players can test their ability to recognize emotions. The game uses AI to detect emotions in images captured via a webcam and compares them with the player’s guess. It's an engaging way to learn about AI/ML applications while having fun!

---

## Features
- **Emotion Detection:** Detects emotions like happy, sad, angry, surprise, and neutral.
- **User Interaction:** Players guess the emotion before the AI prediction.
- **Real-Time Feedback:** Points are awarded based on the correctness of the guess.
- **Webcam Integration:** Capture images directly using the webcam.
- **Simple UI:** Built using Streamlit for ease of use.

---

## How to Run the Game

### Prerequisites
1. Python 3.7 or higher
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Steps to Play
1. Clone the repository or download the code files.
2. Install the dependencies using the provided `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the game using Streamlit:
   ```bash
   streamlit run game.py
   ```
4. Follow the on-screen instructions to:
   - Guess the emotion.
   - Capture your image using the webcam.
   - See if your guess matches the AI’s prediction.

---

## File Structure
```
📂 Guess-the-Emotion-Game
├── Emotion_ditector.py             # Main game script
├── requirements.txt    # List of dependencies
├── README.md           # This file
```

---

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: For building the user interface.
- **OpenCV**: For image processing and webcam integration.
- **FER**: Pre-trained facial emotion recognition model.

---

## Sample Screenshot
![Sample Screenshot](https://via.placeholder.com/800x400.png?text=Sample+Screenshot)

---

## Future Enhancements
- Add a leaderboard to track player scores.
- Include more emotions for detection.
- Multiplayer mode.
- Provide tips for players to mimic specific emotions.

---

## License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements.

---

## Author
Developed by **[Uditya Narayan Tiwari](https://github.com/udityamerit)**.
