#### Problem 3: Movie Data Analysis

# Wrangling the data
def open_csv_file(file_name) :
    with open(file_name,"r") as fr :

        # a list containing all the lines of data in the IMDB-Movie-Data file
        lines = fr.readlines()

        # The header
        header = lines[0].strip().split(",")
        
        # Construct the dataset according to each item of the header by dictionary
        dataset = []
        for line in lines[1:] :
            value = line.strip().split(",")
            observed_value = {header[i]: value[i] for i in range(len(header))}

            dataset.append(observed_value)

        ''' dataset = [{observed value 1.},
                       {observed value 2.},
                       {observed value 3.},
                                 .
                                 .
                                 .
                       {observed value 1000.},] '''
        ''' eg. observed value 1. = {Rank : 55, Title : "The Dark", Genre : "Action|Crime|Drama",..., Metascore : 82}              '''

    return dataset


## Question 1. Top‐3 movies with the highest ratings in 2016?
def Q1(dataset) :
    # filter the observed value which year == 2016
    movie_2016 = []
    for movie in dataset :  # movie = {observed_value}
        if movie["Year"] == "2016" :
            movie_2016.append(movie)

    # Find the top-3 rating movie by sorted() in variable : Rating

    ## key 參數指定一個函數， 用於每次比較時會被調用來提取一個用於比較的鍵值
    ## key=lambda movie:float(movie["Rating"]) 接收電影(為一辭典)的鍵Rating下的值並轉成浮點數
    ## reverse=True 表示由Rating高到低排序
    sorted_rating_movie_2016 = sorted(movie_2016,key=lambda movie:float(movie["Rating"]),reverse=True) # 依照電影評分進行排序

    top_3_movies_2016 = sorted_rating_movie_2016[:3] # Top 3

    print("="*60)
    print("Question 1.")
    for i, movie in enumerate(top_3_movies_2016) :
        print(f"Top {i+1} movie is : \'{movie['Title']}\' with rating {movie['Rating']}")

    print()

## Question 2. The director who involves in the most movies?
def Q2(dataset) :
    director_count_dict = {}
    for movie in dataset :
        director = movie['Director']
        if director in director_count_dict :
            director_count_dict[director] += 1
        else :
            director_count_dict[director] = 1 # initialization if director not in the dictionary

    ## 找出字典director_count_dict中具有最大值的"鍵"
    top_director = max(director_count_dict, key=director_count_dict.get)

    print("="*60)
    print("Question 2.")
    
    print(f"\'{top_director}\' involves in the most movies! (with {director_count_dict[top_director]} movies)")
    print()


    ''' Another solution :

    # Collect all director that participates in movie
    director_list = []
    for movie in dataset :
        if movie['Director'] not in director_list :
            director_list.append(movie['Director'])

    # Count each director's participation
    count_director = [0 for _ in range(len(director_list))]
    for movie in dataset :
        for director in range(len(director_list)) :
            if movie['Director'] == director_list[director] :
                count_director[director] += 1
    
    max_count = max(count_director)
    index = count_director.index(max_count) 
    print("\'%s\' involves in the most movies! (with %d movies)"%(director_list[index],max_count))  '''

## Question 3. The actor generating the highest total revenue?
def Q3(dataset) :
    actor_totrev_dict = {}

    # Handle with missing value of total revenue
    for movie in dataset :
        revenue_str = movie['Revenue (Millions)'] 
        if revenue_str :
            revenue = float(revenue_str)
        else :
            revenue = 0

        # One movie may contain multiple actors splitting by "|"
        actors = movie['Actors'].split("|")
        for actor in actors :
            if actor in actor_totrev_dict :
                actor_totrev_dict[actor] += revenue
            else :
                actor_totrev_dict[actor] = revenue  # initialization if actor not in the dictionary
    
    richest_actor = max(actor_totrev_dict, key=actor_totrev_dict.get)

    print("="*60)
    print("Question 3.")
    print(f"\'{richest_actor}\' has the highest total revenue with ${actor_totrev_dict[richest_actor]} millions!")
    print()

## Question 4. The average rating of Emma Watson’s movies?
def Q4(dataset) :
    total_rating = 0
    count = 0

    # Collect all movies that Emma Watson participated
    for movie in dataset :
        # One movie may contain multiple actors splitting by "|"
        actors = movie["Actors"].strip().split("|")

        for actor in actors :
            if actor.strip() == "Emma Watson" : # eg. 處理含有| Emma Watson| Amy Adams 之情形
                total_rating += float(movie["Rating"])
                count += 1
    
    ave_rating = total_rating/count

    print("="*60)
    print("Question 4.")
    print("The average rating of Emma Watson’s movies is : %f"%(ave_rating))
    print()

