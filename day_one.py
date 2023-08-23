import requests

def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars} "

    for language in languages:
        query += f"language:{language} "

    # a sample query looks like: "stars:>50 language:python language:javascript"
    return query

def repos_with_most_stars(languages, sort="stars", order="desc"):
    gh_api_repo_search_url = "https://api.github.com/search/repositories"
    
    query = create_query(languages)
    sort = "stars"
    order = "desc"
    parameters = {"q": query, "sort": sort, "order": order}
    response = requests.get(gh_api_repo_search_url, params=parameters)

    status_code = response.status_code
    if status_code != 200:
        raise RuntimeError(f"An error occurred. HTTP Code: {status_code}.")
    else:
        response_json = response.json()["items"]
        return response_json

# have a main method 
if __name__ == "__main__":
    languages = ["python", "javascript", "ruby"]
 
    results = repos_with_most_stars(languages)
    
    

    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]
        # make sure that the print statement is in the for loop to print the result for each repo
        print(f"-> {name} is a {language} repo with {stars} stars.")