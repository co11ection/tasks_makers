class MyDict(dict):

    def get(self, *args):
        value = super().get(*args)

        if value:
            return value

        return "Are you kidding?"


obj_dict = MyDict({"some_title": 2}) 

print(obj_dict.get("some")) 
