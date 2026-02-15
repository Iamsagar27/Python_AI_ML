import sys
import os
import time
import schedule
import psutil
import tabulate
import smtplib
from email.message import EmailMessage

def CreateLog(Folder):
    Border = "-"*50
    Ret = False

    Ret = os.path.exists(Folder)

    if Ret == True:
        Ret = os.path.isdir(Folder)
        if Ret == False:
            print("Unable to create folder")
    else :
        os.mkdir(Folder)
        print("Directory for log files gets created successfully")

    time_stamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    File_Name = os.path.join(Folder, "Marvellous_%s.log" % time_stamp)
    print("Log file gets created with name :", File_Name)

    fobj = open(File_Name, "w")

    fobj.write(Border +"\n")
    fobj.write("---- Marvellous Platform Surveillance System -----"+"\n")
    fobj.write("Log created at :"+ time.ctime() + "\n")
    fobj.write(Border +"\n\n")

    fobj.write("---------------- System Report -------------------\n")

    fobj.write("CPU Usage : %s %%\n" % psutil.cpu_percent())

    fobj.write("RAM Usage : %s %%\n" %psutil.virtual_memory().percent)
    fobj.write(Border +"\n")

    fobj.write("\n---------------- Disk Usage Report ---------------\n")
    for part in psutil.disk_partitions():
        try :
            usage = psutil.disk_usage(part.mountpoint)
            fobj.write("%s -> %s %% used \n" %(part.mountpoint, usage.percent))
        except:
            pass
    fobj.write(Border +"\n")

    net = psutil.net_io_counters()
    fobj.write("\n-------------- Network Usage Report --------------\n")
    fobj.write("Sent : %.2f MB\n" %(net.bytes_sent / (1024*1024)))
    fobj.write("Recv : %.2f MB\n" %(net.bytes_recv / (1024*1024)))
    fobj.write(Border +"\n")

    Data = ProcessScan()

    ProcessTable = []
    Header = ["PID", "Name", "UserName", "Status", "Start Time", "CPU %", "Memory %", "Thread Count", "Open Files"]

    process_count = len(Data)
    SortedData = sorted(Data, key= lambda x :x.get("memory_percent", 0), reverse=True)[:10]
    for info in SortedData:
        ProcessTable.append([
            info.get("pid"),
            info.get("name"),
            info.get("username"),
            info.get("status"),
            info.get("create_time"),
            info.get("cpu_percent"),
            info.get("memory_percent"), 
            info.get("num_threads"), 
            info.get("open_files"), 
        ])
    fobj.write("\n------------------ Process Report ----------------\n")
    fobj.write(tabulate.tabulate(ProcessTable, headers=Header, tablefmt="grid"))

    fobj.write("\n" +Border +"\n")
    fobj.write("---------------- End of Log file -----------------"+"\n")
    fobj.write(Border +"\n")

    fobj.close()
    return Data, process_count


def SendMail(folder, sender,app_password,receiver):
    File_Content, process_count = CreateLog(folder)
    
    msg = EmailMessage()

    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = "Marvellous Platform Surveillance System"
    
    body = f"""Summary :\n
        Total Processess - {process_count} \n
        Top Running Process :
        Top CPU usage process: {sorted(File_Content, key= lambda x :x.get("cpu_percent", 0), reverse=True)[0]['cpu_percent']} 
        Top Memory usage process: {sorted(File_Content, key= lambda x :x.get("memory_percent", 0), reverse=True)[0]['memory_percent']}
        Top Thread count process: {sorted(File_Content, key= lambda x :x.get("num_threads", 0), reverse=True)[0]['num_threads']}
        Top Open File Process: {sorted(File_Content, key= lambda x :x.get("open_files", 0), reverse=True)[0]['open_files']}
    """
    msg.set_content(body)


    files = os.listdir(folder)
    files.sort()

    latest_file = files[-1]
    file_path = os.path.join(folder, latest_file)

    with open(file_path, "rb") as f:
        file_data = f.read()

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="octet-stream",
        filename=latest_file
    )

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    smtp.login(sender, app_password)

    smtp.send_message(msg)

    smtp.quit()
    

def ProcessScan():
    listprocess = []

    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass
    
    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid", "name", "username","status", "create_time", "num_threads", "open_files"])

            try:
                info["create_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(info["create_time"]))            
            except :
                info["create_time"] = "NA"

            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            process = psutil.Process(info["pid"])
            info["num_threads"] = process.num_threads()
            info["open_files"] = len(process.open_files())

            listprocess.append(info)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listprocess

def main():
    Border = "-"*50
    print(Border)
    print("--------- Marvellous Platform Surveillance System ----------")
    print(Border)

    if(len(sys.argv) == 2) :
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to")
            print("1 : Create automatic logs")
            print("2 : Executes priodically")
            print("3 : Send mail with the log")
            print("4 : Store information about processess")
            print("5 : Store information about CPU")
            print("6 : Store information about RAM usage")
            print("7 : Store information about secondary storage")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("DirectoryName : Name of directory to create auto logs")

        else :
            print("Unable to proceed as there is no option")
            print("Please use --h or --u for more details")
    
    # py Demo.py 5 Marvellous
    elif (len(sys.argv) == 4) :
        sender_email = "automationpython.test@gmail.com"
        app_password = "bokv dbia aezc siop"

        # Apply the schedular
        schedule.every(int(sys.argv[3])).minutes.do(SendMail, sys.argv[1], sender_email, app_password, sys.argv[2])
        #schedule.every(int(sys.argv[1])).seconds.do(CreateLog, sys.argv[2])

        print("Platform Surveillance System Started successfully")
        print("Directory created with name : ",sys.argv[2])
        print("Time interval in minutes : ",sys.argv[1])
        print("Press Ctrl + C to stop the execution")
        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else :
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no option")
        print("Please use --h or --u for more details")

    print(Border)
    print("--------- Thank You for using our Script ---------")
    print(Border)

if __name__ == "__main__":
    main()