bookstore = { 
    "author name":{
        "name": "author name",
        "birth_year": 1970,
        "genres": ["genre1", "genre2"],
        "books": [
            {
                "name": "book name",
                "isbn": "book isbn",
                "year": 2025,
                "genre": "genre1",
                "publisher": "penguin",
            },
            {
                "name": "book name 2",
                "isbn": "book isbn 2",
                "year": 2023,
                "genre": "genre 2",
                "publisher": "penguin"
            }
        ]
    }
}

def LookUp(Data):
    Searched = []
    Filters = []
    Parents = []
    Selected = Data
    while True:
        print(type(Selected))
        if isinstance(Selected, dict) and Selected not in Searched:  
            Searched.append(Selected)
            Parents.append(Selected)
            for i in Selected.keys():
                if i not in Filters:
                    Filters.append(i)
            Selected = Selected.keys()
        if isinstance(Selected, list) and Selected not in Searched:
            Parents.append(Selected)
            for element in Selected:
                if isinstance(Selected,dict):
                    Selected = element
        else:
            Selected = Parents[:0]
            Parents.remove(Parents[:0])
    
LookUp(bookstore)