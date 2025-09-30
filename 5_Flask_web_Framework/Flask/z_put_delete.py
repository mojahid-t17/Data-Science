### put and delete http verbs
#working with API's --json

from flask import Flask,jsonify,request

app=Flask(__name__)

#initial data in my to do list
tasks=[
    {"id":1,"name":"item 1", "description":"this is item 1"},
    {"id":2,"name":"item 2", "description":"this is item 2"}
    
]

@app.route('/')
def home():
    return "welcome to the to do list app"

# GET: retrieve all the items
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(tasks)



#GET: retrieve specific itm by id
@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((task for task in tasks if task['id']==item_id),None)
    if item is None:
        return jsonify({"error:","item is not found"})
    return jsonify(item)


#post: create a new task
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item is not added"})
    new_item={
        "id":tasks[-1]['id']+1,
        "name":request.json['name'],
        "description":request.json['description']
    }
    tasks.append(new_item)
    return jsonify(new_item)
    
#PUT: update an exiting item
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item=next((task for task in tasks if task['id']==item_id),None)
    if item is None:
        return jsonify({"error":"item is not found"})
    item['name']=request.json.get('name',item['name'])
    item['description']=request.json.get('description',item['description'])
    return jsonify(item) 
#DELETE: delete and existing item
@app.route('/items/<int: item_id>',methods=['DELETE'])
def delete_item(item_id):
    global tasks
    item=[task for task in tasks if task['id'] !=item_id]
    return jsonify({"result": "item deleted"})
if __name__=="__main__":
    app.run(debug=True)
