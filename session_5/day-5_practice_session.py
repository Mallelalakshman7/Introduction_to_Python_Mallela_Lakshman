#contactbook

def contact_book():
        contacts={}
        while True:
                choice=input("1 add, 2 search, 3 list, 0 quit: ")
                if choice=='1':
                        name=input("Enter the name")
                        phone=input("enter the phone number")
                        if name not in contacts:
                                contacts[name]=[]
                        contacts [name].append(phone)
                elif choice=='2':
                        name=input("Enter the name")
                        print(contacts.get(name, "Not found"))
                elif choice=='3':
                        for name in sorted(contacts):
                                print(f"{name:<5}",",".join(contacts[name]))
                elif choice=='0':
                        break
                        

contact_book()

#Word Report 
def word_report():
        with open("text.txt",encoding="utf-8") as f:
                text=f.read().lower()
        for p in ".,!?;":
                text=text.replace(p," ")
        words=text.split()
        word_count={}
        for word in words:
                word_count[word]=word_count.get(word,0)+1
        with open("report.txt","w",encoding="utf-8") as f:
                f.write(f"Words: {len(words)}\n")
                f.write(f"Unique words: {len(word_count)}\n")
                for word in sorted(word_count):
                        f.write(f"{word:<15}{word_count[word]}\n")
        print("Report Saved")

word_report()