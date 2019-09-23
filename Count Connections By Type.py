"""
Count connections by type and pin the results on the HUD. The connections are detected by Volatility.
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'list_connections_1' block
    list_connections_1(container=container)

    return

def list_connections_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('list_connections_1() called')

    # collect data for 'list_connections_1' call

    parameters = []
    
    # build parameters list for 'list_connections_1' call
    parameters.append({
        'profile': "",
        'vault_id': "0dd6d441d8fca241d3970cef6a5d333379d43c29",
    })

    phantom.act("list connections", parameters=parameters, assets=['volatility bots'], callback=list_connections_1_callback, name="list_connections_1")

    return

def list_connections_1_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('list_connections_1_callback() called')
    
    filter_1(action=action, success=success, container=container, results=results, handle=handle)
    filter_2(action=action, success=success, container=container, results=results, handle=handle)
    filter_3(action=action, success=success, container=container, results=results, handle=handle)
    filter_4(action=action, success=success, container=container, results=results, handle=handle)

    return

def filter_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('filter_1() called')

    # collect filtered artifact ids for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        action_results=results,
        conditions=[
            ["list_connections_1:action_result.data.*.state", "==", "WHAT_STATE"],
        ],
        name="filter_1:condition_1")

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        pin_4(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return

def pin_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('pin_4() called')

    filtered_results_data_1 = phantom.collect2(container=container, datapath=["filtered-data:filter_1:condition_1:list_connections_1:action_result.data.*.state"])
    
    phantom.debug(filtered_results_data_1)

    #filtered_results_item_1_0 = [item[0] for item in filtered_results_data_1]
    filtered_results_item_1_0 = len(filtered_results_data_1)

    phantom.pin(container=container, data=filtered_results_item_1_0, message="Number of LISTENING connections", pin_type="card", pin_style="blue", name=None)

    return

def filter_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('filter_2() called')

    # collect filtered artifact ids for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        action_results=results,
        conditions=[
            ["list_connections_1:action_result.data.*.state", "==", "WHAT_STATE"],
        ],
        name="filter_2:condition_1")

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        pin_5(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return

def filter_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('filter_3() called')

    # collect filtered artifact ids for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        action_results=results,
        conditions=[
            ["list_connections_1:action_result.data.*.state", "==", "WHAT_STATE"],
        ],
        name="filter_3:condition_1")

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        pin_6(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return

def filter_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('filter_4() called')

    # collect filtered artifact ids for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        action_results=results,
        conditions=[
            ["list_connections_1:action_result.data.*.state", "==", "WHAT_STATE"],
        ],
        name="filter_4:condition_1")

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        pin_7(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return

def pin_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('pin_5() called')

    filtered_results_data_1 = phantom.collect2(container=container, datapath=["filtered-data:filter_2:condition_1:list_connections_1:action_result.data.*.state"])

    #filtered_results_item_1_0 = [item[0] for item in filtered_results_data_1]
    filtered_results_item_1_0 = len(filtered_results_data_1)

    phantom.pin(container=container, data=filtered_results_item_1_0, message="Number of CLOSED connections", pin_type="card", pin_style="red", name=None)

    return

def pin_6(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('pin_6() called')

    filtered_results_data_1 = phantom.collect2(container=container, datapath=["filtered-data:filter_3:condition_1:list_connections_1:action_result.data.*.state"])

    #filtered_results_item_1_0 = [item[0] for item in filtered_results_data_1]
    filtered_results_item_1_0 = len(filtered_results_data_1)

    phantom.pin(container=container, data=filtered_results_item_1_0, message="Number of ESTABLISHED connections", pin_type="card", pin_style="grey", name=None)

    return

def pin_7(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('pin_7() called')

    filtered_results_data_1 = phantom.collect2(container=container, datapath=["filtered-data:filter_4:condition_1:list_connections_1:action_result.data.*.state"])

    #filtered_results_item_1_0 = [item[0] for item in filtered_results_data_1]
    filtered_results_item_1_0 = len(filtered_results_data_1)

    phantom.pin(container=container, data=filtered_results_item_1_0, message="Number of CLOSED_WAIT connections", pin_type="card", pin_style="red", name=None)

    return

def on_finish(container, summary):
    phantom.debug('on_finish() called')
    # This function is called after all actions are completed.
    # summary of all the action and/or all detals of actions 
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    return