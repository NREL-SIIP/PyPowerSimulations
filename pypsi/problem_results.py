from pypsi.base import convert_to_pandas
from julia import Pandas, DataFrames
from julia import PowerSimulations as PSI

class ProblemResults:
    def __init__(path):
        self.path = path
        self.jl_ProblemResults = PSI.ProblemResults(path)
        
    def read_variable(self, **kwargs):
        return convert_to_pandas(PSI.read_variable(self.jl_ProblemResults, **kwargs))

    def read_variables(self, variables, **kwargs):
        return convert_to_pandas(PSI.read_variable(self.jl_ProblemResults, variables, **kwargs))

    def read_dual(self, **kwargs):
        return convert_to_pandas(PSI.read_dual(self.jl_ProblemResults, **kwargs))

    def read_duals(self, duals, **kwargs):
        return convert_to_pandas(PSI.read_duals(self.jl_ProblemResults, duals, **kwargs))

    def read_parameter(self, **kwargs):
        return convert_to_pandas(PSI.read_parameter(self.jl_ProblemResults, **kwargs))

    def read_parameters(self, parameters, **kwargs):
        return convert_to_pandas(PSI.read_parameters(self.jl_ProblemResults, parameters, **kwargs))

    def read_aux_variable(self, **kwargs):
        return convert_to_pandas(PSI.read_aux_variable(self.jl_ProblemResults, **kwargs))

    def read_aux_variables(self, aux_variables, **kwargs):
        return convert_to_pandas(PSI.read_aux_variables(self.jl_ProblemResults, aux_variables, **kwargs))

    def read_expression(self, **kwargs):
        return convert_to_pandas(PSI.read_expression(self.jl_ProblemResults, **kwargs))

    def read_expressions(self, expressions, **kwargs):
        return convert_to_pandas(PSI.read_expressions(self.jl_ProblemResults, expressions, **kwargs))

    def export_realized_results(self):
        return PSI.export_realized_results(self)
