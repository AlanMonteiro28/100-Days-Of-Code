import requests

API_URL = "https://api.npoint.io/674f5423f73deab1e9a7"


class Post:

    def __init__(self):
        self.posts = requests.get(API_URL).json()

    def get_posts(self):
        return self.posts
    
    def get_image(self, id):
        image = self.posts[id]["image_url"]
        return image