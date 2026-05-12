def noteEntity(item)-> dict:
 return{
  "id": str(item["_id"]),
  "title": item["Title"],
  "description": item["Description"],
  "highpriority": item["highpriority"]
        }

def notesEntity(items)-> list:
 return [noteEntity(item) for item in items]