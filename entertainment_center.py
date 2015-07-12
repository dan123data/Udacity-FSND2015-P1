import media, fresh_tomatoes

toy_story = media.Movie('Toy Story',
						'A story of a boy and his toys that come to life.',
						'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
						'https://www.youtube.com/watch?v=vwyZH85NQC4')


avatar = media.Movie('Avatar',
					'A marine on an alien planet.',
					'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
					'https://www.youtube.com/watch?v=5PSNL1qE6VY')


iron_man = media.Movie('Iron Man',
					'A billionaire industrialist and genius inventor, Tony Stark (Robert Downey Jr.), is conducting weapons tests overseas, but terrorists kidnap him to force him to build a devastating weapon. Instead, he builds an armored suit and upends his captors. Returning to America, Stark refines the suit and uses it to combat crime and terrorism.',
					'https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG',
					'https://www.youtube.com/watch?v=8OCJRbzdzaU')

school_of_rock = media.Movie('School of Rock',
					'A billionaire industrialist and genius inventor, Tony Stark (Robert Downey Jr.), is conducting weapons tests overseas, but terrorists kidnap him to force him to build a devastating weapon. Instead, he builds an armored suit and upends his captors. Returning to America, Stark refines the suit and uses it to combat crime and terrorism.',
					'https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG',
					'https://www.youtube.com/watch?v=8OCJRbzdzaU')

ratatouille = media.Movie('Ratatouille',
					'A billionaire industrialist and genius inventor, Tony Stark (Robert Downey Jr.), is conducting weapons tests overseas, but terrorists kidnap him to force him to build a devastating weapon. Instead, he builds an armored suit and upends his captors. Returning to America, Stark refines the suit and uses it to combat crime and terrorism.',
					'https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG',
					'https://www.youtube.com/watch?v=8OCJRbzdzaU')

midnight_in_paris = media.Movie('Midnight in Paris',
					'A billionaire industrialist and genius inventor, Tony Stark (Robert Downey Jr.), is conducting weapons tests overseas, but terrorists kidnap him to force him to build a devastating weapon. Instead, he builds an armored suit and upends his captors. Returning to America, Stark refines the suit and uses it to combat crime and terrorism.',
					'https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG',
					'https://www.youtube.com/watch?v=8OCJRbzdzaU')

# hunger_games = media.Movie('Hunger Games',
# 					'A billionaire industrialist and genius inventor, Tony Stark (Robert Downey Jr.), is conducting weapons tests overseas, but terrorists kidnap him to force him to build a devastating weapon. Instead, he builds an armored suit and upends his captors. Returning to America, Stark refines the suit and uses it to combat crime and terrorism.',
# 					'https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG',
# 					'https://www.youtube.com/watch?v=8OCJRbzdzaU')


movies = [toy_story, avatar, iron_man, school_of_rock, ratatouille, midnight_in_paris]
fresh_tomatoes.open_movies_page(movies)