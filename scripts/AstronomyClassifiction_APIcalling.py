# Dependencies
import os
import pip._vendor.requests as requests


def APIcalling():
    # Set base URL for search
    API_url = "https://images-api.nasa.gov"

    # Set search query
    queries = [
                "galaxy", 
            "nebulae"]

    # Set output directory
    for query in queries:
        output_directory = r"project_root/raw/"+ query + "_images" # Directory where to save the images, create several subdirectories depending on the query

        # Create output directory if it doesn't exist
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Set search URL with query parameter
        search_url = API_url + "/search?q=" + query 

        # Send GET request to search URL
        response = requests.get(search_url, params = {"media_type" : "image"})

        # Find all image links in search results
        image_links = response.json()["collection"]["items"]

        # Download images
        for link in image_links:
            image_thumb = link["links"][0]["href"]
            nasa_id = link["data"][0]["nasa_id"]
            image_orig = image_thumb.replace("~thumb","~orig")

            image_data = requests.get(image_orig).content
            with open(output_directory+"/"+nasa_id+".jpg", 'wb') as handler:
                handler.write(image_data)

if __name__ == "__main__":
    APIcalling()


