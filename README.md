
# VirtualPet 🐾

**VirtualPet** is a fun and interactive web application where you can take care of a virtual pet. Feed it, play with it, and watch it grow! The project is built using **Flask** (Python) and deployed on **Render**.

🌐 **Live Demo**: [https://virtualpet-yqk0.onrender.com](https://virtualpet-yqk0.onrender.com)

---

## Features ✨

- **Adopt a Virtual Pet**: Give your pet a name and start taking care of it.
- **Feed Your Pet**: Keep your pet happy and healthy by feeding it.
- **Play with Your Pet**: Increase your pet's happiness by playing with it.
- **Random Events**: Experience random events that affect your pet's mood and health.
- **Level Up**: Watch your pet grow and level up as you take care of it.
- **Game Over**: If your pet's health or happiness drops too low, it's game over!

---

## Technologies Used 🛠️

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Jinja2 Templates
- **Deployment**: Render
- **Version Control**: Git & GitHub

---

## How to Run Locally 🚀

Follow these steps to set up and run the project on your local machine.

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/jjingofarouk/VirtualPet.git
   cd VirtualPet
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**:
   ```bash
   python run.py
   ```

6. **Access the Application**:
   Open your browser and go to `http://127.0.0.1:5000`.

---

## Deployment on Render 🚀

The project is deployed on **Render**, a cloud platform for hosting web applications. Here's how you can deploy your own instance:

1. **Fork the Repository**:
   Fork this repository to your GitHub account.

2. **Create a Render Account**:
   Sign up at [https://render.com](https://render.com) if you don’t have an account.

3. **Create a New Web Service**:
   - Go to the Render dashboard and click **New Web Service**.
   - Connect your GitHub account and select the forked repository.
   - Configure the following settings:
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `python run.py`
   - Click **Create Web Service**.

4. **Access Your Deployed App**:
   Once the deployment is complete, Render will provide you with a live URL for your application.

---

## Project Structure 📂

```
VirtualPet/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   └── pet.py
│   ├── routes/
│   │   ├── home.py
│   │   ├── actions.py
│   │   └── reset.py
│   ├── utils/
│   │   ├── persistence.py
│   │   ├── events.py
│   │   ├── status_checker.py
│   │   └── leveling.py
├── templates/
│   ├── index.html
│   └── game_over.html
├── static/
│   └── styles.css
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

---

## Contributing 🤝

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License 📄

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments 🙏

- Thanks to **Render** for providing an easy-to-use deployment platform.
- Special thanks to the Flask community for their amazing documentation and support.

---

Enjoy taking care of your virtual pet! 🐶🐱

