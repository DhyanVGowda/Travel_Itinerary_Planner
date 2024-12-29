Travel Itinerary Planner

Welcome to the Travel Itinerary Planner! This project is designed to simplify trip planning and coordination by allowing users to create, manage, and share detailed travel itineraries. It integrates a Flask backend with a Streamlit frontend and a MySQL database for robust data management.

Features
	•	User Authentication: Secure login and sign-up functionality.
	•	Trip Management: Create and manage trips with options to add destinations, activities, accommodations, expenses, and packing essentials.
	•	Visualizations: Interactive graphs to analyze and compare trip data.
	•	Database Integration: Efficient CRUD operations with MySQL, including stored procedures and triggers.
	•	Intuitive Interface: User-friendly front-end developed with Streamlit.

Installation and Setup

Prerequisites
	•	Python 3.11
	•	MySQL Server
	•	Git

Steps to Set Up the Project
	1.	Clone the Repository

git clone https://github.com/DhyanVGowda/Travel_Itinerary_Planner.git
cd Travel_Itinerary_Planner


	2.	Install Python Libraries
	•	Using requirements.txt:

pip install -r requirements.txt


	•	Required Libraries:
	•	Flask
	•	Streamlit
	•	Pandas
	•	Plotly
	•	PyMySQL
	•	Requests

	3.	Database Setup
	•	Install MySQL Server.
	•	Open MySQL Workbench and execute the SQL scripts in the sql folder:
	1.	1_entities.sql (Creates schema)
	2.	2_data_dump.sql (Inserts data)
	3.	3_procedures.sql (Creates stored procedures)
	4.	4_triggers.sql (Sets up triggers)
	4.	Configure Database Credentials
	•	Edit the configs.json file in the src folder:

{
  "db_username": "your_username",
  "db_password": "your_password",
  "port": "8080"
}


	5.	Run the Backend

python src/backend/main.py

The Flask server will run on http://127.0.0.1:8080.

	6.	Launch the Frontend

streamlit run src/gui/trip_planner_gui.py

The Streamlit app will open in your default browser.

Usage
	•	Sign Up: Create an account with your email and phone number (used as the password).
	•	Log In: Access your account to start planning trips.
	•	Plan Trips: Add destinations, activities, accommodations, and track expenses.
	•	Visualize Data: Use interactive graphs to analyze trip details.
	•	Logout: Securely log out of your session.

Lessons Learned and Future Work

Lessons Learned
	•	Gained proficiency in Python, Flask, and Streamlit.
	•	Enhanced understanding of database design and management.
	•	Explored real-world use cases in the travel and tourism industry.

Future Enhancements
	•	Integration with external travel services (e.g., APIs for flights and accommodations).
	•	Enhanced personalization based on user preferences.
	•	Interactive maps and virtual tours.
	•	Social sharing of itineraries.

Contributors
	•	Dhyan Vasudeva Gowda
	•	Team Members: Shrey Shah, Anshuman Raina.

License

This project is licensed under the MIT License.