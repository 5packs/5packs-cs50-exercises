# GPoznanS

---

### Resources
- Streamlit[https://streamlit.io]
- Folium[https://folium.streamlit.app]
- PoznanAPI[https://egov.psnc.pl/node/29]

---

### Description:

**Project Summary**
My project is a data visualization web app based around the streamlit rapid development library for python. It utilizes the free APIs shared by the city of Poznan to pinpoint the location of certain crucial points on the city map. The project also uses streamlit's folium component which makes the map a lot more detailed and easy to work with in comparison to other streamlit map objects. Thanks to streamlit I could focus more on the backend and API handling side of my project rather than designing the website itself from scratch and focusing too much on the frontend. Through the project I learned a lot about how APIs work and I can now write my own APIs if I need one in the future. Each of the files stands for one subpage of the web app (home, bus and tram stops, monuments, parking ticket machines). This allowed me to easily implement a sidebar to the website which allows for fast navigation in between the different services. I decided to implement the sidebar instead of a seperate menu page as it seems more intuitive to use and allows for quick switching between the services. This project also does not utilize any database, this is due to all the data being fetched from the API whenever you run the page and allows for the app to be very small in size despite operating on lots of data.

**Functionality**
The web app itself has three main functions. Firstly it pinpoints all the famous monuments locations and names in Poznan on an interactive map. Secondly it allows you to also locate all the parking ticket dispensers which when clicked display information on the methods of payment available at the dispenser such as: card, coin or the city public transport card. Lastly the app allows you to display all of the public transport stations in Poznan and around it. Once you press any of the stations you can see the information regarding the zone in which the stop is located as well as which transport lines pass through the station.

**Reasons For**
I decided to create this project because I wanted to get better at utilizing different apis. I also wanted to learn some basic data science framework utilization as I might pursue a career in data science in the future. This led to me researching the most commonly used data visualization frameworks and libraries for python and finally finding streamlit. As mentioned previously decided to use streamlit because I really wanted to create a responsive and simple to use web app while avoiding the hassle related with structuring a website from scratch using HTML and CSS.

---

### Video Demo:
*DEMO*[https://www.youtube.com/watch?v=qoblAp43ZcE]

---

### How to run:
1. Check if you have python installed on your computer
2. Open the project as is in some coding environment
3. Install all the libraries mentioned at the beggining of the `Home_🏠.py` file
4. Run the project through the terminal by executing `streamlit run Home_🏠.py`
5. The website should open in your default browser if it doesnt follow the link in your terminal
6. Enjoy!
