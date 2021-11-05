#Python script for query RRU radios via ENM CLI
#usage: python RRU_query.py {technology] {site name} {cell or GSM sector / TRX number }
#Technology: 5G LTE 3G 2G
#example Cell name for WCMDA: S1C1
#example GSM Sector and TRX: 1-1
#V1.0 5th November 2021

import enmscripting
import re
import sys

def check_radio(op_state1,product_data1):
    if op_state1 == 'ENABLED':
       product_data1 = product_data1.replace('{','')
       product_data1 = product_data1.replace('}','')
       product_data1 = ' ' + product_data1
       p1 = product_data1.split(',')
       #this for cycle is needed because the serial number can be in variated position in the printout list 
       for serialNum in p1:
           if 'serialNumber' in serialNum:
               serialNum2 = serialNum
       p1_serial = serialNum2.split('=')  
       x = 'NOT FOUND_IN_DATABASE;NOT_FOUND_IN_DATABASE' #needs this trick if the radio is not listed in the csv file
       with open('/home/shared/common/data_collections/SSC_RU_list.csv') as temp_f:
            datafile = temp_f.readlines()
       for line in datafile:
            if p1_serial[1] in line:
               x = line
       x1 = x.split(';')
       print('--------------------------------------------------------------------------')
       if tech == '2G':
          print('Site name: ',site,' GSM sector - TRX number: ',cell,' RAT:',tech)
       else:
          print('Site name: ',site,' cell name: ',cell,' RAT:',tech)
       print('Radio opereational state is:',op_state1,' - it is connected phyisically')
       print('Radio physical connection is: ',x1[1])
       for x2 in p1:
           print(x2)
       print('--------------------------------------------------------------------------')
    else:
       print('--------------------------------------------------------------------------')
       print('The RRU is disabled, fix the physical connecntion and repeat the query!')
       print('--------------------------------------------------------------------------')
       
def fetch_MO(mo_to_search,mo_class):
    x = mo_to_search.split(', ') #These lines are needed if mo_to_search is a list e.g rfbranch list
    mo_to_search = x[0] #These lines are needed if mo_to_search is a list e.g rfbranch list
    search1 = mo_class + '=.*([A-Z]|[a-z]|[0-9])' 
    result = re.search(search1,mo_to_search)
    return(result.group(0))
           

def open_session_ENM(cmds_list,fetch_list,elements_list,response_group):
    session = enmscripting.open('<ENM Launcher URL>').with_credentials(enmscripting.UsernameAndPassword('user','pass'))
    e_count = 0
    param1 = site
    param2 = cell
    if tech == "2G":
       param3 = cell.split("-") #This param is needed if GSMsector and TRX given e.g 1-0
    else:
       param3 = ['1','1'] #just for dummy - if tech in is not GSM it can be anything
    for c1 in cmds_list:        
        c1 = c1.replace('SITENAME',param1)
        c1 = c1.replace('PARAMETER',param2)
        c1 = c1.replace('SEC_ID',param3[0]) #This needs also in case of first command in case of GSM query
        c1 = c1.replace('TRX_ID',param3[1]) #This needs also in case of first command in case of GSM query
        cmd = session.command()
        response = cmd.execute(c1)
        e = response_group[e_count]
        e1 = int(e)
        fetch1 = fetch_list[e_count] 
        for element in response.get_output().groups()[e1]:
            b = elements_list[e_count]
            b = int(b)  
            x = str(element[b])
        y = fetch_MO(x,fetch1)
        y1 = y.split('=')
        param2 = y1[1]
        e_count = e_count + 1
    #common parts below     
    y = 'cmedit get '+ param1 + ' RfBranch.(rfBranchId=='+param2+',rfPortRef) -t'
    response = cmd.execute(y)
    for element in response.get_output().groups()[0]:
        x = str(element[5])
    y = fetch_MO(x,'FieldReplaceableUnit')
    y1 = y.split(',')
    x = y1[0]
    z = x.split('=')
    y = 'cmedit get '+ param1 + ' FieldReplaceableUnit.(FieldReplaceableUnitId==' + z[1] + ',ProductData,operationalState) -t'
    cmd = session.command()    
    response = cmd.execute(y)
    for element in response.get_output().groups()[0]:         
        op_state = str(element[4])
        product_data = str(element[5])     
    enmscripting.close(session)
    check_radio(op_state,product_data)


    #Commands for 5G query
