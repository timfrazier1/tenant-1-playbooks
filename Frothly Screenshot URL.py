"""
Playbook to get Screenshot of a URL that is not whitelisted
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'filter_1' block
    filter_1(container=container)

    return

def detonate_url_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('detonate_url_1() called')

    # collect data for 'detonate_url_1' call
    filtered_artifacts_data_1 = phantom.collect2(container=container, datapath=['filtered-data:filter_1:condition_1:artifact:*.cef.requestURL', 'filtered-data:filter_1:condition_1:artifact:*.id'])

    parameters = []
    
    # build parameters list for 'detonate_url_1' call
    for filtered_artifacts_item_1 in filtered_artifacts:
        if filtered_artifacts_item_1[0]:
            parameters.append({
                'url': filtered_artifacts_item_1[0],
                'private': True,
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': filtered_artifacts_item_1[1]},
            })

    phantom.act("detonate url", parameters=parameters, assets=['frothly_urlscan'], callback=get_screenshot_1, name="detonate_url_1")

    return

def filter_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('filter_1() called')

    # collect filtered artifact ids for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["artifact:*.cef.requestURL", "!=", ""],
        ],
        name="filter_1:condition_1")

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        success, message, domains = phantom.get_list(list_name='Domain Whitelist', column_index=0)

        phantom.debug(
        'phantom.get_list results: success: {}, message: {}, Domains: {}'.format(success, message, domains)
        )
        domains = [str(n[0]) for n in domains if n]
        phantom.debug(domains)
        matches = []
        container_data = phantom.collect2(container=container, datapath=['filtered-data:filter_1:condition_1:artifact:*.cef.requestURL', 'filtered-data:filter_1:condition_1:artifact:*.id'])
        for container_item in container_data:
            phantom.debug(container_item)
            if any(n in container_item[0] for n in domains):
                phantom.debug(container_item[0])
                continue
            else:
                matches.append(container_item)
            
        phantom.debug(matches)
        matched_artifacts_1 = matches

        detonate_url_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return

def get_screenshot_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('get_screenshot_1() called')
    
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'get_screenshot_1' call
    results_data_1 = phantom.collect2(container=container, datapath=['detonate_url_1:action_result.parameter.url', 'detonate_url_1:action_result.parameter.context.artifact_id'], action_results=results)

    parameters = []
    
    # build parameters list for 'get_screenshot_1' call
    for results_item_1 in results_data_1:
        if results_item_1[0]:
            parameters.append({
                'uuid': results_item_1[0],
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': results_item_1[1]},
            })

    phantom.act("get screenshot", parameters=parameters, assets=['frothly_urlscan'], name="get_screenshot_1", parent_action=action)

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