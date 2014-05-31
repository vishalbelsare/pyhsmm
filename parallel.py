from __future__ import division
import numpy as np

def _get_stats(model,grp):
    datas, kwargss = zip(*grp)

    mb_states_list = []
    for data, kwargs in zip(datas,kwargss):
        model.add_data(data,stateseq=np.empty(data.shape[0]),**kwargs)
        mb_states_list.append(model.states_list.pop())

    for s in mb_states_list:
        s.meanfieldupdate()

    return [s.all_expected_stats for s in mb_states_list]

