
import bs4
import urllib
import pandas as pd


url = urllib.urlopen("http://www.imdb.com/search/title?release_date=2005,2016&title_type=feature&user_rating=1.0,10")
readHtml = url.read()
url.close()

print "scrapping the website";

soup = bs4.BeautifulSoup(readHtml, 'html.parser')
movie_containers = soup.find_all('div',class_ = 'lister-item mode-advanced');
#print(type(movie_containers));
#print(len(movie_containers));

fm = movie_containers[0]
#print fm.h3.a.text

names = []
years = []
imdb_ratings = []
metascores= []
votes=[]

for container in movie_containers:
	#if container.find('div',cliass_ = 'rating-metascore') is not None:
#		print "hello"
		name = container.h3.a.text
#		print name
		names.append(name)
		
		year = container.h3.find('span', class_ = 'lister-item-year').text
		years.append(year)
	
		imdb = float(container.strong.text)
		imdb_ratings.append(imdb);

		m_score = container.find('span',class_ = 'metascore').text
		metascores.append(int(m_score))
		
		vote = container.find('span',attrs = {'name':'nv'})['data-value']
		votes.append(int(vote))



test_df = pd.DataFrame({'movie': names, 'year':years, 'imdb': imdb_ratings, 'metascore':metascores,'votes':votes
			
			});

test_df2 = test_df.set_index("movie",drop = False)

test_df.to_csv('imdb_list.csv',sep='\t')

print "saved the scrapped details in the imdb_list.csv in the same path";

print "Enter the movie:",
movie_name = raw_input()
print test_df2.loc[movie_name,: ]

test_df.to_csv('imdb_list.csv',sep='\t')
#print test_df.info()
#print test_df
