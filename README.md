# MongoDB_Assignment

## comments collection

Q1. Find top 10 users who made the maximum number of comments

Ans: Group by email as email of user is unique to get number of users for comments:-
[Code](https://github.com/Shubham-Sigmoid044/MongoDB_Assignment/blob/ae695283bdccd77a5550ba12dd336e117284a853/comments.py#L5)
![image](https://user-images.githubusercontent.com/98617328/153005201-70814f92-b369-43c3-89b0-56a405588ab2.png)


Q2. Find top 10 movies with most comments

Ans: Got each individual movie_id with number of comments on each movie_id, Converted bson objectId to convert in appropriate format and used to find all Ids in movie.
[Code](https://github.com/Shubham-Sigmoid044/MongoDB_Assignment/blob/ae695283bdccd77a5550ba12dd336e117284a853/comments.py#L18)
<img width="1364" alt="image" src="https://user-images.githubusercontent.com/98617328/153005841-95e1a781-6b72-46d2-b30c-3caab792bd97.png">

Q3. Given a year find the total number of comments created each month in that year

Ans: Converted object date type into date type, use the list to hold the id and numberlong date format, Updated the comments with new dob format to make query easily, converted numberlong format into date format to seperate month and year, group by month to get the number of user each month.
[Code](https://github.com/Shubham-Sigmoid044/MongoDB_Assignment/blob/ae695283bdccd77a5550ba12dd336e117284a853/comments.py#L53)
<img width="1368" alt="image" src="https://user-images.githubusercontent.com/98617328/153006647-dab3b214-f25c-4c87-8070-88d71987ede7.png">


## movies collection

## i. Find top `N` movies - 

Q1. with the highest IMDB rating

Ans: Use find query and sorted with IMDB rating.
[Code](https://github.com/Shubham-Sigmoid044/MongoDB_Assignment/blob/ae695283bdccd77a5550ba12dd336e117284a853/movies_i.py#L4)
<img width="1362" alt="image" src="https://user-images.githubusercontent.com/98617328/153007417-c00ee051-9d53-452e-89e0-a3a7840a9db7.png">

Q2. with the highest IMDB rating in a given year

Ans: matched with given year and sorted with IMDB rating
[Code](https://github.com/Shubham-Sigmoid044/MongoDB_Assignment/blob/b91d7916784a71a1655688b6bed82f75ea4786c5/movies_i.py#L17)
<img width="1357" alt="image" src="https://user-images.githubusercontent.com/98617328/153014363-44c8da09-0ebb-4b41-93f2-40607c280773.png">


Q3. with highest IMDB rating with number of votes > 1000

Ans: searched only those values whose imdb is greater than 1000
[Code](https://github.com/Shubham-Sigmoid044/MongoDB_Assignment/blob/b91d7916784a71a1655688b6bed82f75ea4786c5/movies_i.py#L27)
<img width="1360" alt="image" src="https://user-images.githubusercontent.com/98617328/153014751-6dbdedc3-b43a-4078-b015-560c0b511d4a.png">


Q4. with title matching a given pattern sorted by highest tomatoes ratings

Ans: searched the title only matching with given regex

## ii. Find top `N` directors - 
[Code](https://github.com/Shubham-Sigmoid044/MongoDB_Assignment/blob/main/movie_ii.py)

Q1. who created the maximum number of movies

Ans: group by directors and calculated numMovies for each

Q2. who created the maximum number of movies in a given year

Ans: group by given year to get the result

Q3. who created the maximum number of movies for a given genre

Ans:  who created the maximum number of movies for a given genre

## iii. Find top `N` actors -  
[Code](https://github.com/Shubham-Sigmoid044/MongoDB_Assignment/blob/main/movie_iii.py)

Q1. who starred in the maximum number of movies

Ans: as cast is given in form of array, unwind all the cast and the group by the cast to get the results

Q2. who starred in the maximum number of movies in a given year

Ans: unwind the cast and match with given year and then group by actors

Q3. who starred in the maximum number of movies for a given genre

Ans: unwind the cast and match with given genre and then group by actors

## iv. Find top `N` movies for each genre with the highest IMDB rating 
[Code](https://github.com/Shubham-Sigmoid044/MongoDB_Assignment/blob/main/movie_iv.py)
<img width="1362" alt="image" src="https://user-images.githubusercontent.com/98617328/153018040-ddc7431d-5f2b-46e3-ae12-7dd8aafa6a12.png">



## theaters collection -

## i. Top 10 cities with the maximum number of theatres
[Code](https://github.com/Shubham-Sigmoid044/MongoDB_Assignment/blob/main/theaters.py)
<img width="1368" alt="image" src="https://user-images.githubusercontent.com/98617328/153016989-45db46f2-ba43-450c-a12e-105bf89c0cff.png">


## top 10 theatres nearby given coordinates

Ans: extracted the theaterid and location in sepearte list, created a list of id and coordinates to update the theater so that I can easily create the 2dsphere index, Updated all the values of theaters by adding coordinates in specific geospatial format so that index can be easily applied, Searched for given lat and long values.
[Code](https://github.com/Shubham-Sigmoid044/MongoDB_Assignment/blob/b91d7916784a71a1655688b6bed82f75ea4786c5/theaters.py#L17)
<img width="1362" alt="image" src="https://user-images.githubusercontent.com/98617328/153017724-a2006658-aeee-4297-990e-02f94b53ee6d.png">


