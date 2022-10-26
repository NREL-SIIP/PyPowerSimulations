from pypsi.base import convert_to_pandas
from julia import Pandas, DataFrames
from julia import PowerSimulations as PSI

class SimulationProblemResults:
    def __init__(self, path, execution, problem, ignore_status=False):
        self.path = path
        self.execution = execution
        self.problem_name = problem
        self.jl_SimulationResults = PSI.SimulationResults(path)
        self.jl_SimulationProblemResults = PSI.get_decision_problem_results(self.jl_SimulationResults, self.problem_name)

    def get_model_name(self):
        return PSI.get_model_name(self.jl_SimulationProblemResults)

    def get_system(self):
        return PSI.get_system(self.jl_SimulationProblemResults)

    def get_resolution(self):
        return PSI.get_resolution(self.jl_SimulationProblemResults)

    def get_execution_path(self):
        return PSI.get_execution_path(self.jl_SimulationProblemResults)

    def get_timestamps(self):
        return PSI.get_timestamps(self.jl_SimulationProblemResults)

    def get_aux_variables(self):
        return convert_to_pandas(PSI.get_aux_variables(self.jl_SimulationProblemResults))

    def get_duals(self):
        return convert_to_pandas(PSI.get_duals(self.jl_SimulationProblemResults))

    def get_expressions(self):
        return convert_to_pandas(PSI.get_expressions(self.jl_SimulationProblemResults))

    def get_parameters(self):
        return convert_to_pandas(PSI.get_parameters(self.jl_SimulationProblemResults))

    def get_variables(self):
        return convert_to_pandas(PSI.get_variables(self.jl_SimulationProblemResults))

    def list_variable_names(self):
        return PSI.list_variable_names(self.jl_SimulationProblemResults)

    def list_parameter_names(self):
        return PSI.list_parameter_names(self.jl_SimulationProblemResults)

    def list_dual_names(self):
        return PSI.list_dual_names(self.jl_SimulationProblemResults)

    def list_aux_variable_names(self):
        return PSI.list_aux_variable_names(self.jl_SimulationProblemResults)

    def list_expression_names(self):
        return PSI.list_expression_names(self.jl_SimulationProblemResults)

    def list_variable_keys(self):
        return PSI.list_variable_keys(self.jl_SimulationProblemResults)

    def set_serialized(self):
        PSI.get_system_b(self.jl_SimulationProblemResults)
        return

    def set_system(self, system_path):
        PSI.set_system_b(self.jl_SimulationProblemResults)
        return
        
    # TODO: test if kwargs are passed correctly
    def read_realized_variables(self, **kwargs):
        return convert_to_pandas(PSI.read_realized_variables(self.jl_SimulationProblemResults, **kwargs))        

    def read_realized_variables(self, variables, **kwargs):
        return convert_to_pandas(PSI.read_realized_variables(self.jl_SimulationProblemResults, variables,  **kwargs))

    def read_realized_variable(self, variable, **kwargs):
        return convert_to_pandas(PSI.read_realized_variable(self.jl_SimulationProblemResults, variable,  **kwargs))

    def read_realized_aux_variables(self, **kwargs):
        return convert_to_pandas(PSI.read_realized_aux_variables(self.jl_SimulationProblemResults, **kwargs))        

    def read_realized_aux_variables(self, aux_variables, **kwargs):
        return convert_to_pandas(PSI.read_realized_aux_variables(self.jl_SimulationProblemResults, aux_variables,  **kwargs))

    def read_realized_aux_variable(self, aux_variable, **kwargs):
        return convert_to_pandas(PSI.read_realized_aux_variable(self.jl_SimulationProblemResults, aux_variable,  **kwargs))

    def read_realized_parameters(self, **kwargs):
        return PSI.read_realized_parameters(self.jl_SimulationProblemResults, **kwargs)        

    def read_realized_parameters(self, parameters, **kwargs):
        return convert_to_pandas(PSI.read_realized_parameters(self.jl_SimulationProblemResults, parameters,  **kwargs))

    def read_realized_aux_variable(self, parameter, **kwargs):
        return convert_to_pandas(PSI.read_realized_aux_variable(self.jl_SimulationProblemResults, parameter,  **kwargs))

    def read_realized_duals(self, **kwargs):
        return convert_to_pandas(PSI.read_realized_duals(self.jl_SimulationProblemResults, **kwargs))        

    def read_realized_duals(self, duals, **kwargs):
        return convert_to_pandas(PSI.read_realized_duals(self.jl_SimulationProblemResults, duals,  **kwargs))

    def read_realized_dual(self, dual, **kwargs):
        return convert_to_pandas(PSI.read_realized_dual(self.jl_SimulationProblemResults, dual,  **kwargs))

    def read_realized_expressions(self, **kwargs):
        return convert_to_pandas(PSI.read_realized_expressions(self.jl_SimulationProblemResults, **kwargs))

    def read_realized_expressions(self, expressions, **kwargs):
        return convert_to_pandas(PSI.read_realized_expressions(self.jl_SimulationProblemResults, expressions,  **kwargs))

    def read_realized_expression(self, expression, **kwargs):
        return convert_to_pandas(PSI.read_realized_expression(self.jl_SimulationProblemResults, expression,  **kwargs))

    def export_realized_results(self,):
        return PSI.export_realized_results(self.jl_SimulationProblemResults)

    def export_realized_results(self, save_path):
        return PSI.export_realized_results(self.jl_SimulationProblemResults, save_path)

    def export_optimizer_stats(self, directory, format="csv"):
        return PSI.export_optimizer_stats(self.jl_SimulationProblemResults, directory, format)


