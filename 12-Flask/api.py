### Put and delete - Http methods(verbs )
### Working with api's -- Json

from flask import Flask, request,jsonify
app=Flask(__name__)

# initial data in my todo list
items = [
    {"id":1, "name":"Buy groceries","description":"Milk, Bread, Eggs"},
    {"id":2, "name":"Read a book","description":"Fiction book"},
]


@app.route("/")
def home():
    return "Welcome to my Todo list API"

#Get retrive all items
@app.route("/items",methods=["GET"])
def get_items():
    return jsonify(items)

## Get retrive single item(Specific item) by id
@app.route("/items/<int:item_id>",methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    return jsonify(item)

## Post : create a new item - API
@app.route("/items",methods=["POST"])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"Item not found"})
    new_item= {
        "id":items[-1]["id"]+1 if items else 1,
        "name":request.json["name"],
        "description":request.json["description"]
    }    
    items.append(new_item)
    return jsonify(new_item)

## Put : update an existing item
@app.route("/items/<int:item_id>",methods=["PUT"])
def update_item(item_id):
    item = next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    item['name'] = request.json.get('name',item['name'])
    item['description']= request.json.get('description',item['description'])
    return jsonify(item)

## Delete : delete an existing item
@app.route("/items/<int:item_id>",methods=["DELETE"])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id']!=item_id]
    return jsonify({"message":"Item deleted successfully"})

if __name__=="__main__":
    app.run(debug=True)

