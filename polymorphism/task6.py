class Language:

    def __init__(self, level: str, type: str) -> None:
        self.level = level
        self.type = type


class Python(Language):

    def write_function(self, func_name: str, arg: str) -> str:
        return f"def {func_name}({arg}):"


    def create_variable(self, var_name: str, value) -> str:
        if type(value) is str:
            return f"{var_name} = '{value}'"

        return f"{var_name} = {value}"


class JavaScript(Language):

    def write_function(self, func_name: str, arg: str) -> str:
        return f"function {func_name}({arg}) {{     }};"


    def create_variable(self, var_name: str, value) -> str:
        if type(value) is str:
            return f"let {var_name} = '{value}';" 

        return f"let {var_name} = {value};"


py = Python("high-level", "interpreted")
print(py.write_function('get_code', 'a')) 
print(py.create_variable('name', 'John'))

js = JavaScript("high-level", "interpreted")
print(js.write_function('validate', 'form'))
print(js.create_variable('password', 'john@123'))
