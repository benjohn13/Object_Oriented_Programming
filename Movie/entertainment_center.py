import fresh_tomatoes
import media

#This is one instance/ object inside the Movie class.
lotr_fellowship = media.Movie("Lord of the Rings - The Fellowship of the Ring",
                        "With the help of his companions, Frodo Baggins sets off on a journey across Middle Earth to destroy the one ring of power.",
                        "http://vignette4.wikia.nocookie.net/lotr/images/7/7d/Fellowship_of_the_Ring_Poster_02.jpg/revision/latest?cb=20150203041117",
                        "https://www.youtube.com/watch?v=Pki6jbSbXIY")

#This is another instance.
lotr_two_towers = media.Movie("Lord of the Rings - The Two Towers",
                        "An alliance between the Dark Lord Sauron and the Wizard Saruman is forged with the intent of destroying the free world of men.",
                        "http://img4.wikia.nocookie.net/__cb20150203041214/lotr/images/9/98/The_two_tower.jpg",
                        "https://www.youtube.com/watch?v=2dlRvAjU_RI")

lotr_the_king = media.Movie("Lord of the Rings -  The Return of the King",
                        "The final chapter of the ring; Aragorn must rise up as the true ruler of free men if he is to defeat the dark alliance against Middle Earth.",
                        "http://img3.wikia.nocookie.net/__cb20150203041337/lotr/images/b/ba/Rie.jpg",
                        "https://www.youtube.com/watch?v=r5X-hFf6Bwo")

the_wind= media.Movie("The Wind Rises",
                        "In 1918, the young Jiro Horikoshi longs to become a pilot, but his nearsightedness prevents it. He then chooses to study aeronautical engineering and dreams creating the world's greatest planes",
                        "https://doompaul.files.wordpress.com/2015/01/the-wind-rises-poster.jpg",
                        "https://www.youtube.com/watch?v=imtdgdGOB6Q")

sao= media.Movie("Sword Art Online",
                        "When Kirito, a boy from Japan in the year 2022, logs into a virtual reality game callled SAO, he and 10,000 other players find they cannot log out.",
                        "http://cwacharacter.wikia.com/wiki/File:SAO_1.jpg",
                        "https://www.youtube.com/watch?v=ALCLCvNJ7iY")

mushi= media.Movie("Mushishi",
                        "Mushishi is set in an imaginary time between the Edo and Meiji periods, featuring some 19th-century technology but with Japan still as a closed country. The story features ubiquitous creatures called Mushi that often display what appear as supernatural powers.",
                        "http://static.tvtropes.org/pmwiki/pub/images/13207.jpg",
                        "https://www.youtube.com/watch?v=VBBFDb0hC4Y") #I couldn't find a trailer I liked for Mushishi, so I chose the opening theme song instead. I feel like the song conveys more of the feeling of the show better anyway.

#This is the list with seperated values
movies = [lotr_fellowship, lotr_two_towers, lotr_the_king, the_wind, sao, mushi]

#Open movie website in browser
fresh_tomatoes.open_movies_page(movies)
