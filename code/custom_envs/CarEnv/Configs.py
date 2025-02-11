from copy import deepcopy


VEH_2CV = {
    'type': 'simple',
    'wheelbase': 2.4,
    'mass': 700.,
    'inertia': 812., # Approximated by 0.1269*m*R*L according to "Approximation von Trägheitsmomenten bei Personenkraftwagen", Burg, 1982
    'engine_power': 20 * 1000,
    'brake_force': 5100.,
    'brake_balance': .5,
    'max_grip': 1.2,
    'rwd': False,
}

RACING = {
    'action': {'type': 'continuous_steering_pedals'},
    'longitudinal': {'type': 'simple'},
    'steering': 'direct()',
    'collision_bb': (-3.81 / 2, 3.81 / 2, -1.48 / 2, 1.48 / 2),
    'vehicle': VEH_2CV,
    'problem': {'type': 'racing', 'track_width': 8., 'cone_width': 7., 'k_forwards': .1, 'k_base': .0, 'extend': 150, 'time_limit': 60.},
    'dt': .1,
    'physics_divider': 10,
    'sensors': {
        #'cones_set': {
        #    'type': 'conemap',
        #    'bbox': (-15, 45, -30, 30),
        #},
        'track_points': {
            'type': 'trackpoints'
        },
        'controller_metrics': {
            'type': 'ctrl_metrics'
        }
    }
}

RACING_FAST = deepcopy(RACING)
RACING_FAST['vehicle']['engine_power'] = 60. * 1000
RACING_FAST['vehicle']['brake_force'] = 7500 #9400.  # 9000  # 7900.
RACING_FAST['vehicle']['max_grip'] = 0.7 #1.4  # .9  # .725
RACING_FAST['vehicle']['max_grip_opt'] = 1.5 #2.8  # 1.8  # 1.55
# TODO: Note that this line has been commented out!!!
# RACING_FAST['sensors']['cones_set']['bbox'] = (-15, 60, -35, 35) #(-18, 75, -35, 35)  # (-15, 60, -30, 30)
RACING_FAST['steering'] = 'linear(60)' #'linear(80)'


_STANDARD_ENVS = {
    'racing': RACING_FAST,
}


def get_standard_env_config(name):
    return deepcopy(_STANDARD_ENVS[name])


def get_standard_env_names():
    return list(_STANDARD_ENVS.keys())
