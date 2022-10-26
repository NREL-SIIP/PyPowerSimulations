from pypsi.simulation_problem_results import SimulationProblemResults

from julia import Pandas, DataFrames
from julia import PowerSimulations as PSI

class SimulationResults:
    def __init__(self, path, execution = 1, ignore_status=False):
        self.path = path
        self.execution = execution
        self.ignore_status = ignore_status
        self.jl_SimulationResults = PSI.SimulationResults(path, execution, ignore_status = ignore_status)

    def get_decision_problem_results(self, model_name):
        return SimulationProblemResults(self.path, self.execution, model_name, self.ignore_status)

    def get_emulation_problem_results(self):
        return PSI.get_emulation_problem_results(self.jl_SimulationResults)

    def list_decision_problems(self):
        return PSI.list_decision_problems(self.jl_SimulationResults)

    def export_results(self, exports):
        return PSI.export_results(self.jl_SimulationResults, exports)
