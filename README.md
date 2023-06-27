# :film_projector:	Data Analysis of Movies! :movie_camera:	

<h2><strong>Overview:</strong></h2>
1. Introduction and Purpose :performing_arts:	<br>
2. Tech Stack :film_strip:	<br>
3. Future Considerations :clapper:	<br>
4. Dataset Source :vhs:	
<br><hr><br>
<h2><strong>Introduction:</strong></h2>
<h3><br></h3>
This project is a presentation of insights regarding the top 1,000 movies on iMDB according to rating and ranking.
Some questions I answer are:<br>
- What genres contain the best movies by rating?<br>
- What movies have the highest difference in rating between iMDB vs Metacritic?<br>
-  
<br><br><br>
The dataset description can be found in the txt file. Watch this demo video <s>here</s> to listen to me explain my findings.
<br><hr><br>
<h2><strong>Tech stack:</strong></h2>
Languages: Python<br>
Libraries/Frameworks: Pandas, NumPy, SciPy Stats, SciKit Learn, Matplotlib, Seaborn<br>
Developer Tools: Jupyter Notebook, Trello, Tableau<br>
Database Source: iMDB site scraped by ScraPy</br>
<br><hr><br>
<h2><strong>Future Considerations:</strong></h2>
<ul>
<li>Retrieving the directors, stars, and gross revenue was skipped. This was because of the way the css wrappers were established in the css file. In the future, I would attempt to edit the ScraPy spider to fetch directors, main actors, and gross reveune.</li>
</ul>
<br><hr><br>
<h2><strong>Dataset Source:</strong></h2><br>
This dataset was scraped by ScraPy. The first page of the list is found <a href="https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&sort=user_rating,desc&view=advanced">here</a>.