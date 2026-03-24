import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile
import smtplib
from email.message import EmailMessage

def zip_file(FolderName):
    print("File name for zip :", FolderName)
    time_stamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    zip_name = FolderName +"_" + time_stamp + ".zip" 

    zobj = zipfile.ZipFile(zip_name , "w", zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(FolderName):
        for file in files:
            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, FolderName)

            zobj.write(src_path, rel_path)

    zobj.close()

    return zip_name

def ExtractZipFile(ZipFileName, Destination):
    zip_file_path = os.path.abspath(ZipFileName)

    zip_folder = Destination
    os.makedirs(Destination, exist_ok= True)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(zip_folder)

def SendMail(folder, sender,app_password,receiver):
    sender_email = "automationpython.test@gmail.com"
    app_password = "bokv dbia aezc siop"
    receiver_email = "sagartg4040@gmail.com"
    
    msg = EmailMessage()

    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Marvellous Data Shield System"
    
    body = f"""
        Please find attached log file and zipfile.
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

def CreateLog(FolderName,Source, BackupName):
    Border = "-"*50
    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to create folder")
            return

    else:
        os.mkdir(FolderName)
        print("Directory for log files gets created succesfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
    print("Log file gets created with name : ",FileName)

    fobj = open(FileName, "w")

    fobj.write(Border+"\n")
    fobj.write("--------- Marvellous Data Shield System ----------\n")
    fobj.write("Log created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    Copied_Files, Time_Taken, Start_Time  = BackupFiles(Source, BackupName)
    zip_file_name = zip_file(BackupName)

    fobj.write(f"Start time of backup the files : {time.ctime(Start_Time)}\n")
    fobj.write(f"Number of File copied in backup folder : {len(Copied_Files)}\n")
    fobj.write(f"Name of zip of backup folder : {zip_file_name}\n")
    fobj.write(f"Time taken to backup the files : {Time_Taken}\n")
    
    fobj.write("\n"+Border+"\n")
    fobj.write("----------------- End of Log File ----------------\n")
    fobj.write(Border+"\n")

def calculate_hash(path):
    hobj = hashlib.md5()

    fobj = open(path,"rb")

    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)

    fobj.close()

    return hobj.hexdigest()

def BackupFiles(Source, Destination):
    copied_files = []

    print("Creating the Backup folder for backup process")
    Start_Time = time.time()

    os.makedirs(Destination, exist_ok= True)

    for root, dirs, files in os.walk(Source):
        for file in files:
            src_path = os.path.join(root,file)

            relative = os.path.relpath(src_path,Source)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path),exist_ok= True)
    
            Extension = file.split('.')
            if(Extension[-1] != 'tmp' and Extension[-1] != 'log' and Extension[-1] != 'exe'):
                if((not os.path.exists(dest_path)) or (calculate_hash(src_path) != calculate_hash(dest_path))):
                    shutil.copy2(src_path, dest_path)
                    copied_files.append(relative)

    End_Time = time.time()
    Time_Taken = End_Time - Start_Time

    return copied_files, Time_Taken, Start_Time

    
def MarvellousDataShieldStart(Source):
    BackupName = "MarvellousBackup"
    FolderName = "LogFiles"
    print("Backup Process Started succesfully at : ", time.strftime("%Y-%m-%d_%H-%M-%S"))

    CreateLog(FolderName ,Source, BackupName)

def main():

    Border = "-"*50
    print(Border)
    print("--------- Marvellous Data Shield System ----------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("\nThis scipt is used to : ")
            print("1 : Takes auto backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create an archive of the backup periodically\n")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("\nUse the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval     : The time in minutes for periodic scheduling")
            print("SourceDirectory  : Name of directory to backed up\n")

        else:
            print("\nUnable to proceed as there is no such option")
            print("Please use --h or --u to get more details\n")
    
    # python Demo.py 5 Data
    elif(len(sys.argv) == 3):
        print("Time interval : ",sys.argv[1])
        print("Directory name : ",sys.argv[2])

        # Apply the schedular
        #schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart, sys.argv[2])
        schedule.every(int(sys.argv[1])).seconds.do(MarvellousDataShieldStart, sys.argv[2])

        print("\nData Shield System started succesfully")
        print("Time interval in minutes: ",sys.argv[1])
        print("Press Ctrl + C to stop the execution\n")

        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    elif(len(sys.argv) == 4):
        if sys.argv[1].lower() == "--restore":
            ExtractZipFile(sys.argv[2], sys.argv[3])
        else :
            print("\nUnable to proceed as there is no such option")
            print("Use below mentioned command :")
            print("ScriptName.py --restore <ZipFileName> <Destination>")
            print("--restore       : Extracts files from the specified zip archive.")
            print("ZipFileName     : Name of the zip file to be extracted.")
            print("Destination     : Directory where the files will be extracted.\n")
    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details") 

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)
    
if __name__ == "__main__":
    main()