cmds_5G = ['cmedit get SITENAME NrCellDu.(nRCellDUId==PARAMETER,nRSectorCarrierRef) -t',
           'cmedit get SITENAME NRSectorCarrier.(nRSectorCarrierId==PARAMETER,sectorEquipmentFunctionRef) -t',
           'cmedit get SITENAME SectorEquipmentFunction.(sectorEquipmentFunctionId==PARAMETER,rfBranchRef) -t']
response_group_5G = ['0','0','0'] #needs to tell the program which printouts are needed from ENM - because WCDMA has two groups printouts
#MO classes for 5G, input for fetch_MO definition          
fetch_5G = ['NRSectorCarrier','SectorEquipmentFunction','RfBranch']
#Which elements to fetch in the printout from ENM
elements_5G = ['4','4','3'] #Info to which elements need to fetch from printout

#Similar to 5G query part, but this is for LTE
cmds_LTE = ['cmedit get SITENAME EUtranCellFDD.(eUtranCellFDDId==PARAMETER,sectorCarrierRef) -t',
            'cmedit get SITENAME SectorCarrier.(sectorCarrierId==PARAMETER,sectorFunctionRef) -t',
            'cmedit get SITENAME SectorEquipmentFunction.(sectorEquipmentFunctionId==PARAMETER,rfBranchRef) -t']

fetch_LTE = ['SectorCarrier','SectorEquipmentFunction','RfBranch']
elements_LTE = ['4','4','3']
response_group_LTE = ['0','0','0']
           
cmds_3G = ['cmedit get SITENAME NodeBLocalCell.(NodeBLocalCellId==PARAMETER),NodeBSectorCarrier.(sectorEquipmentFunctionRef) -t',
           'cmedit get SITENAME SectorEquipmentFunction.(sectorEquipmentFunctionId==PARAMETER,rfBranchRef) -t']
fetch_3G = ['SectorEquipmentFunction','RfBranch']
elements_3G = ['5','3']
response_group_3G = ['1','0']

cmds_2G = ['cmedit get SITENAME GsmSector.(GsmSectorId==SEC_ID),Trx.(TrxId==TRX_ID,sectorEquipmentFunctionRef) -t',
           'cmedit get SITENAME SectorEquipmentFunction.(sectorEquipmentFunctionId==PARAMETER,rfBranchRef) -t']
           
fetch_2G = ['SectorEquipmentFunction','RfBranch']
elements_2G = ['4','3']
response_group_2G = ['1','0']


if len(sys.argv) == 4:
   tech = sys.argv[1]
   site = sys.argv[2]
   cell = sys.argv[3]
   if tech == '5G':
      open_session_ENM(cmds_5G,fetch_5G,elements_5G,response_group_5G)
   if tech == 'LTE' or tech == '4G':
      open_session_ENM(cmds_LTE,fetch_LTE,elements_LTE,response_group_LTE)
   if tech == 'WCDMA' or tech == '3G':
      open_session_ENM(cmds_3G,fetch_3G,elements_3G,response_group_3G)
   if tech == '2G' or tech == 'GSM':
     open_session_ENM(cmds_2G,fetch_2G,elements_2G,response_group_2G)
else:
   print('It seems not all parameter given.')
   print('python p.py LTE BUE15 BUE151_08 - finds radio for LTE cell BUE151_08')
   print('python p.py 5G BUE15 BUE151N1_35 - finds radio for NR cell BUE151N1_35')
   print('python p.py 3G BUE11 S1C1 - finds radio for WCDMA cell sector 1, carrier 1')
   print('python p.py 2G BUE11 1-0  - finds radio for Gsm Sector 1, TRX 0')
print('The END') 
