# Headlines

### Vision
Headlines application displays up-to-date news headlines, weather information,
and currency exchange rates to our users.

### Application should provide:
- Storing the account information of all users;
- Automatically retrieves recent news articles from specific publications;
- Display headlines and summaries of the retrieved articles to our users; 
- Get input from users so that they can customize their experience;
- Displays weather data to our application;
- Displays currency data to our application;
- Remember users' preferences from one visit to the next;


1. Users
   <br>
   <br>
    1.1 User account control  
<br>
    The application allows multiple, unrelated users to use the same app. That is why, each user should have
   a private login account for the system. 
<br>

- Application displays form for registration;
- User enters email, password, and name and presses “Sing up” button;
- If any data is entered incorrectly, incorrect data messages are displayed;
- If the user with the email is already exist, then error message is displaying;
- If entered data is valid, then email and hashed password are adding to database;
- If data is added to database, "Login" page is shown;
- User enters email and password and presses "Login" button;
- If entered data is valid, the "Account" page is shown;
- If any data is entered incorrectly, incorrect data messages are displayed.  
<br>
<br>
2. Headlines
<br>
<br>
    2.1. Headlines and article texts
<br>
<br>
   On the "Home" page some headlines for the chosen publication are shown
<br>
- The list of news headlines, date, and summary for each recent article for BBC publication is shown 
  as a default publication;  
- The application shows a drop-down box;
- User chooses the name of a publication if they want to read another, not a default, publication;
- If the user chose the publication, a list of headlines for it is shown;
- If the user presses on a headline, they will be redirected to the chosen publisher site to read 
  the original article;
- When the user visits the application next time, the previously chosen publication will be a default one.
<br>
<br>
3. Weather
<br>
<br>
  3.1 Displaying the current weather
<br>
<br>
   On the "Home" page the current weather is shown
<br>
- The OpenWeatherMap API is used to get the current weather;
- Application displays the weather for city Dnipro as a default city;
- The application shows a search box;
- The user input a name of a City and press "Submit" button;
- The current weather for the chosen city is shown;
- When the user visits the application next time, the previously chosen city will be a default one.
<br>
<br>
4. Currency
<br>
<br>
  4.1 Displaying the exchange rates
<br>
<br>
   On the "Home" page some exchange rates are shown
<br>
- The PrivatBank API is used to get some exchange rates;
- Application displays the exchange rates for USD currency as the default ones;
- The application shows a drop-down box;
- The user chooses the available currency;
- The exchange rates for the chosen currency are shown;
- When the user visits the application next time, the previously 
  chosen currency exchange rates will be the default ones.