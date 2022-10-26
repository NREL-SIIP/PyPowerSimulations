from pypsi.base import convert_to_pandas
from julia import Pandas, DataFrames
from julia import Main
from julia import PowerSimulations as PSI

class SimulationProblemResults:
    def __init__(self, path, problem, execution=1, ignore_status=False):
        self.path = path
        self.execution = execution
        self.problem_name = problem
        self.jl_SimulationResults = PSI.SimulationResults(path, execution, ignore_status=ignore_status)
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
    def read_realized_variables(self, variables=Main.nothing, start_time=Main.nothing, len=Main.nothing):
        if variables is Main.nothing:
            return convert_to_pandas(PSI.read_realized_variables(self.jl_SimulationProblemResults, start_time=start_time, len=len))        
        else:
            return convert_to_pandas(PSI.read_realized_variables(self.jl_SimulationProblemResults, variables, start_time=start_time, len=len)) 
        

    def read_realized_variable(self, variable, start_time=Main.nothing, len=Main.nothing):
        return convert_to_pandas(PSI.read_realized_variable(self.jl_SimulationProblemResults, variable,  start_time=start_time, len=len))
     

    def read_realized_aux_variables(self, aux_variables=Main.nothing, start_time=Main.nothing, len=Main.nothing):
        if aux_variables is Main.nothing:
            return convert_to_pandas(PSI.read_realized_aux_variables(self.jl_SimulationProblemResults, start_time=start_time, len=len))
        else:
            return convert_to_pandas(PSI.read_realized_aux_variables(self.jl_SimulationProblemResults, aux_variables, start_time=start_time, len=len)) 
        

    def read_realized_aux_variable(self, aux_variable, start_time=Main.nothing, len=Main.nothing):
        return convert_to_pandas(PSI.read_realized_aux_variable(self.jl_SimulationProblemResults, aux_variable,  start_time=Main.nothing, len=Main.nothing))

    def read_realized_parameters(self, parameters=Main.nothing, start_time=Main.nothing, len=Main.nothing):
        if parameters is Main.nothing:
            return convert_to_pandas(PSI.read_realized_parameters(self.jl_SimulationProblemResults, start_time=start_time, len=len))
        else:
            return convert_to_pandas(PSI.read_realized_parameters(self.jl_SimulationProblemResults, parameters, start_time=start_time, len=len)) 
        

    def read_realized_aux_variable(self, parameter=Main.nothing, start_time=Main.nothing, len=Main.nothing):
        return convert_to_pandas(PSI.read_realized_aux_variable(self.jl_SimulationProblemResults, parameter,  start_time=start_time, len=len))

    def read_realized_duals(self, duals=Main.nothing, start_time=Main.nothing, len=Main.nothing):
        if duals is Main.nothing:
            return convert_to_pandas(PSI.read_realized_duals(self.jl_SimulationProblemResults, start_time=start_time, len=len))
        else:
            return convert_to_pandas(PSI.read_realized_duals(self.jl_SimulationProblemResults, duals, start_time=start_time, len=len)) 
        

    def read_realized_dual(self, dual=Main.nothing, start_time=Main.nothing, len=Main.nothing):
        return convert_to_pandas(PSI.read_realized_dual(self.jl_SimulationProblemResults, dual,  start_time=start_time, len=len))

    def read_realized_expressions(self, expressions=Main.nothing, start_time=Main.nothing, len=Main.nothing):
        if expressions is Main.nothing:
            return convert_to_pandas(PSI.read_realized_expressions(self.jl_SimulationProblemResults, start_time=start_time, len=len))
        else:
            return convert_to_pandas(PSI.read_realized_expressions(self.jl_SimulationProblemResults, expressions, start_time=start_time, len=len)) 

    def read_realized_expression(self, expression=Main.nothing, start_time=Main.nothing, len=Main.nothing):
        return convert_to_pandas(PSI.read_realized_expression(self.jl_SimulationProblemResults, expression,  start_time=start_time, len=len))

    def export_realized_results(self, save_path):
        return PSI.export_realized_results(self.jl_SimulationProblemResults, save_path)

    def export_optimizer_stats(self, directory, format="csv"):
        return PSI.export_optimizer_stats(self.jl_SimulationProblemResults, directory, format)


