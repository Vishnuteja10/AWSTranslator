# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter as tk
import boto3

root=tk.Tk()
root.geometry("400x240")
root.title("AWS Translator")
textExample=tk.Text(root,height=10)
textExample.pack()
def getText():
    aws_mag_con=boto3.session.Session(profile_name='demo_user2')
    client=aws_mag_con.client(service_name='translate',region_name='us-east-1')
    result = textExample.get("1.0","end")
    print(result)
    response=client.translate_text(Text=result,SourceLanguageCode='en',TargetLanguageCode='te')
    print('Translated Text:'+response.get('TranslatedText'))
    print("Source Language Code:"+response.get('SourceLanguageCode'))
    print("Target Language Code:"+ response.get('TargetLanguageCode'))


btnRead = tk.Button(root,height=1,width=10,text="Read",command=getText)
btnRead.pack()
root.mainloop()