## Question 5. Top‐4 actors playing the most movies? 
def Q5(dataset) :
    # Collect all actors and then record their participation in movies 
    actor_dict = {}              
    
    for movie in dataset :
        actors = movie["Actors"].strip().split("|")

        for actor in actors :
            actor_dict[actor.strip()] = 0 # initialization of all actors

    # Calculate the frequency of each actor
    for movie in dataset :
        actors = movie["Actors"].strip().split("|")

        for actor in actors :
            actor_dict[actor.strip()] += 1

    # Choose the top 4 actors playing the most movies, and then print them all
    sorted_participation = sorted(actor_dict.items(), key=lambda x : x[1],reverse=True)  # x[1] 表示對電影數量進行降序排列
    
    top4_actor_participation = sorted_participation[:4]

    print("="*60)
    print("Question 5.")
    for i, (actor,count) in enumerate(top4_actor_participation) :
        print(f"Top {i+1}. actor is \'{actor}\' with {count} participations!")

    print()

## Question 6. Top‐7 frequent collaboration pairs of director & actor?
def Q6(dataset) :
    director_actor_pairs = {}

    # Collect all director and actor pairs
    for movie in dataset :
        director = movie['Director']
        actors = movie['Actors'].strip().split("|")
        
        for actor in actors :
            pair = (director, actor.strip())

            # Calculate the frequency collaboration of director and actor
            if pair in director_actor_pairs:
                director_actor_pairs[pair] += 1
            else :
                director_actor_pairs[pair] = 1 # initialization
    
    # 進行大小排序 : x[1] 表示取得鍵值(i.e.合作次數)
    top_7_pairs = sorted(director_actor_pairs.items(), key=lambda x : x[1], reverse=True)[:7]
    
    print("="*60)
    print("Question 6.")
    for i, ((director, actor), count) in enumerate(top_7_pairs, 1) : # index 從1開始
        print(f"Top {i}: \'{director}\' & \'{actor}\' with {count} collaborations")

    print()

## Question 7. Top‐3 directors who collaborate with the most actors?
def Q7(dataset) :
    director_col_freq = {}

    for movie in dataset :
        director = movie["Director"].strip()
        director_col_freq[director] = 0 # initialization

    for director in list(director_col_freq.keys()) :
        actor_list = []
        
        for movie in dataset :

            if movie["Director"].strip() == director :
                actors = movie["Actors"].strip().split("|") 
                for actor in actors :
                    if actor not in actor_list :
                        actor_list.append(actor.strip())
                        director_col_freq[director] += 1

    Top_3_directors = sorted(director_col_freq.items(),key=lambda x : x[1], reverse=True)[:3]
    
    print("="*60)
    print("Question 7.")
    for i , (director,count) in enumerate(Top_3_directors, 1) :
        print(f"Top {i} is {director} with {count} collaborations.")

    print()

## Question 8. Top‐6 actors playing in the most genres of movies?
def Q8(dataset) :
    actor_genres = {}

    for movie in dataset :
        genres = movie["Genre"].strip().split("|")
        actors = movie["Actors"].strip().split("|")

        for actor in actors :
            if actor not in actor_genres :
                actor_genres[actor.strip()] = set()

            # Record actor playing in the genres of movies
            actor_genres[actor.strip()].update(genres)            

    # Calculate the frequency that actor playing in the genres of movies
    actor_genres_freq = {actor : len(genre) for actor, genre in actor_genres.items()}

    top_6_actors_with_most_genre = sorted(actor_genres_freq.items(), key=lambda x : x[1], reverse = True)[:6]
    
    print("="*60)
    print("Question 8.")
    for i, (actor, count) in enumerate(top_6_actors_with_most_genre, 1):
        print(f"Top {i}: \'{actor}\' with {count} genres !")
    
    print() 

## Question 9. Top‐3 actors whose movies lead to the largest maximum gap of years?
def Q9(dataset) :
    actors_gap_year = {}

    for movie in dataset :
        title = movie["Title"].strip()
        actors = movie["Actors"].strip().split("|")
        year = int(movie["Year"].strip())

        for actor in actors :
            if actors_gap_year.get(actor.strip()) == None :
                actors_gap_year[actor.strip()] = {title : year} # initialization
            else :
                actors_gap_year[actor.strip()].update({title : year})

    actor_max_gap_year = {}
    for actor in actors_gap_year :
        title_year_dict = actors_gap_year[actor]
        
        year_list = []
        for title in title_year_dict :
            year_list.append(title_year_dict[title])

        max_year = max(year_list)
        min_year = min(year_list)
        max_gap_year = max_year - min_year

        actor_max_gap_year[actor] = max_gap_year
    
    top_3_actors_with_largest_max_gap_year = sorted(actor_max_gap_year.items(), key=lambda x : x[1], reverse=True)[:3]
        
    print("="*60)
    print("Question 9.")

    for i, (actor,max_gap_year) in enumerate(top_3_actors_with_largest_max_gap_year,1) :
        print(f"Top {i} is \'{actor}\' with \'{max_gap_year}\'maximum gap of years")
    
    print()
    
if __name__=="__main__" :
    file_name = "C:/Users/yenwe/Desktop/H24116154_hw5/IMDB-Movie-Data.csv"
    dataset = open_csv_file(file_name)

    Q1(dataset)

    Q2(dataset)

    Q3(dataset)

    Q4(dataset)

    Q5(dataset)

    Q6(dataset)

    Q7(dataset)

    Q8(dataset)
    
    Q9(dataset)

