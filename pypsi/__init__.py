def initialize_julia_session(custom_jl_env="."):
    try:
        import julia
    except ImportError as e:
        pass

    from julia.api import Julia
    jl = Julia(compiled_modules=False)

    from julia import Pkg
    Pkg.activate(custom_jl_env)
    Pkg.instantiate()
    return jl

initialize_julia_session()
from julia import Pandas, DataFrames
from julia import PowerSimulations as PSI

from pypsi.simulation_results import SimulationResults
from pypsi.simulation_problem_results import SimulationProblemResults
from pypsi.problem_results import ProblemResults
