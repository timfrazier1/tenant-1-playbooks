"""
Pin domains that are younger than 15 days in the HUD.
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

##############################
# Start - Global Code Block

def is_ioc(value):
    import phantom.utils as phutils
    
    ioc_funcs = [phutils.is_ip, phutils.is_url, phutils.is_email, phutils.is_hash]
    for f in ioc_funcs:
        if f(value):
            return True, f.__name__.split('_')[1]
    return False, None


def pin_name_mangle(pin_name, container):
    return pin_name + '__{0}'.format(container['id'])

# End - Global Code block
##############################

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'whois_domain_1' block
    whois_domain_1(container=container)

    return

def whois_domain_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('whois_domain_1() called')

    # collect data for 'whois_domain_1' call
    container_data = phantom.collect2(container=container, datapath=['artifact:*.cef.destinationDnsDomain', 'artifact:*.id'])

    parameters = []
    
    # build parameters list for 'whois_domain_1' call
    for container_item in container_data:
        if container_item[0]:
            parameters.append({
                'domain': container_item[0],
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': container_item[1]},
            })

    phantom.act("whois domain", parameters=parameters, assets=['whois'], callback=Calculate_Domain_Age, name="whois_domain_1")

    return

def Calculate_Domain_Age(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('Calculate_Domain_Age() called')
    results_data_1 = phantom.collect2(container=container, datapath=['whois_domain_1:action_result.data.*.creation_date', 'whois_domain_1:action_result.parameter.domain'], action_results=results)
    results_item_1_0 = [item[0] for item in results_data_1]
    results_item_1_1 = [item[1] for item in results_data_1]

    Calculate_Domain_Age__domain_age = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    #phantom.debug(results_item_1_0)
    #phantom.debug(results_item_1_1)

    from datetime import datetime, timedelta
    
    all_domains_age = []
    
    for idx, val in enumerate(results_item_1_0):
        #Convert string to datetime object
        datetime_object = datetime.strptime(val[0], "%Y-%m-%dT%H:%M:%S")
        domain_age = datetime.strptime("2019-08-02T21:49:40", "%Y-%m-%dT%H:%M:%S") - datetime_object
        if  domain_age.days<15:      
            phantom.pin(container=container, message="Domain is less than 15 days old", data=results_item_1_1[idx], pin_type="card_medium", pin_style="red")
        else:
            pass
        
        #all_domains_age.append(domain_age)

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key='Calculate_Domain_Age:domain_age', value=json.dumps(Calculate_Domain_Age__domain_age))

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