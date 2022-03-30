import json
json_path='D:/data/COCO Data/annotations_trainval2017/annotations/instances_val2017.json'
json_labels=json.load(open(json_path,'r'))
print(json_labels['info'])