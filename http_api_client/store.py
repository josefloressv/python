import requests

def get_categories():
    response = requests.get("https://api.escuelajs.co/api/v1/categories")
    print(response.status_code)
    # print(response.text)
    # print(response.json())
    print(type(response.text)) # <class 'str'>
    print(type(response.json())) # <class 'list'> this can be iterated
    categories = response.json()
    for category in categories:
        # print(category)
        print(category['name'])
    # return response.json()