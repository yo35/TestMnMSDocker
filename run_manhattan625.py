###############
### Imports ###
###############
## Casuals
import pathlib
import time
import numpy as np

## MnMS
from mnms.generation.roads import generate_manhattan_road
from mnms.generation.layers import generate_layer_from_roads, generate_grid_origin_destination_layer
from mnms.generation.demand import generate_random_demand
from mnms.graph.layers import MultiLayerGraph
from mnms.demand.manager import CSVDemandManager
from mnms.log import set_all_mnms_logger_level, LOGLEVEL
from mnms.travel_decision.dummy import DummyDecisionModel
from mnms.mobility_service.personal_vehicle import PersonalMobilityService
from mnms.flow.MFD import MFDFlowMotor, Reservoir
from mnms.simulation import Supervisor
from mnms.time import Time, Dt
from mnms.tools.observer import CSVUserObserver, CSVVehicleObserver

##################
### Parameters ###
##################
log_file = pathlib.Path(__file__).parent.joinpath('sim.log').resolve()

n_nodes_per_dir = 25
mesh_size = 100 # m
n_odnodes_x = 25
n_odnodes_y = 25
odlayer_xmin = 0
odlayer_ymin = 0
odlayer_xmax = 2500 # m
odlayer_ymax = 2500 # m
odlayer_connection_dist = 1e-3 # m

nb_user=10000
tstart = "07:00:00"
tend = "11:00:00"
dt_flow = Dt(minutes=1)
affectation_factor = 10

def mfdspeed(dacc):
    dspeed = {'CAR': 3} # m/s
    return dspeed


#########################
### Scenario creation ###
#########################

#### RoadDescriptor ####
road_db = generate_manhattan_road(n_nodes_per_dir, mesh_size) # one zone automatically generated

#### MlGraph ####
personal_car = PersonalMobilityService()
car_layer = generate_layer_from_roads(road_db,
                                      'CAR',
                                      mobility_services=[personal_car])

odlayer = generate_grid_origin_destination_layer(odlayer_xmin, odlayer_ymin, odlayer_xmax,
    odlayer_ymax, n_odnodes_x, n_odnodes_y)

mlgraph = MultiLayerGraph([car_layer],
                          odlayer,
                          odlayer_connection_dist)

#### Demand ####
demand = generate_random_demand(mlgraph,
                           nb_user,
                           tstart,
                           tend,
                           min_cost=0,
                           cost_path=None,
                           distrib_time=np.random.uniform,
                           repeat=1)

#### Decision model ####
decision_model = DummyDecisionModel(mlgraph)

#### Flow motor ####
flow_motor = MFDFlowMotor()
flow_motor.add_reservoir(Reservoir(road_db.zones["RES"], 'CAR', mfdspeed))

#### Supervisor ####
supervisor = Supervisor(mlgraph,
                        demand,
                        flow_motor,
                        decision_model,
                        logfile=log_file,
                        loglevel=LOGLEVEL.WARNING)

######################
### Run simulation ###
######################

set_all_mnms_logger_level(LOGLEVEL.WARNING)

st = time.time()
supervisor.run(Time(tstart),
               Time(tend),
               dt_flow,
               affectation_factor,
               seed=123)
print(f'Run time = {time.time() - st}')
