SORT_OPTION = {
    "oldest":{ 
        "keyword": "created_at", 
        "label": "Oldest" },
    "latest":{ 
        "keyword": "-created_at", 
        "label": "Latest" },
    "deadline":{ 
        "keyword": "due_date", 
        "label": "Deadline" },
    "a-z":{  
        "keyword": "title", 
        "label": "a-z" },
    "z-a":{  
        "keyword": "-title", 
        "label": "z-a" },
}

DEFAULT_SORT = "created_at"
