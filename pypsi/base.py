from julia import Pandas, DataFrames

def convert_to_pandas(jl_dict):
    py_dict = {}
    for name in jl_dict:
        py_dict[name] = Pandas.DataFrame(jl_dict[name])
    return py_dict
