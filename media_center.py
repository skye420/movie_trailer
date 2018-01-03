import template_html
import media

avengers = media.Movie("Avengers",
"Bunch of super hero killing an monster",
"https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
"https://www.youtube.com/watch?v=6ZfuNTqbHE8")

seven_psychopath = media.Movie("Seven Psychopath",
"Seven psychopath on 1 movie would u expect?",
"https://upload.wikimedia.org/wikipedia/en/e/e3/Seven_Psychopaths_Poster.jpg",
"https://www.youtube.com/watch?v=jsHR77oQKEY")

november_criminals = media.Movie("November Criminals",
"Addison Schacht (Ansel Elgort) investigates the murder of his friend Kevin, with the help of Phoebe (Chloe Grace Moretz), and they discover the truth is darker than they ever imagined.",
"https://upload.wikimedia.org/wikipedia/en/6/6f/November_Criminals_%28film%29.png",
"https://www.youtube.com/watch?v=RUZLUisXtP4")

justice_league = media.Movie("Justice League",
                             "The Flash, Wonder Woman, Superman, Batman, etc make a alliance for destroy aliens",
                             "https://www.cgv.id/uploads/movie/compressed/MOV3355.jpg",
                             "https://www.youtube.com/watch?v=3cxixDgHUYw")

shesoutmyleague = media.Movie("She's Out of My League",
                        "An average Joe meets the perfect woman, but his lack of confidence and the influence of his friends and family begin to pick away at the relationship.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkwMTY5ODA1MF5BMl5BanBnXkFtZTcwODYyNzAxMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=9mj4_hUEnpU")


split = media.Movie("Split",
                    "An person who have 32 identity",
                    "https://upload.wikimedia.org/wikipedia/en/3/31/Split_%282017_film%29.jpg",
                    "https://www.youtube.com/watch?v=84TouqfIsiI")


movies =  [avengers,seven_psychopath,november_criminals,justice_league,shesoutmyleague,split]
template_html.open_movies_page(movies)
