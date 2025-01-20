## ⚡ **Challenge 3: Lambda Expressions**
##* Write a function to sort a list of dictionaries by a specific key using a lambda expression, sort by an optional secondary key if the primary key is equal.
##* Expected function: `sort_by_key(data: list[dict], key: str, secondary_key = '') -> list[dict]`.

def sort_by_key(data: list[dict], key: str, secondary_key = '') -> list[dict]:
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Elements in the data should be dictionaries")
    if secondary_key:
        return sorted(data, key=lambda x: (x.get(key, None), x.get(secondary_key, None)))
    else:
        return sorted(data, key=lambda x: x.get(key, None))

##Test   
if __name__ == "__main__":
    data = [
        {"Name": "Simon", "Age": 29, "Score": 10},
        {"Name": "Laura", "Age": 30, "Score": 90},
        {"Name": "David", "Age": 32, "Score": 70},
        {"Name": "Angela", "Age": 31, "Score": 40}
    ]
    print(sort_by_key(data, "Name", "Age"))