import sys 
import volatility.plugins.taskmods as taskmods
import volatility.plugins.imageinfo as imageinfo
import libapi
import sqlite3

def sqlite_pslist_processing(procs_list):
    conn = sqlite3.connect('VolTest.db')
    c = conn.cursor()











    for proc in procs_list:
        process_data = ""
        for item in proc:
            
        to_exe = "INSERT INTO processes VALUES({0})".format(proccess_data)
    c.execute(bro)
    
    conn.commit()
    c.close()
    conn.close() 
              
def process_list(config):
    '''Prints out the info in a good way'''
    data = libapi.get_json(config, taskmods.PSList) 

   sqlite_processing(data['rows']) #a list of lists that cotain data for each process 


    #name_index = data['columns'].index('Name') 
    #print
    #for row in data['rows']:
    #    proc_name = row[name_index]
    #    sqlite_processing(proc_name) 

def main():

    config = libapi.get_config("WinXPSP2x86","/home/ml-petridish/cridex.vmem" )
    process_list(config)

    
if __name__ == "__main__":
    main()
